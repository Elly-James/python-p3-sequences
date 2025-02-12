#!/usr/bin/env python3

# Write a function print_fibonacci() that prints a list of the
#  fibonacci sequenceLinks to an external site. 
# up to the length provided in the function's parameters.
# print_fibonacci(9)
# => [0, 1, 1, 2, 3, 5, 8, 13, 21]
# they should be printed in new line \n

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence)

print_fibonacci(10)
