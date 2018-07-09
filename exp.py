tuples = [(1,'b'),(1,'d'),(1,'g'),(2,'c')]
#,(2,'f'),(3,'a'),(5,'e')]
def buildtree(tuples):
    while len(tuples)>1:
        least =tuple(tuples[0:2])
        rest = tuples[2:]
        comb = least[0][0]+least[1][0]
        tuples = rest+[(comb,least)]
        tuples.sort()
    return  tuples[0]
tree = buildtree(tuples)
print tree
def trim(tree):
    p = tree[1]
    print type(p)
    print p
    if type(p) == type(""):return p
    else:return (trim(p[0]),trim(p[1]))
print trim(tree)
codes = {}
def assign(node,pat=''):
    global codes
    if type(node) == type(''):
      codes[node] = pat
    else:
        assign(node[0],pat+"0")
        assign(node[1],pat+"1")
assign(trim(tree))
print codes

