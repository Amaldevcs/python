import string
wordlist = []
fin = open(raw_input("file pls  "))
for words in fin:
    word = words.strip()
    wordlist.append(word)
p = list(string.punctuation)
a = []
for i in  wordlist:
  r =list(i)  
  for e in r:
    if e in p:
      r.remove(e)
    if e== "\n":
      r.remove("\n")
  print 
  for s in range (len(r)):
    print r[s],
     


