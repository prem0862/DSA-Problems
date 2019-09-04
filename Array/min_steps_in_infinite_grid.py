"""
    You are in an infinite 2D grid where you can move in any of the 8 directions :

    (x,y) to 
        (x+1, y), 
        (x - 1, y), 
        (x, y+1), 
        (x, y-1), 
        (x-1, y-1), 
        (x+1,y+1), 
        (x-1,y+1), 
        (x+1,y-1) 

    You are given a sequence of points and the order in which you need to cover the points. 
    Give the minimum number of steps in which you can achieve it. You start from the first point.

    Input :

    Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith 
    point respectively.

    Output :

    Return an Integer, i.e minimum number of steps.
    Example :

    Input : [(0, 0), (1, 1), (1, 2)]
    Output : 2
    It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

    This question is intentionally left slightly vague. Clarify the question by trying out a few cases.

"""



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps_taken = []
        a_size = len(A)
        b_size = len(B)
        if b_size == a_size:
            if a_size > 1:
                for i in range(1, a_size):
                    x_steps = A[i] - A[i-1]
                    y_steps = B[i] - B[0]
                    max_steps = max(abs(x_steps), abs(y_steps))
                    steps_taken.append(max_steps)
            elif a_size == 1:
                x_steps = A[a_size -1] - A[0]
                y_steps = B[b_size -1] - B[0]
                max_steps = max(abs(x_steps), abs(y_steps))
                steps_taken.append(max_steps)
        return steps_taken
                    
                    
                    