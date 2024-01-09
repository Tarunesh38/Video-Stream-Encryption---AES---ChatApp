import tkinter as tk
import encryptVid as ev

# Main Window
root = tk.Tk()
root.title(" Video Encryption ")
root.geometry("300x300")

sending = False
recieving = False
key = "1234567890123456".encode('utf-8')  # Give Key of 16 bytes = 128 bits = 10 rounds of AES

# send action for the send button
def send_action(ip, port):
    global send_status_bar
    global sending
    if sending:
        return
    sending = True
    # Create a sender object
    try:
        sender = ev.Transmitter(ip, port, key)
        sender.start()
        send_status_bar.config(text=f"Sending to {ip}:{port}")
        print("Sending to {}:{}".format(ip, port))
        print("Sending...")
    except:
        print(" -> Need an active Listener on that port !")
        return
# Sub Window for Sending
def send():
    global send_window
    send_window = tk.Toplevel(root)
    send_window.title(" Send Video ")
    send_window.geometry("300x300")
    send_window.resizable(False, False)

    # Label for IP
    ip_label = tk.Label(send_window, text="IP Address: ")
    ip_label.pack()

    # Entry for IP
    ip_entry = tk.Entry(send_window)
    ip_entry.insert(0, "localhost")
    ip_entry.pack()

    # Label for Port
    port_label = tk.Label(send_window, text="Port: ")
    port_label.pack()

    # Entry for Port
    port_entry = tk.Entry(send_window)
    port_entry.insert(0, "9090")
    port_entry.pack()

    # Button to start sending video
    send_button = tk.Button(send_window, text="Send", command=lambda:send_action(ip_entry.get(), int(port_entry.get())))
    send_button.pack()

    # Info Label
    info_label = tk.Label(send_window, text=" Press Q on the video capture to stop sending ")
    info_label.pack()

    # Status bar that updates with various system messages
    global send_status_bar
    send_status_bar = tk.Label(send_window, text="Ready!")
    send_status_bar.pack()

    # transient of root
    send_window.transient(root)
    send_window.grab_set()
    root.wait_window(send_window)

# recieve action for the recieve button
def recieve_action(ip, port):
    global recieve_status_bar
    global recieving
    if recieving:
        recieve_status_bar.config(text=f"Already Recieving at {ip}:{port}")
        return
    recieving = True
    # Create a reciever object
    reciever = ev.Reciever(ip, port, key)
    # Start the reciever thread
    reciever.start()
    print("Waiting for Incoming Connection at {}:{}".format(ip, port))
    print("Recieving...")
    recieve_status_bar.config(text=f"Waiting for Incoming Connection at {ip}:{port}")
# Sub Window for Recieving
def recieve():
    global recieve_window
    recieve_window = tk.Toplevel(root)
    recieve_window.title(" Recieve Video ")
    recieve_window.geometry("300x300")
    recieve_window.resizable(False, False)

    # Label for IP
    ip_label = tk.Label(recieve_window, text="IP Address: ")
    ip_label.pack()

    # Entry for IP
    ip_entry = tk.Entry(recieve_window)
    ip_entry.insert(0, "localhost")
    ip_entry.pack()

    # Label for Port
    port_label = tk.Label(recieve_window, text="Port: ")
    port_label.pack()

    # Entry for Port
    port_entry = tk.Entry(recieve_window)
    port_entry.insert(0, "9090")
    port_entry.pack()

    # Button to start recieving video
    recieve_button = tk.Button(recieve_window, text="Recieve", command=lambda:recieve_action(ip_entry.get(), int(port_entry.get())))
    recieve_button.pack()

    # Text Label Explaining how to close video display
    info_label = tk.Label(recieve_window, text=" Press Q on the Video Display Window \nto close video stream ")
    info_label.pack()

    # Status bar that updates with various system messages
    global recieve_status_bar
    recieve_status_bar = tk.Label(recieve_window, text="Ready!")
    recieve_status_bar.pack(anchor=tk.S)

    # transient of root
    recieve_window.transient(root)
    recieve_window.grab_set()
    root.wait_window(recieve_window)

# Group Members
def group_members():
    grp_window = tk.Toplevel(root)
    grp_window.title(" Group Members ")
    grp_window.resizable(False, False)

    # Label for Group Members
    grp_label = tk.Label(grp_window, text="Group Members", font=("Helvetica", 20))
    grp_label.pack()

    # Frame for Members
    member_frame = tk.Frame(grp_window)
    
    # Label for Members
    member_label = tk.Label(member_frame, text="Parthvi Manoj")
    member_label.grid(row=0, column=0)
    rollno_label = tk.Label(member_frame, text="CB.EN.U4AIE21143")
    rollno_label.grid(row=0, column=1)

    member_label = tk.Label(member_frame, text="Sakthi Swaroopan S")
    member_label.grid(row=1, column=0)
    rollno_label = tk.Label(member_frame, text="CB.EN.U4AIE21159")
    rollno_label.grid(row=1, column=1)

    member_label = tk.Label(member_frame, text="Sanjay Chidambaram")
    member_label.grid(row=2, column=0)
    rollno_label = tk.Label(member_frame, text="CB.EN.U4AIE21160")
    rollno_label.grid(row=2, column=1)

    member_label = tk.Label(member_frame, text="Taruneshwaran")
    member_label.grid(row=3, column=0)
    rollno_label = tk.Label(member_frame, text="CB.EN.U4AIE21170")
    rollno_label.grid(row=3, column=1)

    member_frame.pack()

    # transient of root
    grp_window.transient(root)
    grp_window.grab_set()
    root.wait_window(grp_window)


# Title Label
title_label = tk.Label(root, text=" Video Encryption ", font=("Helvetica", 26, "bold"))
title_label.pack(padx=10, pady=10)

# Button to Display Group Members
group_button = tk.Button(root, text="Group Members",font=('Helvatica',16,'bold'), command=group_members)
group_button.pack(fill=tk.X, pady=10)

# Button to start recieving video/sending video(/quit
send_button = tk.Button(root, text="Send",font=('Helvatica',12), command=send)
send_button.pack(fill=tk.X)
recieve_button = tk.Button(root, text="Recieve",font=('Helvatica',12), command=recieve)
recieve_button.pack(fill=tk.X)
quit_button = tk.Button(root, text="Quit",font=('Helvatica',12), command=root.destroy)
quit_button.pack(fill=tk.X)

root.mainloop()
