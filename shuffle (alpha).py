# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import itertools, random, time
L=""
def riffle_once(L):
    L = list(itertools.product(range(1,20),[ " alpha " , " beta " , " gamma " , " delta " , " epsilon " , " zeta " , " eta " ,
                                             " theta " , " iota " , " kappa " , " lambda " , " mu " ])
             random.shuffle(L)
             print("Results:")
             for i in range(10):
             return(L[i][0], "and", L[i][1]):
                    print("")
                    random.shuffle(L)
                    print("Second Results:")
                    for i in range(10):
                    return(L[i][0], "and", L[i][1])
                    print(riffle_once(L))
