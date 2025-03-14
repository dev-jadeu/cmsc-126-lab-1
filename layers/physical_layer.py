import struct
import pickle
import socket

class PhysicalLayer:
    """The layer that simulates the usage of Python sockets and bit-level operations"""

    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send(self, data: dict) -> None:
        """Sends serialized data over a socket with a 4-byte length prefix

        Args:
            data (dict): The structured message to transmit
        """
        # Indicator that this is the layer that is sending the data
        print("\033[96m[PHYSICAL LAYER] Sending over socket\033[0m")

        # Serialize the data by converting the Python object to a stream bytes
        serialized_data = pickle.dumps(data)

        # Packs the length of the serialized data into a 4-bytes using big-endian
        length = struct.pack('!I', len(serialized_data))

        # Send the length and the serialized data
        self.sock.sendall(length + serialized_data)

    def receive(self) -> dict:
        """Receives serialized data from a socket, deserializes it, and returns it as a dictionary

        Returns:
            dict: The deserialized message structure
        """
        # Indicator that this is the layer that is receiving the data
        print("\033[96m[PHYSICAL LAYER] Receiving from socket\033[0m")

        # Read the first 4 bytes to get the length of the serialized data
        raw_length = self.receive_bytes(4)

        # If nothing is received, raise a connection close message
        if not raw_length:
            raise ConnectionError("Nothing is received, connection closed")

        # Convert the 4-byte length into an integer
        length = struct.unpack('!I', raw_length)[0]

        # Calls the receive_bytes helper function to get the exact number of the actual data
        serialized_data = self.receive_bytes(length)

        # Deserialize the received bytes back into a Python object
        return pickle.loads(serialized_data)

    def receive_bytes(self, n: int) -> bytes:
        """Helper method to receive exactly n bytes from the socket

        Args:
            n (int): The number of bytes to read

        Returns:
            bytes: The received bytes
        """
        # Initialize empty bytes object
        data = b''

        # Loop until the length of the data is equal to n
        while len(data) < n:
            # Receives the remaining bytes needed
            packet = self.sock.recv(n - len(data))

            # Raise an error if the connection is closed before all data is received
            if not packet:
                raise ConnectionError("Socket connection closed before receiving all data")

            # Appends the received bytes to the data
            data += packet

        # Returns the received bytes
        return data