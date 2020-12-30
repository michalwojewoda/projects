import turtle

# Stworzenie okna gry
wn = turtle.Screen()
wn.title("Pong by Michał Wojewoda")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0) #wyłączenie odświeżania - będziemy odświeżać go ręcznie


# Główna pętla gry

while true:
    wn.update()


#problem z zainstalowaniem turtle
