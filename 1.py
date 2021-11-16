
import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']

girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

married_coupls=[]

def search(married_coupls,groom,bride):

    couple=[]

    for x in married_coupls:

        if x[0]==groom:

            return 1

        if x[1]==bride:

            return 1

    else:

        return 0

while True:

    g=random.choice(boys)
    groom=str(g)

    b=random.choice(girls)
    bride=str(b)

    n=search(married_coupls,groom,bride)

    if n==0:

        married_coupls.append((groom,bride))

        if len(married_coupls)==8:
            
            print(married_coupls)
            break