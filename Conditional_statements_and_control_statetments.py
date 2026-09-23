#1)  Write a python program to sum two user input integers. However, if the sum is between x to y it will return True. X and Y is from user.

print("Question number 01")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

x = int(input("Enter X: "))
y = int(input("Enter Y: "))

total = a + b

print("Sum =", total)

if x <= total <= y:
    print(True)
else:
    print(False)


input("\nPress Enter for next question...")


# 2) Write a Program to display smallest number from three input numbers. (Hint: Nested if)

print("Question number 02")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c

print("Smallest number is:", smallest)

input("\nPress Enter for next question...")

#Q.3)Write a proram that accept a lowercase/ uppercase character from the user and check whether character i s a vowel or consonant.


print("Question number 03")
char = input("Enter the character: ").lower()
vowel = ["a", "e", "i", "o", "u"]
if char in vowel:
    print(char, " is vowel")
else:
    print(char, " is consonant")

input("\nPress Enter for next question...")

# 4) Write a Python program to input a number between 1 and 7 and print the day of the week: 1 Sun, 2 Mon, 3 Tue, 4 Wed, 5 Thur, 6 Fri, 7 Sat. It should print 'invalid' if the number does not lie in correct range.

print("Question number 04")
num = int(input("Enter a number between 1 - 7: "))
if num == 1:
    print("sun")
elif num == 2:
    print("Mon")

elif num == 3:
    print('Tue')
elif num == 4:
    print("Wed")
elif num == 5:
    print("Thur")
elif num == 6:
    print("Fri")
elif num == 7:
    print("Sat")

else:
    print("Invalid Choice..!")

input("\nPress Enter for next question...")



#5) Write a Python program to accept three numbers x,y,z from user. The program should check whether x lies between the range specified by other two numbers, i.e. y and z (y<=x<=z)

print("Question number 05")
x = int(input("Enter the valuue of x: "))
y = int(input("Enter the valuue of y: "))
z = int(input("Enter the valuue of z: "))

if (y<= x <= z):
    print(x, "lies between the range.")
else:
    print(x, "not lies between the range.")


input("\nPress Enter for next question...")



#6) Write a program that accept three sides of triangle as input, and print whether the triangle is valid or not.

print("Question number 06")
s1 = int(input("Enter the side s1: "))
s2 = int(input("Enter the side s2: "))
s3 = int(input("Enter the side s3: "))

total = s1 + s2 + s3
if total == 180:
    print("Triangle is valid. ")
else:
    print("Triangle is not valid.")

input("\nPress Enter for next question...")



#7) Write a Python program to check a triangle is equilateral, isosceles or scalene. Hint: Input is the angles of triangles.

print("Question number 07")
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))


if a + b + c == 180:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")

input("\nPress Enter for next question...")



# 8) A bank requires customers to have a minimum salary of Rs.30,000 and at least 2
#years of experience on the job to qualify for a loan. Write a Python program to check
#whether a customer qualifies for loan or not, based on these two parameters.


print("Question number 08")
salary = int(input("Entre the salary: "))
job_exp = int(input("Enter the job expreince: "))

if salary <= 30000 and job_exp <= 2:
    print("Qualified for loan.")
else:
    print("Not qualified for loan.")

input("\nPress Enter for next question...")



# 9) Write a program to input a number x from the keyboard. If the number is larger than 0, find its square root. Otherwise, calculate the square of x.

print("Question number 09")
import math

x = float(input("Enter a number: "))

if x > 0:
    print("Square root =", math.sqrt(x))
else:
    print("Square =", x ** 2)

input("\nPress Enter for next question...")


#10 Write a program to check whether given character is a digit or a character in
#lowercase or uppercase alphabet. Hint: ASCII value of digit is between 48 to 58 and
#Lowercase characters in the range of 97 to122, uppercase is between 65 and 90).

print("Question number 10")
ch = input("Enter a character: ")

ascii_value = ord(ch)

if 48 <= ascii_value <= 57:
    print("Digit")
elif 65 <= ascii_value <= 90:
    print("Uppercase Alphabet")
elif 97 <= ascii_value <= 122:
    print("Lowercase Alphabet")
else:
    print("Special Character")


input("\nPress Enter for next question...")


#11 Write a Python program to find the solution the quadratic equation below: ax^2+ bx + c = 0
print("Question number 11")
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c   
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two distinct real roots:")
    print("x1 =", x1)
    print("x2 =", x2)

elif d == 0:
    x = -b / (2*a)
    print("One repeated real root:")
    print("x =", x)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex roots:")
    print("x1 =", real, "+", imag, "i")
    print("x2 =", real, "-", imag, "i")

input("\nPress Enter for next question...")



