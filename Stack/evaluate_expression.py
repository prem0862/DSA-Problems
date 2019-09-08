

# Problem: https://www.interviewbit.com/problems/evaluate-expression/



class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        operators = set(["+", "-", "*", "/"])
        for item in A:
            # push item to stack until we found any operators
            if item not in operators:
                stack.append(item)
            else:
                opr1 = int(stack.pop())
                opr2 = int(stack.pop())
                # perform the operation on two operands
                if item == "+":
                    stack.append(opr2 + opr1)
                elif item == "-":
                    stack.append(opr2 - opr1)
                elif item == "*":
                    stack.append(opr2 * opr1)
                elif item == "/":
                    stack.append(opr2 / opr1)
        
        result = int(stack.pop())
        return result
