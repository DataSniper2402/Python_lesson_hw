

#1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))  
print(is_prime(7)) 

#2
def digit_sum(k):
    return sum(map(int, str(k)))
print(digit_sum(24))   
print(digit_sum(502)) 

#3
def powers_of_two(N):
    result = []
    k = 1
    while 2**k <= N:
        result.append(2**k)
        k += 1
    return result

print(powers_of_two(10))   
