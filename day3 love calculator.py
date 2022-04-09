# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lname1 = name1.lower()
lname2 = name2.lower()

ct_name1 = lname1.count('t') + lname1.count('r') + lname1.count('u') + lname1.count('e')
ct_name2 = lname2.count('t') + lname2.count('r') + lname2.count('u') + lname2.count('e')

cl_name1 = lname1.count('l') + lname1.count('o') + lname1.count('v') + lname1.count('e')
cl_name2 = lname2.count('l') + lname2.count('o') + lname2.count('v') + lname2.count('e')

true_count = ct_name1 + ct_name2
love_count = cl_name1 + cl_name2

score = int(str(true_count) + str(love_count))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


