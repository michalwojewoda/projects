import random

# user guessing

def guess():
    print("Welcome to the guessing game. First you will have to decide range of random number")
    x = int(input("Please type the max range. From 0 to: "))
    print("Got it, lets start the game! \n")
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number beetween 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again, too low")
        elif guess > random_number:
            print("Sorruy, guess again, too High")
    print(f"Yay, congrats. You have guessed the number. It was {random_number} all along")

#computer guessing

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (h), too low (L), or correct(C)?').lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
    print(f"Yay! Computer guessed number, {guess}, correctly!")


computer_guess(1000)