osszeg=int(input("Összeg="))
kamat=int(input("Kamat="))
ev=int(input("Év="))

for i in range(ev):
    osszeg= osszeg+ osszeg*kamat/100

print(ev, " múlva ", osszeg, "forintod lesz a számládon")