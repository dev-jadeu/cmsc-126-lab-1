import pickle

class PresentationLayer:
    """The layer that handles encryption, compression, and encoding"""

    def send(self, data: str) -> bytes:
        """Simulates the serialization of string data into binary format

        Args:
            data (str): The message to serialize

        Returns:
            bytes: The serialized message in binary form
        """
        # Log of serializing data
        print("\033[36m[PRESENTATION LAYER] Serializing data\033[0m")

        # Serialize the data by converting the string to bytes stream
        return pickle.dumps(data)

    def receive(self, data: bytes) -> str:
        """Simulates the deserialization of binary data into string format

        Args:
            data (bytes): The binary data to deserialize

        Returns:
            str: The original deserialized string
        """
        # Log of deserializing data
        print("\033[36m[PRESENTATION LAYER] Deserializing data\033[0m")

        # Deserialize the binary data back into a string
        return pickle.loads(data)
