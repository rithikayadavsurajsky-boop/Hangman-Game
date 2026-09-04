import random

words = ["apple", "python", "computer", "coding", "school"]

word = random.choice(words)
chances = 3

print("Welcome to Hangman!")
print("Guess the word!")
print("_ " * len(word))

while chances > 0:

    guess = input("Enter the word: ").lower()

    if guess == word:
        print("Correct! You won!")
        print("The word was:", word)
        break
    else:
        chances -= 1
        print("Wrong guess!")
        print("Chances left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)
