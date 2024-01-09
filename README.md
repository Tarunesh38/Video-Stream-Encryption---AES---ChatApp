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

### Workflow

<img src="https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/eaf795aa-186c-45e8-b812-aea77fcda1a0" width="500" alt="Image 1">
<img src="https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/fdf67493-8332-4a97-9177-69c48b28d155" width="500" alt="Image 2">

<img src="https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/5c31d13c-0222-45e6-8ce9-ce144b3406e9" width="700" alt="Flowchart">


### Images

![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/e7b68f24-d78a-42c8-838c-21aaf20fa4ea) ![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/5e8fa6ec-2f66-42f7-afff-3c981bed8b6f)
![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/53937411-aa0c-4125-914d-6ed0ec0cbf9e) ![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/83a83daa-c10a-4b59-b3f9-d51c5502b72d) ![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/98b3b020-b91e-4893-b972-e30a34e6c7be) ![image](https://github.com/Tarunesh38/Video-Stream-Encryption-AES-ChatApp/assets/119646778/3593e70c-3002-44fd-ae80-f298ed5771ee)




## Python Implementation

### Install the requirements

```bash
pip install pycryptodomex
```

###Running the app
- Run App.py
- Select Receive option from the GUI to receive data (acts as the server, use the IP Address of the receiver system).
- Select Send option with the Receiver IP Address.
