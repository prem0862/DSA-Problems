"""
	Given an array of integers, sort the array into a wave like array and return it, 
	In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

	Example

	Given [1, 2, 3, 4]

	One possible answer : [2, 1, 4, 3]
	Another possible answer : [4, 1, 3, 2

	NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. So, in example case, you will return [2, 1, 4, 3] 

"""


class Solution:
    def wave(self, A):
        modified_a = sorted(A)
        for i in range(0, len(A)-1, 2):
            temp = A[i]
            modified_a[i] = modified_a[i+1]
            modified_a[i+1] = temp
        return modified_a