"""
	Reverse digits of an integer.

	Example1:

	x = 123,

	return 321
	Example2:

	x = -123,

	return -321

	Return 0 if the result overflows and does not fit in a 32 bit signed integer

"""



import math
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = -1 if A < 0 else 1
        number = abs(A)
        rev = 0
        while number > 0:
           reminder = number % 10
           rev = rev*10 + reminder
           number = math.floor(number/10)
        
        if rev < (2**31):
            return rev*sign
        else:
            return 0