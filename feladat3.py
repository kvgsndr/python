# Kérjünk be a felhasználótól két számot,
#  tároljuk őket egy-egy változóban!
#  a. Adjuk össze őket, és írjuk ki az eredményt!
#  b. Írjuk ki az eredmény elé, hogy „Az összegük:”!
#  c.Írjuk ki magukat a számokat is! 
#  Ha például 2-t és 3-at adott meg a felhasználó, 
#  akkor a kimenet legyen ilyen: 2 és 3 összege: 5
szam1= float( input("Írj be az első számot: "))
szam2= float( input("Írj be a második számot: "))
eredmény=szam1+szam2
print(eredmény)
print("Az összegük:", eredmény)
print(szam1,"és",szam2,"összege:",eredmény)
