class SessionLayer:
    """The layer that manages connection states and synchronization"""

    def send(self, data: str) -> dict:
        """Wraps data with session ID

        Args:
            data (str): The message to send

        Returns:
            dict: A dictionary with session ID and payload
        """
        # Indicator that this is the active layer during execution
        print("\033[92m[SESSION LAYER] Adding session ID\033[0m")

        # Returns the dictionary that simulates a session ID
        return {
            "session_id": "128970",
            "payload": data
        }

    def receive(self, data: dict) -> str:
        """Extracts payload and displays the session ID

        Args:
            data (dict): Contains session ID and payload

        Returns:
            str: The original payload message
        """
        # Prints the session ID
        print("\033[92m[SESSION LAYER] Session ID: {data['session_id']}\033[0m")

        # Returns the payload from the session-wrapped data
        return data["payload"]
