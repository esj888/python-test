# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import fileinput

letter_template = []


def load_letter():
    letter = letter_file.readline()

    while letter:
        letter_template.append(letter)
        letter = letter_file.readline()


def print_letter(print_name):
    print_file = open(f"./Output/ReadyToSend/letter_for_{print_name}.txt", "x")

    for line in letter_template:
        person = line.replace("[name]", print_name)
        print_file.write(person)

    print_file.close()


def process_invites():
    name = names_file.readline()

    while name:
        print_letter(name.strip())
        name = names_file.readline()


letter_file = open("./Input/Letters/starting_letter.txt")
names_file = open("./Input/Names/invited_names.txt")

load_letter()
process_invites()

letter_file.close()
names_file.close()






