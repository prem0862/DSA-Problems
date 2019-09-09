
# Problem: https://www.interviewbit.com/problems/grid-unique-paths/



import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        
        # Approcah: here we have to take total of (m +n -2) steps which consists of 
        # moving towards two direction (down and right)
        
        total_paths = int(math.factorial((A -1)+(B -1))/ (math.factorial(A -1) * math.factorial(B -1)))
        return total_paths
