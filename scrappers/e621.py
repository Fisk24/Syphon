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

    def getAllSinceYesterday(self):
        #self.printIndexResponce()
        # get todays date and subtract 1 day to get yesterdays date
        today = datetime.datetime.now()    # this time object represents the exact date and time of when it was created!
        delta = datetime.timedelta(days=1) # timedeltas are used to objectify amounts of time in terms of dates!
        yestr = today - delta
        print(self.responce[0]["created_at"])
        time = self.responce[0]["created_at"]["s"], self.responce[0]["created_at"]["n"]
        post = datetime.datetime.fromtimestamp(float("{s}.{n}".format(s=time[0], n=time[1])))
        print(post)
        print(self.responce[0]["file_url"])

        print(yestr < post)
        self.getAllSinceDate(date=yestr)

    def getAllSinceDate(self, date):
        posts = []
        for post in self.responce:
            jsonDate = post["created_at"]["s"], post["created_at"]["n"]
            postDate = datetime.datetime.fromtimestamp(float("{s}.{n}".format(s=jsonDate[0], n=jsonDate[1])))
            if postDate > date:
                posts.append({})
                
    
    def printIndexResponce(self):
        print("------{num} posts------".format(num=len(self.responce)))
        for post in self.responce:
            print("#=#=#=#=#=#=#=#=#=#")
            for key in post:
                print("{key} => {value}".format(key=key, value=post[key]))
        
        print("------{num} posts------".format(num=len(self.responce)))

    def printResponce(self):
        for key in self.responce:
            print(key)

    def printData(self):
        for key in self.data:
            print(key, " = ", self.data[key])

    def addPostDataByKey(self):
        pass

    def getPoolInfo(self):
        # Parse self.responce to extract information about the pool
        for key in self.dataKeys:
            self.data[key] = self.responce[key]

    def getPostInfo(self, posts=self.request["posts"]):
        # this function returns requested values from a list of supplied keys
        # example: ["author", "file_url"] would return these key values out of the responce data
        self.data["posts"] = []
        for post in posts:                  # for every post in the list of posts
            self.data["posts"].append({})   # add an empty dict to the post data; this will serve as a container for the requested data
            for key in self.postKeys:       # then for every key in the list of requested keys
                self.data["posts"][-1][key] = post[key] # Select the most recently added post data dict, and add the requested key along with its value
        
    def getJsonData(self, url): 
        # The modified user agent is not always needed but is a solidly useful precaution!
        req = Request(url, headers=self.userAgent)
        x = urlopen(req).read().decode("utf-8")
        return json.loads(x)
