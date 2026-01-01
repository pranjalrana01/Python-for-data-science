import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("welcome to the password guessing game")
print("choose a difficulty level: easy, medium or hard")

level = input('Enter the difficulty: ').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice.Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations!! you guessed it in {attempts} attempts.')
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] ==secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    
    print("hint: ", hint)
print("Game Over")