#12 The program should print the roots if these are real or equal. It should print 'roots are
#imaginary' otherwise. Input a, b & C from user.
print("Question number 12")
import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b**2 - 4*a*c   
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)

    print("Root 1 =", root1)
    print("Root 2 =", root2)
else:
    print("Roots are imaginary")

input("\nPress Enter for next question...")



# 13) Write a program, which accepts annual basi c salary of an employee and calculates
#and displays the Income tax as per the following rules.
#If Basic is less than Rs. 1,50,000/ 1,50,000/--, then Tax = 0
#If Basic is from Rs. 1,50,000/ to Rs. 3,00,000/ 3,00,000/--, then tax is
#If Basic is greater than Rs. 3,00,000/ 3,00,000/--, th en tax is 30%


print("Question number 13")
basis = int(input("Enter the basis: "))
if basis <= 150000:
    tax = 0
    print("Tax: ",tax)
elif basis >= 150000 and basis <= 300000:
    tax = (20/100) * basis
    print("Tax: ", tax)
elif basis > 300000:
    tax = (30/100) * basis
    print("Tax: ", tax)

input("\nPress Enter for next question...")



# 14) Write a program in Python to calculate and print the power m of a number n without using ** operator or pow (n, m) function
print("Question number 14")
n = int(input("Enter the number (n): "))
m = int(input("Enter the power (m): "))

result = 1

for i in range(m):
    result = result * n

print(n, "raised to the power", m, "=", result)

input("\nPress Enter for next question...")



# 15) Write a program i n Python to input 8 numbers from user. It should find and print the smallest value among these.
print("Question number 15")
smallest = float('inf')

for i in range(1, 9):
    num = float(input(f"Enter number {i}: "))
    
    if num < smallest:
        smallest = num

print("Smallest value is:", smallest)

input("\nPress Enter for next question...")




# 16) Write a program in Python to print odd numbers from 1 to 10 except 7. (Hint: use continue statement)
print("Question number 16")
for i in range(1,11):
    if i == 7:
        continue
    if i % 2 != 0:
        print(i,"odd")
input("\nPress Enter for next question...")




#17) Write a program in Python to calculate the sum of numbers in the range from m to n which are not divisible by 2,3 or 5. where m<n.
print("Question number 17")
m = int(input("Enter m: "))
n = int(input("Enter n: "))

total = 0

for i in range(m, n + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        total += i

print("Sum =", total)

input("\nPress Enter for next question...")



#18) Write a program in Python to calculate and print all factors of a number. And think for optimizing the program. (Hint: N /2 times)
print("Question number 18")
n = int(input("Enter a number: "))

print("Factors of", n, "are:")

for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=" ")

print(n)

input("\nPress Enter for next question...")



#19) Write a program in Python to accept one string from user. The program should count
#and print the number of characters in the string using a for loop, without using inbulit functions.
print("Question number 19")
char = input("Enter a string: ")
count = 0
for i in char:
    
        count += 1
print("Number of character: ", count)

input("\nPress Enter for next question...")



#20) Write a program in Python to input a sentence with digits also. The program should
#count the number of uppercase letters, lowercase letters and digits in the sentence.

print("Question number 20")
sentence = input("Enter a sentence: ")

uppercase = 0
lowercase = 0
digits = 0

for ch in sentence:
    if 'A' <= ch <= 'Z':
        uppercase += 1
    elif 'a' <= ch <= 'z':
        lowercase += 1
    elif '0' <= ch <= '9':
        digits += 1

print("Uppercase letters =", uppercase)
print("Lowercase letters =", lowercase)
print("Digits =", digits)

input("\nPress Enter for next question...")


#21) Write a program in Python to generate and print Fibonacci series upto first 10 numbers.
#The Fibonacci series is 0,1,1,2,3,5,8,13… where first term is 0, second term is 1 and the nth term t(n) = t (n 1) + t (n 2).
print("Question number 21")
a = 0
b = 1

print("Fibonacci Series:")

for i in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


input("\nPress Enter for next question...")


#22) Write a program in Python to generate a number whose triangular number is given.
#If number is 4, then the triangular number would be 10 (i.e. 1+2+3+4). The program should return 'ER ROR', if it is not a triangular number.

print("Question number 22")
t = int(input("Enter a triangular number: "))

sum = 0
n = 0

while sum < t:
    n += 1
    sum += n

if sum == t:
    print("Number =", n)
else:
    print("ERROR")

input("\nPress Enter for next question...")


#23 Write a program in Python to find the sum of 5 numbers entered by the user using a for loop.
print("Question number 23")
for i in range(5):
    num = int(input(f"Enter the numeber{i + 1}: "))
    sum += num
    print("Sum: ", sum)

