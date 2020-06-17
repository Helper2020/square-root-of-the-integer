import math

"""
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number < 0:
        number *= -1

    x = 0
    n = number

    while True:
        x = (n + number / n) / 2

        if x == n:
            return int(x // 1)

        n = x







print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
# Edge cases
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (3 == sqrt(9.5)) else "Fail")
# will convert -9 to 9 to return 3
print("Pass" if (3 == sqrt(-9)) else "Fail")