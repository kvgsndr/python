szoveg = "indul a görög aludni"
print(szoveg)
szoveg = szoveg.replace(" ", "")
print(szoveg)
mirror = szoveg[::-1]
print(szoveg)

if szoveg == mirror:
    print("palindrom")
    print("*********")
    print(szoveg)
else:
    print("NEM palindrom")
    print("-------------")
