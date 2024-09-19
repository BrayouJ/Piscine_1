x = input("Enter a string: ").lower()
x = x.replace(" ", "")
y = (len(x)) // 2
palindrome = True
for i in range(y):
    if palindrome == True:
        if x[i] != x[len(x)-1-i]:
            palindrome = False
            
if palindrome == True:
    print("Palindrome")
else:
    print("Not a Palindrome")