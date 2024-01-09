# Video Streaming Application

## Java Implementation

### Prerequisites

- Java Development Kit (JDK)
- Integrated Development Environment (IDE) - Preferably IntelliJ IDEA

### Installation

1. Open the Java folder (`B_17_Java_VideoStreaming`) in your preferred IDE, preferably IntelliJ IDEA.
2. Locate the `pom.xml` file in the project.
3. Open the `pom.xml` file and click the build icon to install the required Maven repositories for the project.

### Running the Application

1. Open `Main_Server.java` and `Main_Client.java` in your IDE.
2. If running codes on the same system, use `localhost` in the code (`Main_Client`, line 102). Otherwise, change it to the IP address of the server machine.
3. During the meeting login, type the IP address of the Server Machine to connect to the Server.
4. Do not modify any information regarding the port address.

### Network Configuration (Optional)

- For optimal performance, it is recommended to use a Personal Hotspot in the 5G band for a lagless connection.

### Notes

- Ensure that you have the Java Development Kit (JDK) installed on your system.
- Use IntelliJ IDEA for the best development experience.
- Keep the server IP address and port information unchanged for proper functioning.

### User Authentication - UI

- **SignUp:** Enter the UserName and Password and click the SignUp button to create a User.
- **SignIn:** Enter the already enrolled UserName and Password to enter the meeting.

### Meeting Setup and Authentication - UI

- **UserName:** Enter your desired name for the meeting.
- **IP Address:** Enter `localhost` (Same system running client and server) or IP Address (of the machine where the server runs).
- Don't make any changes to the Port.
- **Password:** Enter the meeting password.

### Chat Application - UI

- **File Sharing:** Click on the blue icon to browse and select a file for sending it to other users.
- **Video Streaming:** 
  - Start Video Stream: Press the red button to initiate the video stream.
  - Stop Video Stream: A panel with a stop message will appear during the video stream. Click on it to end the video stream.
- **Text Messaging:** 
  - Send Text Messages: Press the green button or hit 'Enter' to send text messages. Emojis are also supported.
- **Leaving the Meeting:** To exit the meeting, click on the 'X' button.

## Python Implementation

### Install the requirements

```bash
pip install pycryptodomex
```

###Running the app
- Run App.py
- Select Receive option from the GUI to receive data (acts as the server, use the IP Address of the receiver system).
- Select Send option with the Receiver IP Address.
