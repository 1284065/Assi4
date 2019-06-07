#!/usr/bin/env python
from sys import argv
prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
	        

for i in range(int(argv[1])):
    if is_prime_number(i):
        prime_numbers += 1
        print i

print "We found " + str(prime_numbers) + " prime numbers."
