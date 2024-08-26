#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    for n in range(length):
        if n > 1:
            fib_list.append(fib_list[-1] + fib_list[-2])
        else:
            fib_list.append(n)

    print(fib_list)
    
# print_fibonacci(9)