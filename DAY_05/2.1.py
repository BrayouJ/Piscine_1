liste = []
for i in range(10):
    liste.append(i+1)
x = 1
for i in liste:
    x = x*liste[i-1]
print(x)