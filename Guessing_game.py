import random
a = random.randint(1, 9)

while True:
    guess = input("Guess the number between 1 and 9 inclusive: ")
    if int(guess) < int(a):
        print("too low")
        continue
    elif int(guess) > int(a):
        print("too high")
        continue
    else:
        int(guess) == int(a)
        print("Bang on!")
    more = input("Do you want to play again? y/n ")
    if more == "y":
        a = random.randint(1, 9)
    elif more == "n":
        break



