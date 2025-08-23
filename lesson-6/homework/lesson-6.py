
# 1


def modify_string(txt):
    result = []
    count = 0
    vowels = "aeiou"

    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
           
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i+1] == "_"):
                pass
            else:
                if i != len(txt) - 1:  
                    result.append("_")
            count = 0
        i += 1

    return "".join(result)


print(modify_string("hello"))         
print(modify_string("assalom"))        
print(modify_string("abcabcabcdeabcdefabcdefg")) 

# 2


n = int(input())
for i in range(n):
    print(i**2)
# 3


i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

n = int(input("Enter number: "))
s = sum(range(1, n+1))
print("Sum is:", s)


num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i, end=" ")

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num < 200:
        print(num)


num = 75869
print(len(str(num)))


n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i, end=" ")


for i in range(-10, 0):
    print(i, end=" ")


for i in range(5):
    print(i)
else:
    print("Done!")


start, end = 25, 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")


a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"\n{n}! =", fact)


# 4

def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for x in list2:
        if x not in list1:
            result.append(x)
    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))           
print(uncommon_elements([1, 2, 3], [4, 5, 6]))           
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 




