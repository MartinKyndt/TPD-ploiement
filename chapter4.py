# -*- coding: utf-8 -*-
"""Ce code permet de dessiner des étoiles en utilisant l'outil graphique turtle
"""

import doctest
import turtle 

def draw_stars(animal,size):
	"""Cette fonction permet de dessiner une étoile via le module turtle de python.

	Parameters 
	----------
	animal : turtle 
		l'objet de type turtle
	size : int 
		la taille des côtés de l'étoile

	Returns 
	-------
	Ne retourne rien
	"""
	for _ in range(5):	
		animal.forward(size)
		animal.right(144)

def draw_five_stars (animal) : 
	"""Cette fonction permet de dessiner cinq étoiles grâce à la fonction précédente.

	Parameters 
	----------
	animal : turtle 
		l'objet de type turtle

	Returns 
	-------
	som : int 
		la somme des angles dont la tortue a tourné 
		
		.. math:: \sum angle
	
	Examples 
	--------
	>>> draw_five_stars()
	720
	"""
	som=0
	for _ in range(5) :
		draw_stars(animal,100)
		animal.penup()
		animal.forward(350)
		animal.right(144)
		som+=144
		animal.pendown()
	return som





