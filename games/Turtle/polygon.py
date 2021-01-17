from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Rysuje kwadrat z bokami o podanej długości.

    Zwraca obiekt Turtle do początkowej pozycji i położenia.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Rysuje n odcinków liniowych.

    t: obiekt Turtle
    n: liczba odcinków liniowych
    length: długość każdego odcinka
    angle: stopnie między odcinkami
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Rysuje wielokąt o n bokach.

    t: obiekt Turtle
    n: liczba boków
    length: długość każdego boku.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Rysuje łuk o danym promieniu i kącie.

    t: obiekt Turtle
    r: promień
    angle: kąt odpowiadający łukowi (w stopniach)
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # wykonanie niewielkiego obrotu w lewo, zanim uruchomienie
    # zmniejszy błąd spowodowany liniową aproksymacją łuku
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Rysuje koło o danym promieniu.

    t: obiekt Turtle
    r: promień
    """
    arc(t, r, 360)


# Następujący warunek sprawdza, czy uruchomiono skrypt, a
# jeśli tak, uruchamiany jest kod testu, czy ma miejsce importowanie 
# (kod testu nie jest wykonywany).

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

"""
if __name__ == '__main__':
    bob = turtle.Turtle()

    # rysuje koło o środku w punkcie początkowym
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # oczekiwanie na zamknięcie okna przez użytkownika
    turtle.mainloop()
"""