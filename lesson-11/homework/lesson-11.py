from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file


print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(6, 7))
print("Divide:", divide(20, 5))


print("Reversed string:", reverse_string("Murodjon"))
print("Vowel count:", count_vowels("Murodjon"))


print("Circle area:", calculate_area(7))
print("Circle circumference:", calculate_circumference(7))


write_file("example.txt", "Hello, Murodjon! This is a test file.")
print("File content:", read_file("example.txt"))
