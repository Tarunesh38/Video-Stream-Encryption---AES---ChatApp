<<<<<<<<<<<<=========================== Java ===========================>>>>>>>>>>>>

Prerequisites
-------------
=> Java Development Kit (JDK)
=> Integrated Development Environment (IDE) - Preferably IntelliJ IDEA

Installation
------------
=> Open the Java folder (B_17_Java_VideoStreaming) in your preferred IDE, preferably IntelliJ IDEA.
=> Locate the pom.xml file in the project.
=> Open the pom.xml file and click the build icon to install the required Maven repositories for the project.

Running the Application
-----------------------
=> Open "Main_Server.java" and "Main_Client.java" in your IDE.
         ----------------       ----------------
=> If you plan to run the codes on the same system, use localhost in the code (Main_Client, line 102). Otherwise, change it to the IP address of the machine where you are running the server.
=> During the meeting login, type the IP address of the Server Machine to connect to the Server, which manages the execution of our Video Stream App. To open the client in the same system then use localhost in the panel.
=> Do not modify any information regarding the port address.

Network Configuration (Optional)
--------------------------------
=> For optimal performance, it is recommended to use a Personal Hotspot in the 5G band for a lagless connection.

Notes
-----
=> Ensure that you have the Java Development Kit (JDK) installed on your system.
=> Use IntelliJ IDEA for the best development experience.
=> Keep the server IP address and port information unchanged for proper functioning.
=> Follow these steps, and you'll have the Java Video Streaming Application up and running smoothly.

User Authentication - UI
------------------------
=> SignUp : Enter the UserName and Password and click the SignUp button to create User
=> SignIn : Enter the already enrolled UserName and Password to Enter the meeting.

Meeting Setup and Authentication - UI
-------------------------------------
=> UserName : Enter your desired name for the meeting.
=> IP Address : Enter localhost (Same system running client and server) or IP Address (of the machine where server runs).
=> Dont make any changes to the Port
=> Password: Enter the meeting password (The first client to enter the meeting sets the password for the other clients, automatically when enters passsword for the first time in UI).

Chat Application - UI
---------------------
=> File Sharing: Click on the blue icon to browse and select a file for sending it to other users.
=> Video Streaming: Start Video Stream: Press the red button to initiate the video stream.
		    Stop Video Stream: A panel with a stop message will appear during the video stream. Click on it to end the video stream.
=> Text Messaging: Send Text Messages: Press the green button or hit 'Enter' to send text messages. Emojis are also supported.
=> Leaving the Meeting: To exit the meeting, click on the 'X' button.