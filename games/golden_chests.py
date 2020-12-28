"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku



import random
def game():
    game_lenght = 5

    while game_lenght > 0:
        game_lenght -= 1

        did_i_found_chest = ["Yes", "No"]

        step = random.choices(did_i_found_chest, [90,10])

        if step == "Yes":
            type_of_chest = [
                "green"
                "orange"
                "violet"
                "gold"
            ]
            print(random.choices(type_of_chest, [75,20,4,1], k=1))
        else:
            print("Pokój jest pusty")

print("You enter first room: ", game())



"""

import random
from enum import Enum

def findAppriximateValue(value, perentRange):
    lowestValue = value - (perentRange / 100) * value
    highestValue = value + (perentRange / 100) * value
    return random.randint(lowestValue, highestValue)


Event = Enum("Event", ["Chest", "Empty"])

eventDictionary = {

    Event.Chest: 80,
    Event.Empty: 20
}
eventList = list(eventDictionary.keys())
eventPropability = list(eventDictionary.values())

Colours = Enum("colours", {"Green": "Green",
                           "Orange": "Orange",
                           "Purple": "Violet",
                           "Gold": "Goldish",
                           }
               )

chestColoursDictionary = {
    Colours.Green: 0.75,
    Colours.Orange: 0.2,
    Colours.Purple: 0.04,
    Colours.Gold: 0.01
}
chestColourList = tuple(chestColoursDictionary.keys())
chestColourPropability = tuple(chestColoursDictionary.values())

rewardsForChests = {
    chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(chestColourList))

}


gameLenght = 5
goldAquired = 0

while gameLenght > 0:
    playerAnswer = input("Do you want to visit another room? Type Yes or No ").lower()

    if (playerAnswer == "yes"):
        print("Great, lets see what you got...")
        drawnEvent = random.choices(eventList, eventPropability)[0]
        if (drawnEvent == Event.Chest):
            print("You have found a CHEST!\n")
            drawnColour = random.choices(chestColourList, chestColourPropability)[0]
            print("Chect color is: ", drawnColour.value)
            gamerReward = findAppriximateValue(rewardsForChests[drawnColour], 11)
            goldAquired = goldAquired + gamerReward
            print("You have found", gamerReward, "gold.\n" )
        elif (drawnEvent == Event.Empty):
            print("Your have found Jack!")

    else:
        print("You have to play, there is really no other option  ;]")
        continue

    gameLenght -= 1

print("\nCongrats you have aquired", goldAquired, "of pure gold.")
