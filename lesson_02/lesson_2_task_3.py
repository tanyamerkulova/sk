import math


def square(a):
    if a % 1 != 0:
        a = math.ceil(a)
    print(a*a)


square(5)
