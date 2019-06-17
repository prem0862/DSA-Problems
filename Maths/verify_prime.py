"""
	Given a number N, verify if N is prime or not.

	Return 1 if N is prime, else return 0.

	Example :

	Input : 7
	Output : True

"""

from math import sqrt
import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A==1:
            return 0
        elif A==2:
            return 1
        else:
            for i in range(2,  int(sqrt(A))+1):
                if A%i == 0:
                    return 0