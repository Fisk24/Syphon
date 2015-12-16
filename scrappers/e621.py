import json

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Scrapper():
    def __init__(self, url, verbose=False):

        ### Return an object containing all the neccisary information to download a pool from e621.net

        self.url      = url
        self.responce = self.getJsonData(self.url)
        self.dataKeys = ["name", "description", "post_count",]
        self.postKeys = ["author", "file_url"]

        self.data     = {}

        self.getPoolInfo()
        self.getPostInfo()
        
        if verbose:
            #print(self.responce)
            self.printResponce()

    def printResponce(self):
        for key in self.data:
            print(key, " = ", self.data[key])
        '''
        for index in self.responce:
            for i in index:
                print(i, " = ", index[i])
            print("========================")
            '''

    def getPoolInfo(self):
        # Parse self.responce to extract information about the pool
        for key in self.dataKeys:
            self.data[key] = self.responce[key]

    def getPostInfo(self):
        # this function returns requested values from a list of supplied keys
        # example: ["author", "file_url"] would return these key values out of the responce data
        self.data["posts"] = []
        for post in self.responce["posts"]:
            self.data["posts"].append({})
            for key in self.postKeys:
                self.data["posts"][-1][key] = post[key]
        
    def getJsonData(self, url):
        x = urlopen(url).read().decode("utf-8")
        return json.loads(x)
