"""
	Write a function that takes an unsigned integer and returns the number of 1 bits it has.

	Example:

	The 32-bit integer 11 has binary representation

	00000000000000000000000000001011
	so the function should return 3.

"""


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        num_of_ones = 0
        number = A
        while(number > 0):
            reminder = number % 2
            if reminder == 1:
                num_of_ones += 1
            number = number / 2
        return num_of_ones