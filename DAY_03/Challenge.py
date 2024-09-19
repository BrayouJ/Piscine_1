text = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
x = text.lower()
y = text.lower()
z = 0
for i in range(2):
    if i > 0:
        y = y[::-1]
    for i in range(len(x)):
        if x[i] == "c":
            if x[i+1] == "a" and x[i+2] == "t":
                z += 1
                print(z)
        if x[i] == "g":
            if x[i+1] == "a" and x[i+2] == "r" and x[i+3] == "d" and x[i+4] == "e" and x[i+5] == "n":
                z += 1
                #print(z)
        if x[i] == "m":
            if x[i+1] == "i" and x[i+2] == "c" and x[i+3] == "e":
                z += 1
                #print(z)
print(z)

#incomplete