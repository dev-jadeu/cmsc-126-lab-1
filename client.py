import socket
from layers.application_layer import ApplicationLayer
from layers.presentation_layer import PresentationLayer
from layers.session_layer import SessionLayer
from layers.transport_layer import TransportLayer
from layers.network_layer import NetworkLayer
from layers.data_layer import DataLinkLayer
from layers.physical_layer import PhysicalLayer

def main():
    debug = input("Want to print data after each layer? (y/n): ").strip().lower() == 'y'

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Initialize layers
    app_layer = ApplicationLayer()
    pres_layer = PresentationLayer()
    sess_layer = SessionLayer()
    trans_layer = TransportLayer()
    net_layer = NetworkLayer()
    data_layer = DataLinkLayer()
    phys_layer = PhysicalLayer(client_socket)

    # Create a message
    message = "Hello, Server! I'm client"

    # Pass the message through the layers
    app_data = app_layer.send(message)
    if debug: print(f"[Application Layer] {app_data}")

    pres_data = pres_layer.send(app_data)
    if debug: print(f"[Presentation Layer] {pres_data}")

    sess_data = sess_layer.send(pres_data)
    if debug: print(f"[Session Layer] {sess_data}")

    trans_data = trans_layer.send(sess_data)
    if debug: print(f"[Transport Layer] {trans_data}")

    net_data = net_layer.send(trans_data)
    if debug: print(f"[Network Layer] {net_data}")

    data_data = data_layer.send(net_data)
    if debug: print(f"[Data Link Layer] {data_data}")

    phys_layer.send(data_data)
    if debug: print(f"[Physical Layer] Sent to server")

    # Receive response from the server
    received_data = phys_layer.receive()
    net_data = data_layer.receive(received_data)
    trans_data = net_layer.receive(net_data)
    sess_data = trans_layer.receive(trans_data)
    pres_data = sess_layer.receive(sess_data)
    app_data = pres_layer.receive(pres_data)
    response = app_layer.receive(app_data)

    print(f"Hi client! Check this out: {response}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
