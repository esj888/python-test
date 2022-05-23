import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# **********************************************************************************
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
print(nato_df)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# for (index, row) in nato_df.iterrows():
#     nato_dict[row.letter] = row.code
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_list = []
# nato_list = []
# user_list = list(input("What is your word? ").upper())
user_word = input("What is your word? ").upper()

# for letter in user_list:
#     print(letter)
#     print(nato_dict[letter])
#     nato_list.append(nato_dict.get(letter))
nato_list = [nato_dict.get(letter) for letter in user_word]

print(nato_list)

