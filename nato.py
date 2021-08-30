# TODO - Create a program that takes in a name from a user and outputs the corresponding names in the nato alphabet

# Import the data
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1- Change the data into a dictionary with key value pairs

new_df = {row.letter:row.code for (index, row) in data.iterrows()}
# print(new_df)

name = input("Please input the name. ").upper()
nato_name = [new_df[letter] for letter in name]
print(nato_name)
