# 9d 9c
import random
gondolt_szám= random.randint(1,100)
tippek_szama=0
tipp=int( input('Gondoltam egy számra.Tippeld meg!'))
while tipp!=gondolt_szám:
    if tipp>gondolt_szám:
        print('A szám kisebb!')
    elif tipp<gondolt_szám:
        print('A szám nagyobb!)')
    tippek_szama+=1
    tipp=input('Tippeld meg!')
    tipp=int(tipp)      
print('Eltaláltad', tippek_szama, ". tipp !")