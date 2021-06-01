kacatok=[]
kacat=input("Írd be a kacat nevét!")

while kacat!="elfogyott":
    kacatok.append(kacat)
    kacat=input("Írd be a kacat nevét!")

kacataim= "Kacataim: " + ", ".join(kacatok)+"."
print(kacataim)

print("Kacataim: ", kacatok)

print("Katacaim: ", end="")
for i in range(len(kacatok)):
    print(kacatok[i], sep=",",end=" "  )
print()
    

