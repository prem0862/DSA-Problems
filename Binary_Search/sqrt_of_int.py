"""

	Implement int sqrt(int x).

	Compute and return the square root of x.

	If x is not a perfect square, return floor(sqrt(x))

	Example :

	Input : 11
	Output : 3

	DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY

"""



class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        high = A
        low = 1
        while low <= high:
            mid = (low + high) / 2
            # Check if mid = floor(sqrt(A))
            if  mid*mid <= A and (mid+1)*(mid+1) > A:
                return mid
            elif mid*mid < A:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0 # If we were given 0, return 0 (this is the only way we'll get here