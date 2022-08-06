#Guess a number between 1 to 9 given by the user. Hint. Random
import random
guessedNumber="" #initialize guessedNumber
randomNumber=random.randint(1, 10)
while randomNumber!=guessedNumber:
    guessedNumber=int(input("Guess a number between 1 and 10 until you get it right: "))
print("you guessed correct!")
