#Write your code below this line 👇
from unittest import skip


def prime_checker(number):
    prime_flag = 'y'
    for x in range(1, number + 1):
        if number % x == 0:
            if x == 1 or x == number:
                continue
            else:
                x = number
                prime_flag = 'n'
                break    

    if prime_flag == 'y':
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



