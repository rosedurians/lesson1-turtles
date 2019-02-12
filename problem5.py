from turtle import * 

screen = Screen()
screen.bgcolor("black")

john = Turtle()
cena = Turtle()

john.color("white")
john.pensize(6)
john.speed(9)
john.shape("turtle")


cena.color("white")
cena.pensize(6)
cena.speed(9)
cena.shape("turtle")




for x in range(3):
	john.forward(100)
	john.left(120)

	

for x in range(4):
	cena.forward(100)
	cena.left(90)




mainloop()
