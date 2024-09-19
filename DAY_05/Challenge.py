import random
import time

liste=[]
for i in range(1000000):
    liste.append(random.randint(0,10000))

startingTime = time.time()

liste.sort()
print(liste)

duration = time.time()- startingTime

print(duration)