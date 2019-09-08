
# Problem: https://www.interviewbit.com/problems/generate-all-parentheses/



class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        # create an empty stack
        stack = []
        for item in A:
            if item in set(["(", "{", "["]):
                stack.append(item)
            else:
                if len(stack) == 0:
                    return 0
                if item == ")":
                    if stack.pop() != "(":
                        return 0
                elif item == "}":
                    if stack.pop() != "{":
                        return 0
                elif item == "]":
                    if stack.pop() != "[":
                        return 0
                        
        # check if stack is empty
        if len(stack):
            return 0
        else:
            return 1
