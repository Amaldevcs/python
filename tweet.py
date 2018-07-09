import requests,json
from requests_oauthlib import OAuth1
API_Key= "VBTj4JqebIFDctJlztF2xpd0P"
API_Secret =  "pVlDfHthTeQhsqVqVRgNduwwQIPwXxE08LKBlzPqCq2SIAWo1J"
Access_Token ="1010899301818658820-JpNNgTA5RMIiX7Ufe9fqUAcBgz1ora"
Access_Token_Secret ="GHRf6rPmX4x0zpQ6YdLD6dboe1E71d9XHqRnJN60wRqIS"
username = raw_input ("enter the username")
print username
url=" https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&tweet_mode=extended&count=10"
auth = OAuth1(API_Key,API_Secret,Access_Token,Access_Token_Secret)
r = requests.get(url,auth=auth)
k =r.text
d= json.loads(k)
print r.status_code,d
for i in d:
 if  i["full_text"]:
  print"#"*20
  print i["full_text"]


