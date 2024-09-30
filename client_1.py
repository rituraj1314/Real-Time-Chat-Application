import socket
import tkinter as tk
import threading

HOST = '127.0.0.1'
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to the server")
        add_message("[SERVER] Successfully connected to the server")
    except:
        print("Unable to connect")
        return

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
        print("SEND : ", username.encode())
    else:
        print("Invalid username")
        return

    threading.Thread(target=listen_for_messages_from_server).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)
    username_button.pack_forget()
    username_textbox.pack_forget()
    username_label['text'] = "Welcome " + username + " to our secure room"
    username_label.pack(side=tk.LEFT)

def send_message():
    message = message_textbox.get()
    if message != '':
        message_textbox.delete(0, tk.END)
        client.sendall(message.encode("utf-8"))
        print("SEND : ", message.encode())
        print("This message has been delivered")
    else:
        print("Empty message")

def listen_for_messages_from_server():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            print("RECV : ", message)
            if message != '':
                add_message(message)
        except Exception as e:
            print("Error:", str(e))
            client.close()
            break

def add_message(message):
    message_listbox.insert(tk.END, message)

root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

username_label = tk.Label(root, text="Enter your alias:")
username_label.pack()

username_textbox = tk.Entry(root)
username_textbox.pack()

username_button = tk.Button(root, text="Join", command=connect)
username_button.pack()

message_textbox = tk.Entry(root)
message_textbox.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

message_listbox = tk.Listbox(root, width=50, height=20)
message_listbox.pack()

root.mainloop()
