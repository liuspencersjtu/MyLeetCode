class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        tmp = []
        cnt = K
        def pop(lst):
            nonlocal cnt
            while lst and lst[0] == 1:
                lst.pop(0)
            if lst and lst[0] == 0:
                lst.pop(0)
                cnt += 1
            

        longest = 0
        length = 0
        for i in A:
            if i == 1:
                tmp.append(i)
                length += 1
                longest = max(longest, length)
            else:
                if cnt>0:
                    tmp.append(i)
                    length += 1
                    cnt-=1
                else:
                    pop(tmp)
                    length = len(tmp)
                    if cnt>0:
                        tmp.append(i)
                        length += 1
                        cnt -= 1
                longest = max(longest, length)
        return longest
