import random

lowest_num = 0
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runnning = True

print("number guessing game")
print(f"select the number between {lowest_num} and {highest_num}")

while is_runnning:
    guess = input("enter ur guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("that numb is out of range")
            print(f"please select the number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("too low, try again")
        elif guess > answer:
            print("too high, try again")
        else:
            print(f"CORRECT!, the answer was: {answer}")
            print(f"number of guesses: {guesses}")
            is_runnning = False

    else:
        print("Invalid guess")
        print(f"please select the number between {lowest_num} and {highest_num}")

