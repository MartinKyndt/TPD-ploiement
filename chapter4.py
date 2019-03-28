# -*- coding: utf-8 -*-
"""Ce code permet de dessiner des étoiles en utilisant l'outil graphique turtle
"""

import turtle 

def draw_stars(animal,size):
	"""Cette fonction permet de dessiner une étoile via le module turtle de python.

	Parameters 
	----------
	animal : l'objet de type turtle
	size : la taille des côtés de l'étoile

	Returns 
	-------
	Ne retourne rien
	"""
	for _ in range(5):	
		animal.forward(size)
		animal.right(144)

def draw_five_stars () : 
	"""Cette fonction permet de dessiner cinq étoiles grâce à la fonction précédente.

	Parameters 
	----------
	Aucuns

	Returns 
	-------
	Ne retourne rien
	"""
	for _ in range(5) :
		draw_stars(tess,100)
		tess.penup()
		tess.forward(350)
		tess.right(144)
		tess.pendown()


window=turtle.Screen() 
window.bgcolor("lightgreen")
tess=turtle.Turtle()
draw_five_stars()




