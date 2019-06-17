"""
	Given a number N, find all prime numbers upto N ( N included ).

	Example:

	if N = 7,

	all primes till 7 = {2, 3, 5, 7}

	Make sure the returned array is sorted.

"""

import math

def IsPrime(A):
        flag = True
        if A == 1:
            return False
        for t in range(2,int(math.sqrt(A))+1):  
            if A%t == 0:
                flag = False
                break
        return flag

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        slist = []
        for x in range(2,int(A+1)):
            if IsPrime(x):
                slist.append(x)
        return slist