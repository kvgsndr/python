# 9c 9d
# Egyszerű matematikai műveletek
a = 2
b = 3

c = a+b
print ('Összeg=',c)

print ('\nÖsszeadás 2+3 = {}'.format(a+b)) # addition of numbers

print ('\n***Összeadás {}+{} = {}'.format(a,b,a+b)) # addition of numbers

print ('\n===Összeadás ',a,"+",b, "=", a+b) # addition of numbers
print (f'\n===Összeadás {a}+{b}={a+b}')
a = 2.2
b = 1

print ('\nÖsszeadás 2.2+1 = {}'.format(a+b)) # addition of float and number. The result is float

x = a+b
print(f"x tipusa {type(x)}")



a = 2
b = 5

print ('\nDivision  5/2= {}'.format(b/a)) # Divisions of two numbers
print ('\nQuotient  5//2= {}'.format(b//a)) # Getting quotient from division of two numbers
print ('\nRemainder 5 % 2= {}'.format(b%a)) # Getting Remainder from division of two numbers

a = 5
b = 6


print ('\nExponential {}**{}= {}'.format(a,b,a**b)) # Exponential of two numbers


data = 2
data +=3   # Equivalent to data = data + 3
print (data)


first_name = 'Sándor'
print (first_name)
last_name = "Kővágó"
print (last_name)

print ('\n')

long_message = """   This is a long message which will span multiple lines 
by pressing enter.

Line 1  =
Line 2  
                """
print (long_message)

var1 = 'Python Language'
#       012345678901234
#                   -2      
print (var1)

print (var1[0])

print (var1[0:3]) #prints character from position 0 to 2

print('Last Position is',var1[-1])  # last position is -1

print("****")
print (var1[-3:-1]) #prints character from position -3 to last minus 1

print( var1[-3:])

print( var1[:])

str = """Vishal's house is in Mumbai"""
print (str)

str1 = 'This is very \'exciting\' '
str2 = "This is very 'exciting'"
print (str1)
print (str2)

