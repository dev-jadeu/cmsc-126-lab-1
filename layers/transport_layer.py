class TransportLayer:
    """The layer that implements TCP-like packet sequencing and error handling"""

    def send(self, data: str) -> dict:
        """Attaches a sequence number to the payload

        Args:
            data (str): The message to send

        Returns:
            dict: A dictionary with sequence number and payload
        """
        # Indicator that this is the active layer during execution
        print("\033[93m[TRANSPORT LAYER] Adding transport header\033[0m")

        # Returns the dictionary that simulates a simplified TCP packet
        return {
            "sequence": 0,
            "payload": data
        }

    def receive(self, data: dict) -> str:
        """Extracts payload and displays the sequence number

        Args:
            data (dict): Contains sequence number and payload

        Returns:
            str: The original payload message
        """
        # Prints the sequence number
        print("\033[93m[TRANSPORT LAYER] Sequence number: {data['source_ip']}\033[0m")

        # Returns the payload from the sequence-wrapped packet
        return data["payload"]
