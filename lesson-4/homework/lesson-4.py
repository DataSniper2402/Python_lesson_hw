# 1. 
my_dict = {2: 30, 1: 10, 3: 20}
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# 2. 
sample = {0: 10, 1: 20}
sample[2] = 30
print("After adding:", sample)

# 3. 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {**dic1, **dic2, **dic3}
print("Merged Dictionary:", merged)

# 4.
n = 5
squares = {x: x**2 for x in range(1, n+1)}
print("Squares Dictionary:", squares)

# 5. 
squares_15 = {x: x**2 for x in range(1, 16)}
print("Squares 1 to 15:", squares_15)


# 1. 
my_set = {1, 2, 3, 4}
print(my_set)

# 2. 
for item in my_set:
    print("Item:", item)

# 3.
my_set.add(5)
my_set.update([6, 7])
print("After adding:", my_set)

# 4. 
my_set.remove(7)  
print("After remove:", my_set)

#5. 
my_set.discard(10)  
print("After discard (safe remove):", my_set)
