"""Wordle Game With Functions."""

__author__ = "730411655"


def contains_char(any_length: str, single_chr: str) -> bool:
    """Searches for a single chr and specifc chr string."""
    assert len(single_chr) == 1
    equal: bool = False
    i: int = 0
    # i is counting each character to check each chr in the word you guess
    while equal is False and i < len(any_length):
        if any_length[i] == single_chr:
            equal = True
        else:
            i += 1
            # you add to continue the loop until the counter is greater then the actual length
    if equal is True:
        return True
    else:
        return False
  

def emojified(guess: str, secret_word: str) -> str:
    """Testing two strings for correct colored boxs."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    while i < len(secret_word):
        if guess[i] == secret_word[i]:
            emoji += GREEN_BOX
            i += 1
        elif contains_char(secret_word, guess[i]) is True:
            emoji += YELLOW_BOX
            i += 1
        else:
            emoji += WHITE_BOX
            i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Tests for the expected word length."""
    word = input(f"Enter a {expected_length} character word: ")
    while len(word) != (expected_length):
        word = input(f"That wasn't {expected_length} chars! Try again: ")
        # checks the length with the givin input you give it
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    won: bool = False
   
    while turn <= (6) and not won:
        print(f"=== Turn {turn}/6 ===")
        turn += 1
        correct_guess: str = input_guess(len(secret_word)) 
        emoji: str = emojified(correct_guess, secret_word)
        print(emoji) 
        if correct_guess == secret_word:
            won = True
            turn -= 1
            print(f"You won in {turn}/6 turns! ")
    if turn > (6):
        print("X/6 - Sorry, try again tomorrow!")
        # wordle only has 6 max tries so one i > 6 the games has to end


if __name__ == "__main__":
    main()