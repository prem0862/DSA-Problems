
# Problem: https://www.interviewbit.com/problems/amazing-subarrays/



class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        string = A
        vowels = ["a", "e", "i", "o", "u"]
        amazing_sub = 0
        string_size = len(string)
        for i in range(0, string_size):
            if string[i].lower() in vowels:
                amazing_sub += (string_size -i)
        
        return amazing_sub % 10003
