import requests

class Model:
    """
    Model is the business layer and handles all the data stuff
    """
    def __init__(self, host, port):
        """
        Initializes the model with host adress and port
        :param host: the host address
        :param port: the port number
        """
        self.host = host
        self.port = port

    def detectLanguage(self, text):
        """
        Makes REST-API Call with the text as parameter

        :param param: text
        :return: JSON response
        """
        url = "http://%s:%i/langdetect/?text=%s" % (self.host, int(self.port), text)
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return "error"

        return response.json()

