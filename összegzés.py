# add össze a számokat a felhasználó által megadottig!

szam = int(input("Írj be egy egész számot: "))

osszeg=0
for i in range(1,szam+1):   # 1 2 3 4 5 6 ... szam
    osszeg+=i               # osszeg= 1+2+3+4+5+6+...+szam

print("Az első", szam, "szám összege=", osszeg)