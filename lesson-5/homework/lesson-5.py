

# 1. 
def is_leap(year):
    """
    Determines whether a given year is a leap year.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 2. 
def weird_or_not(n):
    """
    Given an integer n, determine whether it is Weird or Not Weird.
    """
    if n % 2 == 1:   # odd
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


# 3.

#  1 (with if-else)
def even_numbers_ifelse(a, b):
    if a > b:
        a, b = b, a
    return list(range(a + (a % 2), b + 1, 2))


#  2 
def even_numbers_no_ifelse(a, b):
    return list(range(min(a, b) + (min(a, b) % 2), max(a, b) + 1, 2))

#1

    print("Leap Year Tests:")
    print("2000 ->", is_leap(2000))  # True
    print("1900 ->", is_leap(1900))  # False
    print("2024 ->", is_leap(2024))  # True
    print()

    # 2
    print("Conditional Statements Tests:")
    print("n = 3 ->", weird_or_not(3))   # Weird
    print("n = 4 ->", weird_or_not(4))   # Not Weird
    print("n = 18 ->", weird_or_not(18)) # Weird
    print("n = 22 ->", weird_or_not(22)) # Not Weird
    print()

    # 3
    print("Even Numbers Between a and b:")
    print("If-Else (3, 12) ->", even_numbers_ifelse(3, 12))   # [4, 6, 8, 10, 12]
    print("No If-Else (12, 3) ->", even_numbers_no_ifelse(12, 3))  # [4, 6, 8, 10, 12]
