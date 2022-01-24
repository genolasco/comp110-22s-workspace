"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730411655"

five_chr_word: str = input("Enter a 5-character word: ")
if len(five_chr_word) < (5):
    print("Error: Word must contain 5 characters")
    exit()
if len(five_chr_word) > (5):
    print("Error: Word must contain 5 characters")
    exit()
single_chr: str = input("Enter a single character: ")
if len(single_chr) > (1):
    print("Error: Character must be a single character.")
    exit()
if len(single_chr) == (0):
    print("Error: Character must be a single character.")
    exit()
count_instance: int = 0
print("Searching for " + single_chr + " in " + five_chr_word)
if single_chr == five_chr_word[0]:
    print("" + single_chr + " found at index 0")
    count_instance = count_instance + 1
if single_chr == five_chr_word[1]: 
    print("" + single_chr + " found at index 1")
    count_instance = count_instance + 1
if single_chr == five_chr_word[2]:
    print("" + single_chr + " found at index 2") 
    count_instance = count_instance + 1
if single_chr == five_chr_word[3]:
    print("" + single_chr + " found at index 3")
    count_instance = count_instance + 1
if single_chr == five_chr_word[4]:
    print("" + single_chr + " found at index 4")
    count_instance = count_instance + 1

if count_instance > (1):
    print(str(count_instance) + " instances of " + single_chr + " found in " + five_chr_word)
if count_instance == (1):
    print(str(count_instance) + " instance of " + single_chr + " found in " + five_chr_word)
else:
    print("No instances of " + single_chr + " found in " + five_chr_word)