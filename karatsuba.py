# import math module for getting the the smallest and largest integer value
# greater than or equal to x.
import math

# define the karatsuba function for fast multiplication of 2 integers


def karatsuba(a, b):
    # Multiply normally if the numbers are less than 10
    if a < 10 and b < 10:
        return a * b

    # else
    # maximum length of the two integers
    max_n = max(len(str(a)), len(str(b)))
    # Cast max_n into a float to get 4 different integer length
    m = math.ceil(max_n / 2)
    # equation here:
    #  -> k = x_H * y_H
    #  -> l = x_L * y_L
    #  -> e = (x_H + x_L) * (y_H + y_L)  - (x_H * y_H) - (x_L * y_L)
    #  -> x * y = (k * l^n) + (e * l^(n/2)) + d
    x_H = math.floor(a / int(math.pow(10, m)))
    y_H = math.floor(b / int(math.pow(10, m)))
    x_L = a % (int(math.pow(10, m)))
    y_L = b % (int(math.pow(10, m)))

    # Recursively getting the values of k,l,e
    k = karatsuba(x_H, y_H)
    l = karatsuba(x_L, y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - k - l

    # Return the final value for the function x * y
    # print(int(k * (int(math.pow(10, (m * 2)))) + e * (int(math.pow(10, m))) + l))
    return int(k * (int(math.pow(10, (m * 2)))) + e * (int(math.pow(10, m))) + l)


print(karatsuba(20, 100))
