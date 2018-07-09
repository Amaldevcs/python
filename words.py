
import sys
word=[]
fin =open("q1.txt")
for line in  fin :
 w = line.strip()
 word.append(w)
end = len(word)-1
while end !=0:
 for i in range (end):
  if word[i] > word[i+1]:
    word[i],word[i+1]=word[i+1],word[i]
 end=end-1 
print word

 


 


  



