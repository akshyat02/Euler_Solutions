# https://projecteuler.net/problem=35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million ?

def isPrime(n):
    n = int(n)
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

def isCircularPrime(n):
    s = str(n)
    c = len(s)
    i=1
    if int(s) < 10:
        return isPrime(s)
    while i<c+1:
        s = s[-1] + s[0:-1]
        if not isPrime(s):
            return False
        i+=1
    return True
            

def main():
    plus = 0
    for i in range(0, 1000000):
        if isCircularPrime(i):
            plus += 1
    print(plus)

main()