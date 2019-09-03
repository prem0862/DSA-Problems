"""
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Here are few examples.

    [1,3,5,6], 5 → 2
    [1,3,5,6], 2 → 1
    [1,3,5,6], 7 → 4
    [1,3,5,6], 0 → 0

"""



class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        a_size = len(A)
        if a_size >= 1:
            if B < A[0]: return 0
            if B > A[a_size -1]: return a_size
        
        start = 0
        end = a_size -1
        while(start <= end):
            mid = (start + end)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B and A[mid -1] < B:
                return mid
            elif A[mid] < B and A[mid +1] > B:
                return mid +1
            elif A[mid] > B:
                end = mid -1
            elif A[mid] < B:
                start = mid +1
        