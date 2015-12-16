#! /usr/bin/python3

from scrappers import e621

class Main():
    def __init__(self):
        print("Working")
        #self.url      = "http://e621.net/post/index.json?limit=5"
        self.url      = "https://e621.net/pool/show.json?id=6520"
        self.values   = ["author", "file_url", "tags"]
        self.scrapper = e621.Scrapper(self.url, verbose=False)
        
        self.printPoolInfo()

    def printPoolInfo(self):
        print(self.scrapper.data["name"])
        print(self.scrapper.data["description"])
        print("------- {0} posts -------".format(len(self.scrapper.data["posts"])))
        for i in self.scrapper.data["posts"]:
            print(i["author"], i["file_url"])

    def printRequestedData(self):
        x = self.scrapper.getValues(self.values)
        print("########################")
        print(len(x))
        print("########################")
        for post in x:
            print("--------- {0} ---------".format(post["author"]))
            print(post["file_url"])
            print(post["tags"])

if __name__ == "__main__":
    Main()
        
