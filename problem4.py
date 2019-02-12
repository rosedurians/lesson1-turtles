from turtle import * 

john = Turtle()
cena = Turtle()


john.color("blue")
john.pensize(6)
john.speed(9)
john.shape("turtle")

cena.color("red")
cena.pensize(6)
cena.speed(9)
cena.shape("turtle")



john.circle(99)



cena.color("red")
cena.pensize(8)
cena.speed(10)
cena.shape("turtle")


for x in range(3):
	cena.forward(100)
	cena.left(120)

mainloop()

