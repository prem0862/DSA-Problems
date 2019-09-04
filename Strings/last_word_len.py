
# Problem: https://www.interviewbit.com/problems/length-of-last-word/




class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        flag = False
        count = 0
        
        for i in range(len(A) -1, -1, -1):
            if ((A[i] >= "a" and A[i] <= "z") or (A[i] >= "A" and A[j] <= "Z")):     
                flag = True
                count += 1
            else:
                if flag == True:
                    return count
        return count
                
        
