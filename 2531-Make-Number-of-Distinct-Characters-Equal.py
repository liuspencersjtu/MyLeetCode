class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        from collections import Counter
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        # if abs(len(cnt1.keys())-len(cnt2.keys()))>=2:
        #     return False
        for k1 in cnt1:
            for k2 in cnt2:
                if k1 == k2:
                    if len(cnt1)==len(cnt2):
                        return True
                    continue
                t1, t2 = len(cnt1), len(cnt2)
                # swicth k1 and k2
                if cnt1[k1]==1:
                    t1 -= 1
                if cnt2[k2]==1:
                    t2 -= 1
                if k1 not in cnt2:
                    t2 += 1
                if k2 not in cnt1:
                    t1 += 1
                if t1==t2:
                    return True
        return False
