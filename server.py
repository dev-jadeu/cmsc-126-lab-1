import socket
from layers.application_layer import ApplicationLayer
from layers.presentation_layer import PresentationLayer
from layers.session_layer import SessionLayer
from layers.transport_layer import TransportLayer
from layers.network_layer import NetworkLayer
from layers.data_layer import DataLinkLayer
from layers.physical_layer import PhysicalLayer

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    print("Server is listening on port 8080... until one request is received")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Initialize layers
    app_layer = ApplicationLayer()
    pres_layer = PresentationLayer()
    sess_layer = SessionLayer()
    trans_layer = TransportLayer()
    net_layer = NetworkLayer()
    data_layer = DataLinkLayer()
    phys_layer = PhysicalLayer(conn)

    # Receive data through the layers
    data_data = phys_layer.receive()
    net_data = data_layer.receive(data_data)
    trans_data = net_layer.receive(net_data)
    sess_data = trans_layer.receive(trans_data)
    pres_data = sess_layer.receive(sess_data)
    app_data = pres_layer.receive(pres_data)
    message = app_layer.receive(app_data)

    print(f"Server Received Message: {message}")

    # Secret response
    response = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    encoded_response = app_layer.send(response)
    encoded_response = pres_layer.send(encoded_response)
    encoded_response = sess_layer.send(encoded_response)
    encoded_response = trans_layer.send(encoded_response)
    encoded_response = net_layer.send(encoded_response)
    encoded_response = data_layer.send(encoded_response)
    encoded_response = phys_layer.send(encoded_response)

    print("Server Response Sent")

    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
