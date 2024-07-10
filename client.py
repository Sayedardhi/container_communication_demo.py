import socket
import numpy as np

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server', 5001))  # Use service name 'server' as the host
    
    data = np.random.random((2000, 2000)).astype(float)
    client_socket.sendall(data.tobytes())
    
    response = client_socket.recv(4096)
    print(f"Received response: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    main()