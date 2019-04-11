import chapter4 as c

if __name__=='__main__' : 
	import turtle
	import doctest
	window=turtle.Screen() 
	window.bgcolor("lightgreen")
	tess=turtle.Turtle()
	c.draw_five_stars(tess)
	doctest.testmod(verbose=True)
