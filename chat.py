import requests,json
url = "https://matrix.org/_matrix/client/r0/rooms/!FXclHICUyrLMhiVPYq:matrix.org/send/m.room.message?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDI4Y2lkIHVzZXJfaWQgPSBAYW1hbGRldmNzOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSBRU2MsYU9vMn5LWEw9MnQ3CjAwMmZzaWduYXR1cmUgnufaSzM_y5gwiYnRnuqt2OpTIPaywRDJjJ37rbGJ0zQK"
msg = raw_input("enter the msg:::")
content = {"msgtype":"m.text","body":msg}
data = json.dumps(content)
r = requests.post(url,data=data)
print r.status_code
if r.status_code == 200 :
 print "ok"




