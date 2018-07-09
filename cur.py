import requests,json
print "use USD-->for DOller,INR-->Indian rUpee,EUR--> Euro"
api_key = "a9da6bd7112437cbe655914c40024b97"
url = "http://data.fixer.io/api/latest?access_key="+api_key+"&base = USD&symbols ="+ "EUR,IND,AUD,CAD,PLN,MXN"
r = requests.get(url)
d = r.json()
c= d["rates"]
fro = raw_input("enter the from currency")
to = raw_input("enter the to currency")
amount = raw_input("enter the from amont")
base = "EUR"
if fro==base:
 result =  float(c[to])*float(amount)
 print "the converted amount is:",result
else:
 x = float(1/c[fro])
 y =  float(x*float(amount))
 z = y*c[to]
 print "the converted amount is :",z
