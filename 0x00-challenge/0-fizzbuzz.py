#!/usr/bin/python3
"""
FizzBuzz functiom prints from 1 to n separated by space.
- For multiples of 3 it pronts "Fizz" instead of the number.
- For multiples of 5 it prints "Buzz" instead of the number.
- While for multiples which are for both 3 and 5 it prints "FizzBuzz".
"""

import sys


def fizzbuzz(n):
    """Function body"""
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
