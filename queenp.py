def printbo(partial):
    size = 8
    for digit in partial:
        col = int(digit)
        lin = '.'*(col -1)+"q"+\
               '.'*(size-col)
        print lin

printbo("36428571")
