# du1 Jachym Cernik SGG Piskvorky 
import turtle
import random
from turtle import forward,right,exitonclick, left, pendown, penup, speed, hideturtle, backward
from math import sqrt 
a = int(input("vyber pocet radku")) # delka radku
b = int(input("vyber pocet sloupcu")) # vyska pole

strana = 50 # strana sestiuhelniku
screen = turtle.Screen()
screen.setup(800,800)

penup()
turtle.setposition(100,-100) # posunuti trochu do praveho dolniho rohu aby bylo pole vice ve stredu screenu 
pendown()
speed(0)


# funkce pro kresleni pole 
def climbHexRight(): # brusleni po stranach sestiuhelniku do prava 
    forward(strana)
    right(60)
    forward(strana)
    right(60)


def preRowPosition(): # vrati zelvu na zacatek sloupce aby se stejna funkce znovu exekuovat 
    penup()
    for i in range (2):
        forward (strana)
        right(60)
    right(120)
    pendown()

def backToStart(): # zelva odejde zpet na start kde zacal radek 
    left(240)
    for y in range(a):
        forward(strana)
        left(60)
        forward(strana)
        right(60)

def drawHex(): # nakresli sestiuhelnik
    for i in range (6):
        forward (strana)
        left(60)
    left(120)

def drawRow(): # nakresli radek a = pocet hexagonu do sirky pole
    for x in range(a):
        drawHex()
        penup()
        climbHexRight()
        pendown()

#####################################################################
# funkce na hru 
def drawX(): # dovede zelvu na stred sestiuhelniku, nakresli krizek , vrati zelvu domu na start
    left(180)
    forward(strana)
    pendown()
    turtle.color("blue")
    right(45)
    turtle.backward(strana/2)
    turtle.forward(strana)
    turtle.backward(strana/2)
    right(90)
    forward(strana/2)
    turtle.backward(strana)
    turtle.setheading(0)
    penup()
    turtle.goto(home_Base_position)
def drawCircle(): # dovede zelvu na stred sestiuhelniku, nakresli kolecko, vrati zelvu domu na start
    left(180)
    forward(strana)
    turtle.penup()
    right(90) 
    forward(25)
    left(90)
    turtle.pendown()
    turtle.color("red")
    turtle.circle(25,360,50)
    turtle.setheading(0)
    penup()
    turtle.goto(home_Base_position)
def rowchooser(): # dovede zelvu na souradnice, pocet se urcuje v column, Osa X 
    left(120)
    forward(strana)
    right(60)
    forward(strana)
    right(60)
def columnchooser(): # dovede zelvu na souradnice, pocet se urcuje v column, osa Y
    forward(50)
    left(60)
    forward(50)
    right(60)
stopper = b # stopuje preRowPostiton 
for w in range(b): # vytvori pole b = pocet sestiuhelniku do vysky 
    drawRow()
    backToStart()
    if stopper > 1: # aby ke konci malovani zelva nesla mimo pole 
        preRowPosition()
    stopper -=1 

penup()
# konec malovani site 
left(120) # nakoleni zelvu tak aby se s ni lepe operovalu pri hrani, smer na prvou stranu screenu 
home_Base_position = turtle.position() # zaznamena startovni pozici pro zelvu, od ktere se bude startovat pri hre 
speed(0)
n=0 # variable na inniciaci cyklu a rozhodnuti kdo hraje, 
# za kazdym tahem se pricte n +1, az se vyplni vsechni mozna policka tak se cykul zastavi 
while n<(a*b):
    m=n/2
    if n//2==m: # zajisti kazde kolo stridani hracu jelikoz se na konci cyklu pricita n + 1 
        print("hraje kolečko")
    else:
        print("hraje křížek")
    row = int(input("vyber řádek (1 až {}) - ".format(a))) # input a zadavání sousřadnic
    column = int(input("vyber sloupec (1 až {}) - ".format(b)))
    if row > b or row < 0 or column > a or column < 0: # zajisti ze player nemuze dat input mimo rozmezi hriste 
        print("souradnice jsou mimo hraci plochu, hraj znova")
        row = int(input("vyber řádek (1 až {}) - ".format(a)))
        column = int(input("vyber sloupec (1 až {}) - ".format(b)))   
    for distance in range(column): 
        columnchooser()
    if row != 1: # zajisti ze zelva nepujde v pripade rozhodnuti pro prvni radek a timpadem se vubec funkce pro lezeni na ose Y vubec neodehraje 
        for distance in range(row-1):
            rowchooser()
    if n//2 == m:  # k
        drawCircle()
    else:
        drawX()
    n += 1
exitonclick()