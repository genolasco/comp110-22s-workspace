"""Another step toward Wordle Exercise."""

__author__ = "730411655"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word = str("python")

i: int = 0
emoji: str = ""
guess: str = input("What is your 6-letter guess? ")

while len(guess) < (6):
    print("That was not 6 letters! Try again: ")
    while len(guess) > (6):
        print("That was not 6 letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        emoji += GREEN_BOX
    else:
        exist: bool = False 
        double_check: int = 0
        while not exist and double_check < len(secret_word): 
            if guess[i] == secret_word[double_check]:
                exist = True
            else: 
                double_check += 1
        if exist:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1
print(emoji)
