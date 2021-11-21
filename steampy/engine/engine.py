import requests

class Engine:
    def __init__(self):
        pass

    def request(self, r):
        resp = requests.get(r.get_url(), headers={'Accept': 'application/json'})
        if not resp.ok:
            print(r.get_url())
            print(resp)
            print(resp.text)
        return r.response(resp)