
import json
from urllib.request import urlopen

class GetRequester:

    def __init__(self, url):
        if not isinstance(url,str):
            raise TypeError("url must be a string")
        self.url = url

    def get_response_body(self):
        with urlopen(self.url) as response:
            return response.read()

    def load_json(self):
        body=self.get_response_body()
        return json.loads(body)