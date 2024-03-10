import socket

# Define host and port
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()
    
    print(f"Server is listening on {HOST}:{PORT}")
    
    # Accept incoming connections
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        
        print(f"Connection from {client_address} has been established.")
        
        # Handle the connection
        with client_socket:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Print the received data
            print(f"Received data from {client_address}: {data.decode()}")
            
            # Echo back the received data
            client_socket.sendall(data)
