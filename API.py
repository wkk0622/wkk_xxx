import requests

class Api:
    def __init__(self, url):
        if not url.endswith("/"):
            url += "/"
        self.url = url
    
    def __call__(self, api_name):
        ret = requests.post("{self.url}{self.api_name}")
        return ret.json()

 