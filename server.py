import socket
import numpy as np

def svd_computation(data):
    # Convert data to NumPy array and perform SVD
    array = np.frombuffer(data, dtype=float).reshape((2000, 2000))
    U, S, Vt = np.linalg.svd(array)
    return U, S, Vt

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5001))
    server_socket.listen(1)
    print("Server listening on port 5001...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Adjust the buffer size to match the data size (2000 * 2000 * 8 bytes for float64)
    buffer_size = 2000 * 2000 * 8
    data = b''
    while len(data) < buffer_size:
        packet = conn.recv(buffer_size - len(data))
        if not packet:
            break
        data += packet
    print(f"Received data of length: {len(data)}")
    
    # Perform SVD computation
    U, S, Vt = svd_computation(data)
    response = f"U shape: {U.shape}, S shape: {S.shape}, Vt shape: {Vt.shape}"
    conn.sendall(response.encode('utf-8'))
    
    conn.close()

if __name__ == "__main__":
    main()