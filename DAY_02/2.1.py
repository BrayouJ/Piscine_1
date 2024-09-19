liste = []
liste2 = []
result = 0
x = 0
z = int(input("Nombre de 1? "))
while x <= z - 1:
    liste.append( 1 * 10**x )
    x += 1
    y = sum(liste)
    liste2.append(y)
for element in liste2:
    result += element
print (result)
a = int(input("Puissance? "))
print (result**a)