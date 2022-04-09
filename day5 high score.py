# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
num_of_scores = len(student_scores)
highest_score = 0
for x in range(0, num_of_scores):
    if student_scores[x] > highest_score:
        highest_score = student_scores[x]

print("The highest score in the class is: ", highest_score)
