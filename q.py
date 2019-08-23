import turtle
def DesenhaQuadrado(tart,lado):
tart = turtle.Turtle
tart.forward(lado)
tart.left(90)
tart.forward(lado)
tart.left(90)
tart.forward(lado)
tart.left(90)
tart.forward(lado)
tart.left(90)
return
def DeslocaDireita(tart,dist):
"""Desloca distância p/direita"""
tart.up()
tart.fd(dist)
tart.down()
return
tart = turtle.Turtle()
DesenhaQuadrado(tart,100)
DeslocaDireita(tart,100)
DesenhaQuadrado(tart,50)
DeslocaDireita(tart,50)
DesenhaQuadrado(tart,25)
