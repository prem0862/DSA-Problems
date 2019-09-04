
# Problem: https://www.interviewbit.com/problems/noble-integer/



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        numbers = A
        numbers.sort()
        total_num = len(numbers)
        
        if numbers[total_num -1] == 0:
            return 1
            
        for i in range(0, total_num -1):
            if numbers[i] == numbers[i +1]:
                continue
            if (total_num -i -1) == abs(numbers[i]):
                return 1
        return -1