import json, datetime, sys

from bs4 import BeautifulSoup
from urllib.error   import *
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

    def getAllSinceYesterday(self):
        #self.printIndexResponce()
        date = datetime.date.today()
        print(date)
        print("------{num} posts------".format(num=len(self.responce)))
        self.getAllSinceDate(date="")

    def getAllSinceDate(self, date):
        for post in self.responce:
            pass
    
    def printIndexResponce(self):
        print("------{num} posts------".format(num=len(self.responce)))
        for post in self.responce:
            print("#=#=#=#=#=#=#=#=#=#")
            for key in post:
                print("{key} => {value}".format(key=key, value=post[key]))
        
        print("------{num} posts------".format(num=len(self.responce)))

    def printResponce(self):
        # this function attempts to print out the contents of the JSON responce object returned by self.getJsonData()
        # in a legible format.
        for key in self.responce:
            print(key)

    def printData(self):
        # this function prints out the contents of self.data in a legible format
        for key in self.data:
            print(key, " = ", self.data[key])

    def getPoolInfo(self):
        # As part of the JSON object returned by self.getJsonData(), there are certain key-value pairs that
        # contain data about the pool in question. The keys that are belived to be relevent are supplied by
        # self.dataKeys.
        # Parse self.responce to extract information about the pool
        for key in self.dataKeys:
            self.data[key] = self.responce[key]

    def getPostInfo(self):
        # this function returns requested values from a list of supplied keys
        # in the JSON object returned by self.getJsonData(), there is a DICT containing several key-value pairs
        # when given a list of keys by self.postKeys this functions returns the values associated with those keys
        # example: ["author", "file_url"] would return these key values out of the responce data
        # this list is stored in the value self.data["posts"]; accesable by the parent class that created this 
        # scrapper object.
        self.data["posts"] = []
        for post in self.responce["posts"]: # for every post in the list of posts
            self.data["posts"].append({})   # add an empty dict to the post data; this will serve as a container for the requested data
            for key in self.postKeys:       # then for every key in the list of requested keys
                self.data["posts"][-1][key] = post[key] # Select the most recently added post data dict, and add the requested key along with its value
        
    def getJsonData(self, url):
        # This function takes a url and expects to get a JSON responce back from it. If the responce is not in JSON format the function throws an error.
        try:
            # The modified user agent is not always needed but is a solidly useful precaution!
            req = Request(url, headers=self.userAgent)
            x = urlopen(req).read().decode("utf-8")
            return json.loads(x)
        except json.decoder.JSONDecodeError as e:
            print("RESPONCE WAS NOT IN JSON FORMAT")
            print(e)

        except URLError as e:
            print(e)
            print("Do you have an internet connection?")
            sys.exit()
