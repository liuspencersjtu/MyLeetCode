class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        
        tmp_res = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i+j] += int(num1[i])*int(num2[j])
        res = [0 for i in range(len(num1)+len(num2))]
        
        for i in range(len(num1)+len(num2)):
            res[i] = tmp_res[i] %10
            if i<len(num1)+len(num2)-1:
                tmp_res[i+1]+=tmp_res[i]//10
        return ''.join(str(i) for i in res[::-1]).lstrip('0')
