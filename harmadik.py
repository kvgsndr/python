# Slicing - "darabolás?" A stringeket mint egy tömböt is felfoghatjuk, ez a technika érvényes az (indexelhető) lista-szerű objektumokra is, lásd később.

# szoveg = D  a  r  a  b  o  l  á  s  !
#          0  1  2  3  4  5  6  7  8  9
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

szoveg = "Darabolás!"
# szöveg[mettől:meddig:lépésköz]
# visszafelé -1-től ameddig csak tart, -1-es lépésközzel
print(szoveg[-10::1])
print(szoveg[-1::-1])
print(szoveg[-1:-4:-1])
print(szoveg[1:6:2])
print(szoveg[1:])
print(szoveg[2:5])

szoveg = "Indul a görög aludni"
print(szoveg.replace(" ", ""))
print(szoveg)
print(szoveg[::-1])
#2 db ö betű van benne
print(szoveg.count("ö"))
print(szoveg.upper())
print(szoveg.lower())
lista = szoveg.split()
print(lista)
print(lista[2])