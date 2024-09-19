x = 1
multiplier = 0
for i in range(1000000):
    multiplier += 1 / x - 1 / ( x + 2 )
    x += 4
print ( 4 * multiplier)