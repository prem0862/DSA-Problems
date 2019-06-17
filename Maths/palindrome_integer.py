"""
	Determine whether an integer is a palindrome. Do this without extra space.

	A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
	Negative numbers are not palindromic.

	Example :

	Input : 12121
	Output : True

	Input : 123
	Output : False

"""

import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A > 0:
            number = A
            reverse = 0
            while number > 0:
                reminder = number % 10
                reverse = reverse*10 + reminder
                number = math.floor(number/10)
            if reverse == A:
                return 1
            else:
                return 0
        else:
            return 0