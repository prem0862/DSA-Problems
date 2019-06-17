"""
	Given a number N >= 0, find its representation in binary.

	Example:

	if N = 6,

	binary form = 110
"""

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        stack = []
        quotient = A
        binary_rep = ""
        if A == 0:
            return 0
        while quotient > 0:
            stack.append(quotient%2)
            quotient = quotient/2
        while(stack != []):
            binary_rep += str(stack.pop())
        return binary_rep