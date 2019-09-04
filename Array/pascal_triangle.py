
# Problem: https://www.interviewbit.com/problems/pascal-triangle/



class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0: return
        if A == 1: return [[1]]
        pascal_triangle = [[1], [1, 1]]
        if A == 2: return pascal_triangle
        
        for c in range(3, A +1):
            pascal_row = [1, 1]
            for i in range(1, c -1):
                pascal_row.insert(i, pascal_triangle[c -2][i] + pascal_triangle[c -2][i -1])
            pascal_triangle.append(pascal_row)
        
        return pascal_triangle
