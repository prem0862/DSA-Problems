"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1

"""


import math
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        number = A
        trailing_zeros = 0
        diviser = 5
        while number > 0:
            number = math.floor(number/diviser)
            trailing_zeros = trailing_zeros + number
        return trailing_zeros