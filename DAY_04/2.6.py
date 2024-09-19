n = int(input("Input an integer: "))
for i in range(2,(n//2)+1):
    #for j in range(i,n,i):
    for j in range(n-i,i+1,-i):
        print(j, end=" ")