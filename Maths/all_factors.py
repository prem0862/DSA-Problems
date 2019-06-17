"""	
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}

"""

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        empty_list = []
        if A == 1:
            return A
        for i in range(1, int(math.sqrt(A))):
            if A%i == 0:
                empty_list.append(i)
                if i != int(math.sqrt(A)):
                    empty_list.append(int(A/i))
        return sorted(empty_list)