vegetarian = False

def bread () :
    print ("<////////// >")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O ")
def ham () :
    print (" ============ ")

def sandwitch():
    bread()
    tomato()
    ham()
    lettuce()
    ham()
    bread()

def vege():
    bread()
    tomato()
    lettuce()
    tomato()
    lettuce()
    bread()

#1.3
#for i in range(42):
#    sandwitch()

#1.4
def order(y):
    if y >= 0:
        if vegetarian == True:
            for i in range(y):
                vege()
        else:
            for i in range(y):
                sandwitch()
    else:
        print("I can't do this")

x = input("How many sandwitches?: ")

if "veg" in x:
    vegetarian = True

y = 0

for i in x.split():
    if i.isdigit:
        y = y + int(i)

order(y)