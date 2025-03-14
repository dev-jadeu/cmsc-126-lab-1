import json

class ApplicationLayer:
    """The layer that implements HTTP-like request-response communication"""

    def send(self, data: str) -> str:
        """Formats data into a JSON HTTP-like request

        Args:
            data (str): The raw message to send

        Returns:
            str: A JSON-formatted string representing the message
        """
        # Log of formatting data
        print("\033[32m[APPLICATION LAYER] Formatting data as HTTP-like JSON\033[0m")

        # Return the JSON-formatted string
        return json.dumps({"method": "GET", "data": data})

    def receive(self, data: str) -> str:
        """Extracts the original message from a JSON HTTP-like request

        Args:
            data (str): A JSON string containing the message

        Returns:
            str: The original message data
        """
        # Log of extracting data
        print("\033[32m[APPLICATION LAYER] Parsing HTTP-like JSON\033[0m")

        # Parse the JSON string back into a Python dictionary
        payload = json.loads(data)

        # Return the original message
        return payload["data"]
