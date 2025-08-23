

# 1
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# 2

try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer!")
# 3

try:
    f = open("not_existing.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")
# 4

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a) + float(b)
    print("Result:", result)
except ValueError:
    raise TypeError("Error: Both inputs must be numbers!")
# 5

try:
    f = open("/etc/shadow", "r")  
except PermissionError:
    print("Error: You don't have permission to access this file!")

# 6
try:
    n = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", n)
except KeyboardInterrupt:
    print("\nInput canceled by user.")
# 7

try:
    n = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", n)
except KeyboardInterrupt:
    print("\nInput canceled by user.")
# 8
try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred!")
# 9

with open("test.txt", "r") as f:
    print(len(f.readlines()))
# 10

from collections import Counter
with open("test.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    print(Counter(words))
# 11

import os
print(os.path.getsize("test.txt"), "bytes")
# 12
data = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    for item in data:
        f.write(item + "\n")
# 13
with open("test.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
# 14
with open("f1.txt") as f1, open("f2.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip() + " " + b.strip())
# 15
import random
with open("test.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))
# 16

f = open("test.txt", "r")
print(f.closed)  
f.close()
print(f.closed)  
# 17
with open("test.txt") as f:
    lines = [line.strip() for line in f]
print(lines)
# 18
with open("test.txt") as f:
    text = f.read().replace(",", " ")
    words = text.split()
    print("Word count:", len(words))
# 19
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}\n")
      # 20
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}\n")
# 21
import string
letters = string.ascii_uppercase
n = 5
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")




















































