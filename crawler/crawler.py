from bs4 import BeautifulSoup
import requests

class Crawler:
    def __init__(self, parser):
        try:
            req = requests.get(parser.TARG_URL)
            self.soup = BeautifulSoup(req.text, 'html.parser')
            self.parser = parser
        except:
            pass
    def parse(self):
        return self.parser.parse(self.soup)


