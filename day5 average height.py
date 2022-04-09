# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
num1 = 0
total_height = 0

for x in student_heights:
    num1 += 1

for y in range(num1):
    total_height += student_heights[y]

print(round(total_height / num1))

