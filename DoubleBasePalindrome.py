# https://projecteuler.net/problem=36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def isPalindrome(s):
    return s==s[::-1]

def main():
    plus=0
    for i in range(0,1000000):
        if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
            plus+=i
    print(plus)
            
main()