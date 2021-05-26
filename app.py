# print("Hello World")
"""print("    / |")
print("   /  |")
print("  /   |")
print(" /____|")
========= variables
age = 20
age = 30
first_name = "Ravali"
is_online = False

print(age)"""
# ======
"""name = input("what is yor name? ")
print("Hello " +name)
# ======
birth_year = input("what is your birth year? ")
age = 2021 - int(birth_year)
print(age)
print("Your age is " +str(age))"""
# ====== type conversions
"""first_number = input("Enter first number ")
print(first_number)
sec_number = input("Enter second number ")
print(sec_number)
sum = float(first_number) + float(sec_number)
print(sum)
print("Sum is " + str(sum))"""
# ====== Strings
"""course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course)
print(course.find("y"))
print(course.find("for"))
print(course.find("Y"))
print(course.replace("for", "4"))
print(course.replace("X", "4"))
print(course.find("Python"))
print("Python" in course)"""
# ====== Arithmetic operators
"""print(15 + 10)
print(15 - 10)
print(15 * 10)
print(15 / 10)
print(15 // 10)
print(15 % 10)
print(15 ** 10)
x = 10
x +=3
print(x)
x -=3
print(x)
x *=3
print(x)"""
# ====== Operator Precedence
"""x= 10 + 3 * 2
print(x)
x= (10 + 3) * 2
print(x)"""
# ====== Comparison Operators
"""x = 3 > 2
print(x)
x = 3 >= 2
print(x)
x = 3 < 5
print(x)
x = 3 <= 2
print(x)
x = 3 == 2
print(x)
x = 3 != 2
print(x)"""
# ====== Logical Operators
"""price = 25
print(price > 20 and price < 30)
price = 15
print(price > 20 or price < 30)
price = 40
print(not price > 20)"""
# ====== If Statements
"""temp = 5
if temp > 30:
    print("It's is a hot day")
    print("Drink plenty of water")
elif temp > 20:
    print("It's is a nice day")
elif temp > 10:
    print("It's is a bit cold")
else:
    print("It's is cold")
print("Done")
# ============== Exericse
weight = int(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lbs " +str(converted))
else:
    converted = weight * 0.45
    print("weight in lbs " +str(converted))"""

# ====== While Loops
"""i = 1
while i <= 1000:
    print(i)
    i = i + 1
# ======
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1"""
# ====== Lists
"""names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names)
print(names[0])
print(names[-1])
print(names[0:3])
print(names)"""
# ====== List Methods
"""numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(3, 7)
numbers.insert(0, -1)
numbers.remove(3)
# numbers.clear()
print(10 in numbers)
print(len(numbers))
print(numbers)"""
# ====== For loops
"""numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

i = 0
while i <= len(numbers):
    print(numbers[i])
    i = i+1"""
# ====== The Range Function
""""numbers = range(5)
print(numbers)
for number in numbers:
    print(number)
numbers = range(5, 10)
print(numbers)
for number in numbers:
    print(number)
numbers = range(5, 10, 2)
print(numbers)
for number in numbers:
    print(number)
for number in range(5,10):
    print(number)"""
# ====== Tuples
numbers = (1, 2, 3, 2)
# numbers[0] = 10
print(numbers.count(2))
print(numbers.index(2))
# =============
"""
$ python3 -m venv venv
$ source venv/bin/activate # in Windows -> $ venv\Scripts\activate.bat
$ pip install pytest
"""
























