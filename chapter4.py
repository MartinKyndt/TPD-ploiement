import math 
import turtle 
window=turtle.Screen() 
window.bgcolor("lightgreen")
tess=turtle.Turtle()

def draw_poly(t,n,sz):
	for _ in range(n):
		t.forward(sz)
		tess.right(360/n)

def draw_equilateraltriangle(animal, size):
	draw_poly(animal,3,size) 

def draw_stars(animal,size):
	for _ in range(5):	
		animal.forward(size)
		animal.right(144)

for _ in range(5) :
	draw_stars(tess,100)
	tess.penup()
	tess.forward(350)
	tess.right(144)
	tess.pendown()