input("\nPress Enter for next question...")



#24 Write a program in Python to find the sum of the series 1+3+5+7+…upto 31 using for loop.
print("Question number 24")
for i in range(1,32,2):
    sum += i
    print("Sum: ", sum)

input("\nPress Enter for next question...")



#25 Write a program in Python to print sum of first 10 odd numbers and first 10 e ven numbers using while loop.
print("Question number 25")
odd_sum = 0
even_sum = 0

odd = 1
even = 2

count = 1

while count <= 10:
    odd_sum += odd
    even_sum += even

    odd += 2
    even += 2
    count += 1

print("Sum of first 10 odd numbers =", odd_sum)
print("Sum of first 10 even numbers =", even_sum)
input("\nPress Enter for next question...")




#26 Write a program in Python to print table of any number 'n' provided by user using while loop.
print("Question number 26")
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
input("\nPress Enter for next question...")




#  27 Write a program to find the factorial of a given positive integer n. The factorial of a number is the product of all the integers from 1 to n.
print("Question number 27")
n = int(input("Enter a positive integer: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorial of", n, "=", factorial)
input("\nPress Enter for next question...")



# 28 W rite a Python program to check a given positive number is a numeric palindrome or not.
print("Question number 28")
num = int(input("Enter a positive number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
input("\nPress Enter for next question...")



# 29) Write a program to convert a binary number to a decimal number without using built in function provided by Python.
print("Question number 29")
binary = input("Enter a binary number: ")
valid = True

for digit in binary:
    if digit != '0' and digit != '1':
        valid = False
        break

if not valid:
    print("Invalid Binary Number")
else:
    decimal = 0
    power = 0

    
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1

    print("Decimal Number =", decimal)

input("\nPress Enter for next question...")



# 30) Write a program to check the given positive integer N is divisible by 3 or not. If yes, verify that N is also an even number
print("Question number 30")
N = int(input("Enter a positive integer: "))

if N % 3 == 0:
    print("N is divisible by 3")

    if N % 2 == 0:
        print("N is also an even number")
    else:
        print("N is not an even number")
else:
    print("N is not divisible by 3")

input("\nPress Enter for next question...")


# 31) Write a program to print all the multiples of 5 from 1 to n for a given positive integer n.
print("Question number 31")
n = int(input("Enter a positive integer: "))

print("Multiples of 5 from 1 to", n, "are:")

for i in range(5, n + 1, 5):
    print(i, end=" ")

input("\nPress Enter for next question...")




# 32) Write a program in Python t o print all factors of a given positive integer n.
print("Question number 32")
n = int(input("Enter a positive integer: "))

print("Factors of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

input("\nPress Enter for next question...")




# 33) Write a program to find out the highest common factor (HCF) of two given positive
#integers n and m. Then use HCF of n and m to find the least common multiple (LCM) of n and m
print("Question number 33")
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

a = n
b = m

while b != 0:
    a, b = b, a % b

hcf = a
lcm = (n * m) // hcf

print("HCF =", hcf)
print("LCM =", lcm)


input("\nPress Enter for next question...")



# 34) Let N be a positive integer (read as the input). Verify that the English calendar year
#with year number N is a leap year or not. Note that you are not allwed to look into
#the calendar of the year. Just, with the information of year number you need to
#answer that the year is a leap or not.
print("Question number 34")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

input("\nPress Enter for next question...")


# 35) Write a program to read the registration number (last four digits) and verify whether
#the car is allowed on roads on a particular d ay or not. You do not read the day of the
#week as part of the input.

print("Question number 35")

car_no = int(input("Enter car number (last four digits): "))

if car_no % 2 == 0:
    print("CAR IS ALLOWED ON ROADS OF DELHI CITY")
else:
    print("CAR IS NOT ALLOWED ON ROADS OF DELHI CITY")

input("\nPress Enter for next question...")




# 36) A banking company sends a 6 digit integer number as one time password (OTP) to
#its c ustomer mobile for all mobile banking transactions. An integer is a valid OTP if
#(1) it is of six digit length and (2) contains the same number of even and odd digits.
#Further, the OTP does not start with 0. Write a python program to read an integer and
#ve rify whether it is a valid OTP or not.
print("Question number 36")

otp = input("Enter a 6-digit OTP: ")


if len(otp) != 6 or otp[0] == '0':
    print("Invalid OTP")
else:
    even_count = 0
    odd_count = 0

    for digit in otp:
        if not ('0' <= digit <= '9'):
            print("Invalid OTP")
            break

        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    else:
        if even_count == odd_count:
            print("Valid OTP")
        else:
            print("Invalid OTP")