from __future__ import print_function, division

import turtle

from polygon import arc


def petal(t, r, angle):
    """Rysuje płatek za pomocą dwóch łuków.

    t: obiekt żółwia
    r: promień łuków
    angle: kąt (w stopniach) odpowiadający łukom
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Rysuje kwiatek za pomocą n płatków.

    t: obiekt żółwia
    n: liczba płatków
    r: promień łuków
    angle: kąt (w stopniach) odpowiadający łukom
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Przemieszcza obiekt żółwia (t) do przodu o (length) jednostek bez pozostawiania śladu.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# rysowanie sekwencji trzech kwiatów w sposób pokazany w książce.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()
