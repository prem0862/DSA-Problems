
# Problems: https://www.interviewbit.com/problems/redundant-braces/



class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        push_set = set(["(", "+", "-", "*", "/"])
        stack = []
        for item in A:
            # push parenthesis and operators to the stack till it encounters closing braces
            if item in push_set:
                stack.append(item)
            elif item == ")":
                top_element = stack.pop()
                # if the immediate pop has opening braces then it contains redundent braces
                if top_element != "(":
                    stack.pop()
                else:
                    return 1
        return 0
