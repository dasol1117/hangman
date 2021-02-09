# 행맨 게임

import random
words = ["apple","coffee","guitar","harmony","programmers","spaghetti"]
question =  random.choice(words)

letters = ""

print("-"*50)
print("Welcome To Hangman Game")
print("-"*50)
life = len(questions) + 2
while True:
    answer = True
    for w in question:
        if w in letters: print(w, end="")
        else:
            print("_", end=" ")
            answer = False
    print()

    if answer:
        print("^^ Congraulations!!")
        break
    if life == 0:
        print("--; You Died")
        break

    letter = input("Guess a letter: ")
    if letter not in letters: letters += letter
    if letter in question: print("YES")
    else:
        life -= 1
        print(f"NO! Your life {life}")
    print()

print("-"*50)
print("Goodbye")
print("-"*50)
