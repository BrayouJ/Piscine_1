liste = [1,2,3,4,5]
#print(liste[0])
#print(liste[-1])
liste.append(6)
#print(liste)
liste.remove(liste[-1])
#print(liste)
liste.insert(0,0)
#print(liste)
#print(liste[1:6])
liste2 = []
for i in liste:
    liste2.append(liste[-i-1])
#print(liste2)
#print(liste[0],liste2[0])
for i in range(17):
    liste.append(i+6)
print(liste)

#liste.extend(liste2)
#print(liste)

#.extend extends the first list by adding the second at the end.
#The second list remains unchanged.

#liste = [*liste,*liste2]
#print(liste)

#same as .extend