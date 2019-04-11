class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        strNum = 0
        positive = True
        if not str:
            return 0
        if str[0] == "-":
            positive = False
            str = str[1:]
        elif str[0] == "+":
            str = str[1:]
        
        for it in str:
            if '0'<=it<='9':
                strNum = strNum*10+ord(it)-ord('0')
            else:
                break
        
        if not positive:
            return max(-2**31, -strNum)
        else:
            return min(2**31-1, strNum)
