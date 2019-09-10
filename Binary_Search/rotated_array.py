
# Problem: https://www.interviewbit.com/problems/rotated-array/



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        low = 0
        high = n -1
        
        while(low <= high):
            
            if A[low] <= A[high]:
                # true if arry is linearly sorted
                return A[low]
            
            mid = (low + high)//2
            next_ind = (mid +1) % n
            prev = (mid -1 + n) % n
            
            if A[mid] <= A[prev] and A[next_ind] >= A[mid]:
                #  condition for minimum element
                return A[mid]
            elif A[mid] >= A[low]:
                # so min element can't be in left part
                low = mid +1
            elif A[mid] <= A[high]:
                # so min element can't be in right half part
                high = mid -1
                 
