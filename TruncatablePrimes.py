# https://projecteuler.net/problem=37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def isPrime(n):
    if n < 2: 
         return False
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def leftTruncatable(n):
    while(n>10):
        n = int(str(n)[1:])
        if not isPrime(n):
            return False
    return True
            
def func():
    primestillnow = [2, 3, 5, 7]
    addlist = [1, 3, 7, 9] #numbers to be added into middle or to the end
    plus = 0
    while primestillnow:
        prime = primestillnow.pop(0)
        for digit in addlist:
            temp = prime * 10 + digit
            if isPrime(temp):
                primestillnow.append(temp)
                if leftTruncatable(temp):
                    plus += temp
    return plus

print(func())