from turtle import * 

john = Turtle()

john.color("red")
john.pensize(6)
john.speed(9)
john.shape("turtle")


for x in range(6):
	john.forward(100)
	john.left(60)

mainloop()
