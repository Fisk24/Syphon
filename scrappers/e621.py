import json, datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class Scrapper():
    def __init__(self, url, verbose=False):

        ### Return an object containing all the neccisary information to download a pool from e621.net

        self.url       = url
        self.responce  = ""
        self.userAgent = {'User-Agent': 'Mozilla'}
        self.dataKeys  = ["name", "description", "post_count"]
        self.postKeys  = ["author", "file_url"]

        self.data     = {}
        
        self.responce = self.getJsonData(self.url)
        #self.getPoolInfo()
        #self.getPostInfo()
        
        if verbose:
            #print(self.responce)
            self.printResponce()

    def getAllSinceYesterday():
        pass

    def getAllSinceDate():
        pass

    def printResponce(self):
        for key in self.data:
            print(key, " = ", self.data[key])

    def getPoolInfo(self):
        # Parse self.responce to extract information about the pool
        for key in self.dataKeys:
            self.data[key] = self.responce[key]

    def getPostInfo(self):
        # this function returns requested values from a list of supplied keys
        # example: ["author", "file_url"] would return these key values out of the responce data
        self.data["posts"] = []
        for post in self.responce["posts"]: # for every post in the list of posts
            self.data["posts"].append({})   # add an empty dict to the post data; this will serve as a container for the requested data
            for key in self.postKeys:       # then for every key in the list of requested keys
                self.data["posts"][-1][key] = post[key] # Select the most recently added post data dict, and add the requested key along with its value
        
    def getJsonData(self, url): 
        # The modified user agent is not always needed but is a solidly useful precaution!
        req = Request(url, headers=self.userAgent)
        x = urlopen(req).read().decode("utf-8")
        return json.loads(x)
