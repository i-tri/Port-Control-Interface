# Port Control Interface

## Description
This program provides a web-based GUI to control and monitor the status of network device ports. Users can log in with the device's IP address, username, and password to interact with the device's ports. The interface allows you to enable or disable ports, and displays the current status of each port in real-time. The program uses **Python** with the **Flask** web framework and **Netmiko** to interact with the device over SSH.

## Features
- **Login**: Provides an interface to input device IP, username, and password.
- **Port Status**: Displays the status of ports (1-8) and allows enabling or disabling them.
- **Button Color Change**: The color of the port buttons changes dynamically based on whether the port is active (green) or inactive (red).
- **Logout**: Allows users to log out of the device session.

## Technologies Used
- **Flask**: Web framework for creating the GUI.
- **Netmiko**: Python library for SSH communication with network devices.
- **HTML/CSS**: For frontend development and styling.

## Installation

To get started with the project, follow these steps:

**1. Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Port-Control-Interface.git
   cd Port-Control-Interface
   ```
**2. Install dependencies: Create a virtual environment (recommended)**:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows, use 'venv\Scripts\activate'
```

Install the required Python libraries:

```bash
pip install flask netmiko
```
**3. Run the application: Start the Flask development server**:

```bash
python Port_State_GUI.py
```
The web application will be available at http://127.0.0.1:5000/.

## Configuration ##
Before running the application, make sure to set up the device's IP address, username, and password in the login form. The program will use this information to connect to the device and execute commands.

## Usage ##
1. Login: Enter the device's IP address, username, and password.
2. Port Control: Once logged in, you will see buttons for ports 1-8. These buttons indicate the current status of each port (green for active, red for inactive). Click on a button to enable or disable the corresponding port.
3. Logout: You can log out of the session at any time by clicking the Logout button.

## Example Screenshot ##

**Initial Login Screen**

<img width="350" alt="GUI-1" src="https://github.com/user-attachments/assets/42594598-8f8c-478b-8e10-c65cd6b35516">


**Login Details with Port Layout**

<img width="323" alt="GUI-2" src="https://github.com/user-attachments/assets/b4d2d0f3-e5f9-4cdb-b49b-f7eac7db078c">


**Command output**

<img width="308" alt="GUI-Command output" src="https://github.com/user-attachments/assets/b7acf464-8bc4-4d62-8206-6fcabb1100f4">


**Command Output if port state can not be changed**

This will depend on device used and command executed

<img width="307" alt="GUI-Command output error" src="https://github.com/user-attachments/assets/09993f6a-ec9e-47cd-b8e6-9c6b1e1cc6a3">



## Troubleshooting ##
- If the device is not reachable, check the network connection and ensure SSH access is enabled on the device.
- If the port buttons do not change color, verify that the correct commands are being executed and that the port status is properly read.

## License ##
This project is licensed under the MIT License - see the LICENSE file for details.




