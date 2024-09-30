# server.py
import socket
import threading
import secrets
import el_gamal
import RSA

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []  # List of all currently connected users
flagmethod = None  # Variable to store the encryption method chosen by clients


# Function to choose which security method to use
def chooseMethod():
    lst = ["DES", "ELGAMAL", "RSA"]
    print("---------Welcome to our secure chat")
    print("1- DES (Data encryption standard)")
    print("2- ElGamal encryption system")
    print("3- RSA (Rivest–Shamir–Adleman)")
    while True:
        num = input("Choose the encryption system: ")
        try:
            num = int(num)
            if num >= 1 and num <= len(lst):
                print(lst[num - 1] + " mode has been started")
                return num
            else:
                print("Invalid choice. Please enter a number between 1 and", len(lst))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def getMethod():
    return flagmethod


# Function to listen for upcoming messages from a client
def listen_for_messages(client, username, key, elgamapublickey, rsa_string):
    while True:
        message = client.recv(2048).decode('utf-8')
        print("RECV : ", message)
        if message != '':
            # Send the message to all connected clients
            final_msg = f"{username}: {message}"
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from client {username} is empty")


# Function to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())


# Function to send any new message to all the clients that are currently connected to this server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)


# Function to handle client
def client_handler(client, key):
    while True:
        username = client.recv(2048).decode('utf-8')
        print("RECV : ", username)
        if username != '':
            active_clients.append((username, client, key))
            key = secrets.token_hex(8).upper()
            n, E, D = RSA.calc()
            print("public and private key parameters: ")
            print("n: ", n)
            print("E: ", E)
            print("D: ", D)
            print("")
            print("")
            rsa_string = str(n) + "," + str(E) + "," + str(D) + ","
            elgamalpublickey = ",".join(map(str, el_gamal.generate_public_key()))
            print("elgamal public key", elgamalpublickey)

            prompt_message = "SERVER~" + f"{username} added to the chat~" + key + "~" + str(flagmethod) + "~" + elgamalpublickey + "~" + rsa_string
            send_messages_to_all(prompt_message)

            print("Session key successfully generated for " + f"{username} ==> {key}")
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, key, elgamalpublickey, rsa_string,)).start()


# Main function
def main():
    global flagmethod
    flagmethod = chooseMethod()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        key = ""
        threading.Thread(target=client_handler, args=(client, key,)).start()


if __name__ == '__main__':
    main()
