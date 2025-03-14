class DataLinkLayer:
    """The layer that implements a MAC addressing system and frame transmission"""

    def send(self, data: str) -> dict:
        """Wraps the payload in a frame with MAC addressing information

        Args:
            data (str): The packet to send

        Returns:
            dict: A simulated data frame with MAC addressing and payload
        """
        # Indicator that this is the active layer during execution
        print("\033[95m[DATA LINK LAYER] Adding MAC header\033[0m")

        # Returns the dictionary that simulates a simplified Ethernet frame
        return {
            "source_mac": "7C:5A:C3:91:2D:AF",
            "destination_mac": "8C:3A:5D:21:FA:33",
            "payload": data
        }

    def receive(self, data: dict) -> str:
        """Extracts the payload from the received data frame

        Args:
            data (dict): A frame with MAC headers and payload

        Returns:
            str: The extracted payload from the frame.
        """
        # Logs the source and destination MAC addresses for tracing
        print(f"\033[95m[DATA LINK LAYER] Frame from {data['source_mac']} to {data['destination_mac']}\033[0m")

        # Returns the payload from the frame
        return data["payload"]
