import turtle
#imports turtle
toto = turtle.Screen()
toto.bgcolor ("black")
#changes the color of the background to black
titi = turtle.Turtle()
titi.color ("red")
#changes cursor to red
for i in range(3):
    titi.right(90)
    titi.circle(42)
#draws 3 circles
turtle.mainloop()