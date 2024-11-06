from flask import Flask, render_template, request, session, redirect
from netmiko import ConnectHandler
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure secret key

device_info = {
    'device_type': 'generic', ##use specific device for your application according to Netmiko
    'ip': '',
    'username': '',
    'password': '',
}

# Dictionary to hold port statuses
port_statuses = {f"port_{i}": False for i in range(1, 9)}


def get_port_statuses():
    """
    Connects to the device and retrieves the status of all ports.
    Updates port_statuses based on the output of 'YOUR COMMAND TO CHECK STATUS OF ALL PORTS ON DEVICE'. # use specific command to check port status
    """
    try:
        device_info.update({
            'ip': session.get('ip'),
            'username': session.get('username'),
            'password': session.get('password'),
        })
        with ConnectHandler(**device_info) as ssh_conn:
            output = ssh_conn.send_command("YOUR COMMAND TO CHECK STATUS OF ALL PORTS ON DEVICE") # use specific command to check port status
            for i in range(1, 9):
                eth_port = f"eth{i}"
                port_statuses[f"port_{i}"] = eth_port in output
    except Exception as e:
        print(f"Error retrieving port statuses: {str(e)}")
        return "Error retrieving port statuses."


def toggle_port(port):
    """
    Toggles the specified port on or off and updates port status.
    """
    eth_interface = f"eth{port.split('_')[1]}"
    port_statuses[port] = not port_statuses[port]
    command = f"SET COMMAND {eth_interface}  {'enable' if port_statuses[port] else 'disable'}" # use specific command to set port state to enable or disable

    try:
        with ConnectHandler(**device_info) as ssh_conn:
            output = ssh_conn.send_command(command)
        return output
    except Exception as e:
        return f"Error toggling port: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        if 'login' in request.form:
            # Store IP, username, and password in the session
            session['ip'] = request.form['ip']
            session['username'] = request.form['username']
            session['password'] = request.form['password']

            # Update device info for the first login
            device_info.update({
                'ip': session['ip'],
                'username': session['username'],
                'password': session['password'],
            })

            # Get the initial port statuses
            get_port_statuses()

        elif 'port' in request.form:
            # Toggle port status
            port = request.form.get("port")
            if port:
                output = toggle_port(port)
                get_port_statuses()  # Refresh port statuses after toggling

        elif 'logout' in request.form:
            # Logout and clear session
            session.clear()
            return redirect("/")

    elif session.get("ip"):
        # If already logged in, refresh port statuses
        get_port_statuses()

    return render_template("index.html", output=output, port_statuses=port_statuses,
                           ip=session.get("ip", ""), username=session.get("username", ""), password=session.get("password", ""))

if __name__ == "__main__":
    app.run(debug=True)
