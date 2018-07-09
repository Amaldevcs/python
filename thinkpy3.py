def histo(t):
    d = {}
    for i in t:
        if i not in d:
          d[i] = 1
        else:
          d[i] = d[i] + 1
    print d
    t = []
    for key,value in d.items():
        t.append((value,key))
    print t
    t.sort(reverse=True)
    print t
print "enter the word pls"
histo(raw_input())
