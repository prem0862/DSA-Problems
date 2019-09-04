
# Problem: https://www.interviewbit.com/problems/implement-strstr/




class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if A == B: return 0
        string = A
        sub_str = B
        str_len = len(string)
        sub_str_len = len(sub_str)
        
        for i in range(0, str_len):
            if string[i] == sub_str[0] and (str_len - i) > sub_str_len:
                str_ind = i
                for j in range(0, sub_str_len):
                    if string[str_ind] != sub_str[j]:
                        break
                    str_ind += 1
        
                if (str_ind - i == sub_str_len):
                    return i
        return -1
