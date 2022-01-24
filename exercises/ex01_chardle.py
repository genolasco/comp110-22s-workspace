"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730411655"

five_chr_word: str = input("Enter a 5-character word:")
if len(five_chr_word) < (5):
    print("Error: Word must contain 5 characters")
    exit()
if len(five_chr_word) > (5):
    print("Error: Word must contain 5 characters")
    exit()
single_chr: str = input("Enter a single character:")
if len(single_chr) > (1):
    print("Error: Character must be a single character.")
    exit()
if len(single_chr) == (0):
    print("Error: Character must be a single character.")
    exit()
number_matching_chr: int = 0
print("Searching for " + single_chr + " in " + five_chr_word + ".")
if single_chr == five_chr_word[0]:
    print("" + single_chr + " found at index 0")
    number_matching_chr = number_matching_chr + 1
if single_chr == five_chr_word[1]: 
    print("" + single_chr + " found at index 1")
    number_matching_chr = number_matching_chr + 1
if single_chr == five_chr_word[2]:
    print("" + single_chr + " found at index 2") 
    number_matching_chr = number_matching_chr + 1
if single_chr == five_chr_word[3]:
    print("" + single_chr + " found at index 3")
    number_matching_chr = number_matching_chr + 1
if single_chr == five_chr_word[4]:
    print("" + single_chr + " is found at index 4")
    number_matching_chr = number_matching_chr + 1
print(str(number_matching_chr) + " instances of " + single_chr + " found in " + five_chr_word)
