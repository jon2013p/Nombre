import turtle
import tkinter
import pygame
import time

t=turtle.Pen()

def estrellapar(tamano,n):
	for i in range(n):
		t.forward(tamano)
		t.left(angulo)

tamano=int(input("Ingrese el tamaño para la estrella"))
n=int(input("ingrese un numero par"))

angulo = (-360/n)+180

estrellapar(tamano,n)