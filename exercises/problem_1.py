'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def problem_1(limit, *args):
    
    sum_multiples = 0
    
    for i in range(limit):
        for numbers in args:
            if i%numbers == 0:
                sum_multiples += i
                break
    return sum_multiples

print(problem_1(1000, 3, 5))
