# du1 Jachym Cernik SGG Piskvorky 
import turtle
import random
from turtle import forward,right,exitonclick, left, pendown, penup, speed, hideturtle, backward
from math import sqrt 
pocet_radku = int(input("vyber pocet radku ")) 
pocet_sloupcu = int(input("vyber pocet sloupcu ")) 
while pocet_radku < 3 or pocet_sloupcu < 3: # kontroluje chybny pocet radku nebo sloupcu 
    print("3x3 je minimalni velikost, zadejte novou velikost pole")
    pocet_radku = int(input("vyber pocet radku ")) 
    pocet_sloupcu = int(input("vyber pocet sloupcu "))

strana = 50 # strana sestiuhelniku
screen = turtle.Screen()
screen.setup(800,800)

penup()
turtle.setposition(100,-100) # posunuti trochu do praveho dolniho rohu aby bylo pole vice ve stredu screenu 
pendown()
speed(0)

# funkce pro kresleni pole 
def climbHexRight(): #  
    forward(strana)
    right(60)
    forward(strana)
    right(60)
'''
brusleni po stranach sestiuhelniku do prava
'''

def preRowPosition(): 
    penup()
    for i in range (2):
        forward (strana)
        right(60)
    right(120)
    pendown()
'''
vrati zelvu na zacatek sloupce aby se stejna funkce znovu exekuovat
'''

def backToStart(m):
    left(240)
    for y in range(m):
        forward(strana)
        left(60)
        forward(strana)
        right(60)
'''
 zelva odejde zpet na start kde zacal radek 
'''

def drawHex(): 
    for i in range (6):
        forward (strana)
        left(60)
    left(120)
'''
nakresli sestiuhelnik
'''

def drawRow(m): 
    for x in range(m):
        drawHex()
        penup()
        climbHexRight()
        pendown()
'''
nakresli radek a = pocet hexagonu do sirky pole
'''

#####################################################################

# funkce na hru 
def drawX(): 
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
'''
dovede zelvu na stred sestiuhelniku, nakresli krizek , vrati zelvu domu na start
'''

def drawCircle(): 
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
'''
dovede zelvu na stred sestiuhelniku, nakresli kolecko, vrati zelvu domu na start

'''

def rowchooser(): 
    left(120)
    forward(strana)
    right(60)
    forward(strana)
    right(60)
'''
dovede zelvu na souradnice, pocet se urcuje v column, Osa X 
'''

def columnchooser(): 
    forward(strana)
    left(60)
    forward(strana)
    right(60)
'''
dovede zelvu na souradnice, pocet se urcuje v column, osa Y
'''

stopper = pocet_sloupcu # stopuje preRowPostiton 
for w in range(pocet_sloupcu): # vytvori pole b = pocet sestiuhelniku do vysky 
    drawRow(pocet_radku)
    backToStart(pocet_radku)
    if stopper > 1: # aby ke konci malovani zelva nesla mimo pole 
        preRowPosition()
    stopper -=1 

penup()
# konec malovani site 
left(120) # nakoleni zelvu tak aby se s ni lepe operovalu pri hrani, smer na prvou stranu screenu 
home_Base_position = turtle.position() # zaznamena startovni pozici pro zelvu, od ktere se bude startovat pri hre 
speed(0)
pocitacka=0 # variable na inniciaci cyklu a rozhodnuti kdo hraje, 
# za kazdym tahem se pricte n +1, az se vyplni vsechni mozna policka tak se cykul zastavi 

while pocitacka<(pocet_radku*pocet_sloupcu):
    if pocitacka%2==0: # zajisti kazde kolo stridani hracu jelikoz se na konci cyklu pricita n + 1 
        print("hraje křížek")
    else:
        print("hraje kolečko")
    row = int(input("vyber řádek (1 až {}) - ".format(pocet_radku))) # input a zadavání sousřadnic
    column = int(input("vyber sloupec (1 až {}) - ".format(pocet_sloupcu)))
    while row < 1 or column < 1: # kontroluje ze neni zadana chybna souradnice 
        print("souradnice nemohou byt mensi nez jedna, zvolte nove souradnice")
        row = int(input("vyber řádek (1 až {}) - ".format(pocet_radku)))
        column = int(input("vyber sloupec (1 až {}) - ".format(pocet_sloupcu)))
    while row > pocet_radku or row < 1 or column > pocet_sloupcu or column < 1: # zajisti ze player nemuze dat input mimo rozmezi hriste 
        print("souradnice jsou mimo hraci plochu, hraj znova")
        row = int(input("vyber řádek (1 až {}) - ".format(pocet_radku)))
        column = int(input("vyber sloupec (1 až {}) - ".format(pocet_sloupcu)))
        while row < 1 or column < 1:
            print("souradnice nemohou byt mensi nez jedna, zvolte nove souradnice")
            row = int(input("vyber řádek (1 až {}) - ".format(pocet_radku)))
            column = int(input("vyber sloupec (1 až {}) - ".format(pocet_sloupcu)))
    for distance in range(column): 
        columnchooser()
    if row != 1: # zajisti ze zelva nepujde v pripade rozhodnuti pro prvni radek a timpadem se vubec funkce pro lezeni na ose Y vubec neodehraje 
        for distance in range(row-1):
            rowchooser()
    if pocitacka%2==0:
        drawX()
    else:
        drawCircle()
    pocitacka += 1
exitonclick()
