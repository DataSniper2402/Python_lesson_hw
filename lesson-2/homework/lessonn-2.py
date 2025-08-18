# 1. 
from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

# 2.
txt = 'LMaasleitbtui'
car1 = txt[::2]   
car2 = txt[1::2] 
print(car2, car1)


# 3.
txt = 'MsaatmiazD'
car1 = txt[::2]  
car2 = txt[1::2] 
print(car2, car1

# 4.
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Residence Area:", area)

# 5.
s = input("Enter a string: ")
print("Reversed:", s[::-1])

# 6. 
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in word if ch in vowels)
print("Number of vowels:", count)

# 7.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", max(numbers))

# 8.
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("Palindrome ")
else:
    print("Not Palindrome ")

#
email = input("Enter your email: ")
domain = email.split("@")[-1]
print("Domain:", domain)

# 10. 
import random, string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))
print("Generated Password:", password)
