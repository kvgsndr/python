# 9c 9d
import random

pontok=0

for i in range(5):
    szam1= random.randint( 1, 10 )
    szam2= random.randint( 1, 10 )
    eredmény=szam1*szam2
    print( szam1, '*', szam2, '=', end="")
    tipp= int( input())
    if eredmény==tipp:
        pontok+=1;    # pontok=pontok+1
        print("OK!")
    else:
        print("Ezt elrontottad!")

print("Pontok: ", pontok)

