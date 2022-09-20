#Problem_3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

number = 600851475143
first_prime = 2
while first_prime <= number:
    if number%first_prime ==0:
        number /= first_prime
    else:
        first_prime += 1
print(first_prime)