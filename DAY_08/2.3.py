import turtle as t

def draw_polygon(sides):
    
    for i in range(sides):
        t.fd(100)
        t.rt(360//sides)

x = int(input("Number of sides?: "))
draw_polygon(x)

t.mainloop()
