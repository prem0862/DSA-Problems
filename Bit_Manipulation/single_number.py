"""
	Given an array of integers, every element appears twice except for one. Find that single one.

	Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

	Example :

	Input : [1 2 2 3 1]
	Output : 3

"""



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        single_element = 0
        for element in A:
            single_element = (single_element ^ element)
        return single_element