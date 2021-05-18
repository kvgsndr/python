name= input("Írja be a nevét! ")
születési_év=int(  input("Írd be a születési évedet: ")  ) 
print("Üdvözlet,", name, ":)", end=" ") 
éves=2021-születési_év
print("Te", éves, "éves vagy!")
if éves >=18:
    print("Felnőtt!")
else:
    print("Még kiskorú")