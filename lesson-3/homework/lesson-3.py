# 1.
fruits = ["apple", "banana", "cherry", "orange", "mango"]
print("Third fruit:", fruits[2])

# 2. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

# 3.
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("New list:", new_list)

# 4. 
movies = ["Inception", "Avatar", "Titanic", "Interstellar", "Joker"]
movies_tuple = tuple(movies)
print("Movies Tuple:", movies_tuple)

# 5.
cities = ["London", "Paris", "New York", "Tokyo"]
print("Is Paris in the list?", "Paris" in cities)

#6.
nums = [1, 2, 3]
duplicate = nums * 2
print("Duplicated List:", duplicate)

# 7. 
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("Swapped List:", nums)

# 8. 
t = tuple(range(1, 11))
print("Slice (index 3 to 7):", t[3:8])

# 9. 
colors = ["blue", "red", "green", "blue", "yellow", "blue"]
print("Blue count:", colors.count("blue"))

# 10. 
animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))

# 11. 
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("Merged Tuple:", merged)

# 12. 
lst = [1, 2, 3, 4]
tpl = (5, 6, 7, 8, 9)
print("List length:", len(lst))
print("Tuple length:", len(tpl))

# 13.
tpl = (10, 20, 30, 40, 50)
lst = list(tpl)
print("Converted List:", lst)

# 14. 
nums = (15, 2, 98, 45, 67)
print("Max:", max(nums))
print("Min:", min(nums))

# 15. Reverse a Tuple
words = ("apple", "banana", "cherry", "date")
print("Reversed Tuple:", words[::-1])
