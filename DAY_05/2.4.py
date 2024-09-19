liste = [6,8,10,2,4]
liste.sort()
print(liste[0],liste[-1])
for i in liste:
    if i<7:
        print(i, end=" ")
liste.sort(reverse=True)
print(liste)