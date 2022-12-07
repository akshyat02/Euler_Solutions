# https://projecteuler.net/problem=41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

def isPandigital(n):
    return ''.join(sorted(set(str(n)))) == ''.join(sorted(str(n)))

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

def largestPandigitalPrime(n):
    str = "9876543210"
    for i in range(int(str[:n]),0,-1):
        if isPandigital(i):
            if isPrime(i):
                return i

def main():
    n=int(input("Enter digit: "))
    print(largestPandigitalPrime(n))
    

main()