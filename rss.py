import requests,feedparser
url=raw_input("enter the url")
r = feedparser.parse(url) 
for i in r["entries"]:
 print "##################################"
 print "*******"+i["title"]+"*********"+"\n"+i["published"]+"\n"+i["summary"]+"\n"+i["link"]

