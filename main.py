#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Nikal Morgan"


def add(x, y):
    """Add two integers."""
    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    totalNum1 = abs(x)
    z = x
    for i in range(1, abs(y)):
        x = add(abs(x), totalNum1)
        # print(x)
    # print(z < 0 )
    # print(y < 0)
    # print(z < 0 and y < 0)
    if z < 0 and y < 0:
        return x
    if z < 0 or y < 0:
        return -x
    return x


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    totalPower = x
    for i in range(1,n):
        x = multiply(x, totalPower)
    return x


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    totalFact = x
    for i in range(x-1,0, -1):
        totalFact = multiply(totalFact, i)
    return totalFact


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    fibArray = [0, 1]
    fibNum = 0
    for i in range(0,n-1):
        fibNum = fibArray[i] + fibArray[i + 1]
        fibArray.append(fibNum)
    return fibArray[n- 1]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}    expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))

def main():
    print('add')
    test(add(4, 5), 9)
    test(add(4,-5), -1)
    test(add(10,-15), -5)
    test(add(-10,-15), -25)

    print('\nmultiply')
    test(multiply(5,-2), -10)
    test(multiply(5,2), 10)
    test(multiply(-3,-4), 12)
    test(multiply(3,4), 12)

    print('\npower')
    test(power(2,3), 8)
    test(power(4,2), 16)
    test(power(5,3), 125)
    test(power(3,4), 81)

    print('\nfactorial')
    test(factorial(2), 2)
    test(factorial(3), 6)
    test(factorial(4), 24)
    test(factorial(5), 120)

    print('\nfibonacci')
    test(fibonacci(1), 0)
    test(fibonacci(3), 1)
    test(fibonacci(4), 2)
    test(fibonacci(5), 3)


if __name__ == '__main__':
    main()


