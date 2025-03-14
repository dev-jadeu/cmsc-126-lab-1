class NetworkLayer:
    """The layer that simulates IP addressing and packet routing"""

    def send(self, data: str) -> dict:
        """Wraps the payload with source and destination IPs

        Args:
            data (str): The message to send

        Returns:
            dict: A dictionary with IP headers and payload
        """
        # Indicator that this is the active layer during execution
        print("\033[94m[NETWORK LAYER] Adding IP header\033[0m")

        # Returns the dictionary that simulates a simplified IP packet
        return {
            "source_ip": "192.168.1.1",
            "destination_ip": "192.168.1.2",
            "payload": data
        }

    def receive(self, data: dict) -> str:
        """Extracts payload from the received IP packet

        Args:
            data (dict): IP packet containing the payload

        Returns:
            str: The original payload message
        """
        # Logs the source and destination IP addresses for tracing
        print(f"\033[94m[NETWORK LAYER] Frame from {data['source_ip']} to {data['destination_ip']}\033[0m")

        # Returns the payload from the IP packet
        return data["payload"]
