# Real-Time-Chat-Application

This project is a **real-time chat application** built using Python, featuring **end-to-end encryption** to ensure secure communication between clients. The application uses multiple encryption algorithms, including **ElGamal**, **RSA**, and **DES**, and provides an interactive GUI with features like joining chat rooms, sending and receiving messages, and aliasing.

## Key Features

- **Real-Time Messaging**: Instant communication between multiple users connected to the same server.
- **Encryption Options**: Choose from **DES (Data Encryption Standard)**, **ElGamal**, or **RSA (Rivest–Shamir–Adleman)** for message encryption.
- **User Aliasing**: Enter an alias upon joining a chat room for easy identification.
- **Secure Key Exchange**: Uses RSA and ElGamal for secure key exchanges, ensuring that the session remains confidential.
- **Interactive GUI**: User-friendly interface for joining chat rooms, sending/receiving messages, and viewing the chat log.

## How It Works

The server runs on a predefined IP and port and listens for incoming client connections. Once a client joins, they choose their alias and encryption method. A session key is generated for the user, and the messages are securely transmitted using the selected encryption technique.

### Encryption Algorithms:
1. **DES**: A symmetric key algorithm for encrypting message blocks.
2. **ElGamal**: An asymmetric key encryption for encrypting data based on public-private key pairs.
3. **RSA**: Another widely-used public-key encryption algorithm for secure data transmission.

## Files

- **client_1.py**: Client-side code that handles user input, establishes the connection to the server, and manages message sending/receiving using encryption.
- **server_1.py**: Server-side code that manages incoming connections, distributes messages to all clients, and handles the encryption logic.

## Installation and Setup

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/rituraj1314/Real-Time-Chat-Application.git
   cd Real-Time-Chat-Application
   ```

2. **Install Dependencies**:
   
   Ensure that you have Python installed on your machine. You may need to install the following libraries:

   ```bash
   pip install pycryptodome
   ```

3. **Run the Server**:
   
   Navigate to the server file and start the server:

   ```bash
   python server_1.py
   ```

4. **Run the Client**:
   
   In another terminal, navigate to the client file and start the client:

   ```bash
   python client_1.py
   ```

5. **Choose Encryption Method**:
   
   Upon starting the server, you will be prompted to select the encryption method (DES, ElGamal, RSA) that will be used during the chat session.

6. **Connect Clients**:
   
   Each client enters an alias and connects to the server. You can start chatting after successfully joining.

## Features In Detail

### 1. Encryption Algorithms:
- **DES**: Symmetric key encryption where both sender and receiver use the same key.
- **ElGamal**: Public-key cryptosystem based on discrete logarithms. Keys are exchanged securely.
- **RSA**: Asymmetric encryption algorithm for secure key exchange and message encryption.

### 2. User Aliasing:
- Each user selects an alias when joining the chatroom. Messages are tagged with the user's alias.

### 3. GUI Interface:
- Interactive GUI built using **Tkinter** for user-friendly chat experience.
- Users can easily join rooms, send messages, and view chat history in real time.

### 4. Secure Message Transmission:
- Each message is encrypted using the selected algorithm before being transmitted.
- The server securely distributes the messages to all connected clients.

### 5. Session Key:
- A unique session key is generated per user for secure communication. RSA and ElGamal handle the secure transmission of the session keys.

## Example Usage

### Starting the Server:
```bash
python server_1.py
```

### Starting the Client:
```bash
python client_1.py
```

### Select Encryption Algorithm:
- Upon running the server, select between DES, ElGamal, or RSA as the encryption algorithm.

### Chat Interaction:
- Clients input their alias, join the room, and start chatting in real time. All messages are encrypted and transmitted securely.

## Future Enhancements

- **File Sharing**: Add functionality for secure file sharing between clients.
- **Group Chats**: Enable private group chats with dedicated rooms and encryption.
- **User Authentication**: Implement a more robust authentication mechanism using public/private key certificates.

## License

This project is licensed under the MIT License.

---

This README provides a structured overview of your project, making it easy for others to understand, set up, and contribute.
