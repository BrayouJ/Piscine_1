x = 0
y = str()
nombre = str(input("Nombre? "))
for i in nombre:
    if i.isdigit():
        y = y+i
    else:
        break
print (y)

#incomplet