import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """   ____                                                       _               
  / ___|_   _  ___  ___ ___     __ _    _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   / _` |  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \  | (_| |  | | | | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/   \__,_|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  """
# Functions
attempts = 11


def guess_number(diff):
    global attempts, number
    number = random.randint(1, 100)
    if diff == "hard":
        attempts -= 5
    guessing()


def guessing():
    global guessed_number, attempts, number_status
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Guess a number: "))
    number_status = number_checker(number)


def number_checker(num):
    if num > guessed_number:
        return "low"
    if num < guessed_number:
        return "high"
    if num == guessed_number:
        return "win"


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess_number(difficulty.lower())
end_of_number_guessing = False


while not end_of_number_guessing:
    if number_status == "low":
        print(f"Too low.")
        print("Guess again.")
        guessing()
    elif number_status == "high":
        print("Too high.")
        print("Guess again.")
        guessing()
    elif number_status == "win":
        print(f"You got it! The answer was {number}")
        end_of_number_guessing = True
        exit()
    if attempts == 1:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {number}")
        end_of_number_guessing = True
        exit()

