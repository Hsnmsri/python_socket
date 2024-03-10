import socket

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'  # Change this to the server's IP address
SERVER_PORT = 12345      # Change this to the server's port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
    
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    
    # Receive data from the server
    data = client_socket.recv(1024)
    
    # Print the received data
    print(f"Received data from server: {data.decode()}")
