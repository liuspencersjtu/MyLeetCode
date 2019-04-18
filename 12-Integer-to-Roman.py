class Solution:
    def intToRoman(self, num: int) -> str:
        memo = {1000: 'M', 500: 'D',
               100: 'C', 50: 'L',
               10:'X', 5: 'V', 1: 'I'}
        res = []
        for it in [1000,100,10,1]:
            ##
            a = num//it
            num = num%it
            if a == 9:
                res.append(memo[it])
                res.append(memo[it*10])
            elif a==4:
                res.append(memo[it])
                res.append(memo[it*5])
            elif a==5:
                res.append(memo[it*5])
            elif a<4:
                res += [memo[it]]*a
            else:
                res.append(memo[it*5])
                res+=[memo[it]]*(a-5)
        return ''.join(res)
