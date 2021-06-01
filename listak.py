lista=[1,2,3,2,5,2]
print(lista)
print("A 2 száma= ",lista.count(2))
lista.reverse()
print(lista)
lista.sort()
print(lista)


""" egyenlő:         ==
nem egyenlő:     !=
kisebb:          <
nagyobb:         >
kisebb egyenlő:  <=
nagyobb egyenlő: >=

Mindig igazzal tér vissza: True
Mindig hamissal tér vissza: False

Logikai operátorok:

ÉS: and
VAGY: or
Negálás: not """

print((5>3)and(3>=2)or(3!=5))

""" print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True" """
print(type(True))
szoveg = "Hello2"
masikszoveg = "Hello2"
print(szoveg is masikszoveg)
print(id(szoveg))
print(id(masikszoveg))


elem = 5
if elem == 1:
    print("valami")
else:
    print("Nem talált!")
