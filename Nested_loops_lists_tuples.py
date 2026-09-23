#1 Write a program in Python to print the following patterns u s i n g l o o p
print("Question number 01")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
input("\nPress Enter for next pattern...")


for i in range(4):
    for j in range(5, 0, -1):
        print(j, end=" ")
    print()

input("\nPress Enter for next pattern...")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

input("\nPress Enter for next pattern...")



for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


input("\nPress Enter for next pattern...")



for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(5):
    print("| | | |")

for i in range(5):
    print("| | | |")

input("\nPress Enter for next pattern...")


n = 7

for i in range(n):

    
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print("   ", end="")  
    
    for j in range(n):
        if (i <= n//2 and (i == j or i + j == n - 1)) or \
           (i > n//2 and j == n//2):
            print("*", end="")
        else:
            print(" ", end="")

    print("   ", end="")


    for j in range(n):
        if i == 0 or i == n - 1 or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()


# 2) Let A = [ -5, 3, 6, 7, -9, -11, -4, 8, 11, 14, -17, -15, 15] be a list of integers. Write a
#program to create two sepearate list B and C where B contains all positive integers in
#A and C contains all negative numbers in A. Output both lists B and C.
print("Question number 02")
A = [-5, 3, 6, 7, -9, -11, -4, 8, 11, 14, -17, -15, 15]
B = []
C = []

for i in A:
    if i > 0:
        B.append(i)
    elif i < 0:
        C.append(i)
print(B)
print(C)
input("\nPress Enter for next pattern...")


# 3) A=[3,17,9,2,4,8,97,43,39,10,3,17,1,9,2,4,8,97,43,39] be a list of positive integers.
#Find three lists, one contains all prime numbers in A, second one contains com posit
#numbers in A, and the third list contains all other numbers in A which are neither
#prime nor composite
print("Question number 03")
A=[3,17,9,2,4,8,97,43,39,10,3,17,1,9,2,4,8,97,43,39]
b = []
c = []
d = []

for i in A:
    if i == 1:
        d.append(i)
    else:
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            b.append(i)
        else:
            c.append(i)

print("Prime =", b)
print("Composite =", c)
print("Neither =", d)
input("\nPress Enter for next pattern...")



# 4)Write a program that accepts two p ositive integers a and b (a is smaller than b) and
#returns a list that contains all the odd numbers between a and b (including a and
#including b if applicable) in descending order.
print("Question number 04")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = []

if a < b:
    for i in range(a, b + 1):
        if i % 2 != 0:
            c.append(i)

    c.sort(reverse=True)
    print(c)

else:
    print("Exit..!")
    
    

input("\nPress Enter for next pattern...")


# 5 Write a program to check duplicate elements in a list. It should print all the elem e nts which are unique in the list.
print("Question number 05")
A = [1, 1, 3, 5,5, 3, 6, 7]

for i in A:
    if A.count(i) == 1:
        print(i, end=" ")

input("\nPress Enter for next pattern...")


# 6 Consider that A be a list of integers with duplicates. Find the integer in A which
#appeared most number of times in A.
print("Question number 06")
A = [3, 17, 9, 2, 4, 8, 97, 43, 39, 10, 3, 17, 1, 9, 2, 4, 8, 97, 43, 39]

max_count = 0
most_frequent = A[0]

for i in A:
    count = A.count(i)

    if count > max_count:
        max_count = count
        most_frequent = i

print("Most frequent element =", most_frequent)
print("Frequency =", max_count)

input("\nPress Enter for next pattern...")


#7 ) Write a program to print all primes up to a given integer n by using the fact that a
#number is said to be a prime if it is not divisible by any prime number less than
#  it.
#Your program should avoid unnecessory divisions to decide a number is a prime or not.

print("Question number 07")
n = int(input("Enter n: "))

primes = []

for num in range(2, n + 1):
    is_prime = True

    for p in primes:
        if p * p > num:
            break

        if num % p == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)



print("Prime numbers up to", n, "are:")
for p in primes:
    print(p, end=" ")

input("\nPress Enter for next pattern...")


# 8) Let A be a list of integers (read the input from the user). Modify the list A such that
#the minimum element in A is at the start of the list. (Other elements can be in any
#order, but all other elements from A mus t present in the modified list)
#DO NOT USE NEW LIST. No predefined function is allowed to use, except append()
#and remove().
print("Question number 08")

A = list(map(int, input("Enter elements: ").split()))


min_ele = A[0]

for i in A:
    if i < min_ele:
        min_ele = i
A.remove(min_ele)
A = [min_ele] + A

print("Modified List:", A)
input("\nPress Enter for next pattern...")



# 9) Let A be a list of integers (read the input from the user). Modify the list A such that
#the elements are in the increasing order (all elements in A must be in the modified list).
#DO NOT USE NEW LIST. No prede fined function is allowed to use, except append()
#and remove().
print("Question number 09")
A = []

n = int(input("Enter the size of the list: "))

print("Enter", n, "elements into the list:")

for i in range(n):
    x = int(input())
    A.append(x)

print("Given list :", A)

for i in range(n):
    for j in range(n - 1):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp

print("Modified list :", A)
input("\nPress Enter for next pattern...")


#10) Q.10) Let data=[[10, 3], [5, 4], [7, 5], [3, 6], [2, 7], [0, 8], [1, 9]] be a (two dimensional) list
#representing the data of marks of a classs where [x,y] means x number of students
#scored mark y.
#Write a program to find the average mark of the class.
print("Question number 10")
data = [[10, 3], [5, 4], [7, 5], [3, 6], [2, 7], [0, 8], [1, 9]]

total_marks = 0
total_students = 0

for i in data:
    total_marks = total_marks + (i[0] * i[1])
    total_students = total_students + i[0]

average = total_marks / total_students

print("Avg mark :", average)
input("\nPress Enter for next pattern...")




#11) Let A=[4, 5, 6, 5, 3, 2, 8, 0, 4, 6, 7, 8, 4, 5, 7, 9, 8, 6, 7, 5, 5, 4, 2, 1, 9, 3, 3, 4, 6, 4] be
#a list. Create a new two dimensional list B=[[ , ], [ , ], ...., [ , ]] such that for an
#element [x, y] in B, x denote a value of an element in A and y denotes how many
#times x appeared in list A.
print("Question number 11")
A=[4, 5, 6, 5, 3, 2, 8, 0, 4, 6, 7, 8, 4, 5, 7, 9, 8, 6, 7, 5, 5, 4, 2, 1, 9, 3, 3, 4, 6, 4] 
B = []

for i in A:
    found = False

    for j in B:
        if j[0] == i:
            found = True
            break

    if not found:
        B.append([i, A.count(i)])

print(B)
input("\nPress Enter for next pattern...")



#12) Let A = [["Brasil"," ["India","New Delhi"], ["Srilanka","
#["Pakistan"," ["Japan","Tokyo"]] be a list of countries with their capital
#cities. Now, read a country name from the user. If the country name is presented in
#list A, then display that "the country is already in the list". Otherwise, read the capital
#city of the country from the user and add both, country along with its capital city to city of the country from the user and add both, country along with its capital city to the list. Repeat the process for a couple of iterationsthe list. Repeat the process for a couple of iterations and finally print the updated list and finally print the updated list A.A.
print("Question number 12")
A = [["Brasil", "Rio"],
     ["India", "New Delhi"],
     ["Srilanka", "Colombo"],
     ["Pakistan", "Islamabad"],
     ["Japan", "Tokyo"]]

while True:
    country = input("Enter country: ")

    found = False

    for i in A:
        if i[0].lower() == country.lower():
            found = True
            break

    if found:
        print(country, "is already in the list")
    else:
        capital = input("Enter capital of " + country + ": ")
        A.append([country, capital])

    ch = int(input("Do you want to continue?\nEnter 1 for Yes 0 for No: "))

    if ch == 0:
        break

print("List A =", A)
input("\nPress Enter for next pattern...")



#13) Suppose that a web browser mai ntains a list of recently visited pages. Assume that it
#can only store at most five pages which are recently (latest) visited by the user. If a
#page is revisited after some time, it only saves the newest visit, and it will store only
#distinct pages. The la st page in the list is the newest visited one, the before last page
#visited after all its predessors in the list and it is true for all other pages in the list.
#More sepcifically, the latest visit of a page in the list is after the latest visit of the its
#preceding pages in the list.
#Write a python program to implement the above protocol with an assumption that
#every page address is a positive integer. When you enter a negative page
#number, the program will not store the page number in the list and further, it
#prints the entries in the list and halts.
print("Question number 13")
pages = []

while True:
    page = int(input("Enter page number: "))

    if page < 0:
        break

    
    if page in pages:
        pages.remove(page)

    pages.append(page)
    
    if len(pages) > 5:
        pages.remove(pages[0])

print("Recently visited pages:", pages)
input("\nPress Enter for next pattern...")



#14) Write a python program for the following:
#Read two string from the user and verify that the seco nd string is a substring of the
#first one.
#Note that use are not allowed to use any predefined functions, except len().
#Hi n t: use slice operator to solve the problem.
print("Question number 14")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

found = False

for i in range(len(s1) - len(s2) + 1):
    if s1[i:i + len(s2)] == s2:
        found = True
        break

if found:
    print("Second string is a substring of first string")
else:
    print("Second string is not a substring of first string")
input("\nPress Enter for next pattern...")




#15) Write a Python program to solve the following problem.
#There ar e N apples in a bag, which need to be distributed among three kids X, Y, and
#Z such that X and Y should get three apples each and Z must get at least two
#apples. List all possible answers.
#You store all possible answers in a list and once you are done with appending all
#possible solutions in the list, display the the number of possible solutions
#along with the solutions.


# X, Y and Z must each get at least 3, 3 and 2 apples respectively
print("Question number 15")
N = int(input("Enter the number of apples in the bag: "))

solutions = []

for x in range(3, N + 1):
    for y in range(3, N + 1):
        z = N - x - y

        if z >= 2:
            solutions.append((x, y, z))

if len(solutions) == 0:
    print("No solution !!!!")
else:
    print("The number of possible solutions are :", len(solutions))
    print("The possible solutions are:", solutions)