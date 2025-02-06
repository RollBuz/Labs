import random
guess_num = random.randint(1,20)
name = input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
index = 0
while True:
    a = int(input("Take a guess."))
    index += 1
    if a == guess_num:
        print(f"Good job, {name}! You guessed my number in {index} guesses!")
        break
    elif a < guess_num:
        print("Your guess is too low.")
        continue
    elif a > guess_num:
        print("Your guess is too high.")
        continue