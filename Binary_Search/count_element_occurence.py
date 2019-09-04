
# Problem: https://www.interviewbit.com/problems/count-element-occurence/



class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def find_index(self, A, B, first_search):
        start = 0
        end = len(A) -1
        result = -1
        while(start <= end):
            mid = (start + end)//2
            if A[mid] == B:
                result = mid
                if first_search:
                    end = mid -1
                else:
                    start = mid +1
            elif A[mid] < B:
                start = mid +1
            elif A[mid] > B:
                end = mid -1
        return result
                
            
    def findCount(self, A, B):
        first_search = self.find_index(A, B, first_search = True)
        last_search = self.find_index(A, B, first_search = False)
        occurrence =  last_search - first_search + 1
        if first_search == -1 and last_search == -1:
            return 0
        return occurrence
        
        
