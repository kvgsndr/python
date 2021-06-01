N=int( input("Mennyi számot szeretnél bevinni?"))
lista=[]
for i in range(N):
    bevitel=input("Vidd be a " + str(i+1) + ". számot: ")
    lista.append( int(bevitel) )

print(lista)
osszeg=0
for i in range( len(lista)) :    # range(N)
    osszeg+=lista[i];

print("Összeg= ", osszeg)
atlag=osszeg/N
print("Átlag= ", atlag)