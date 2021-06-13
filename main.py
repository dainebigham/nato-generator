import pandas as pd

# open the nato-phonetic csv file as a data fram
nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

# grab the data out of the dataframe and create a dictionory with the alphabet letter
# as the key, and the nato-phonetic code as the value using dict comprehension
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# get the user input and make sure it is upper case
word = input("Enter a word: ").upper()

# for each letter in the users word, look up that letter in the nato-phonetic alphabet
# dict, grab the value, and add it to the nato list using list comprehension
nato = [nato_dict[letter] for letter in word]

print(nato)
