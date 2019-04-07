class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        tmp = 0
        res = 0
        i = 0
        N = len(clips)
        curtmp = -1
        while i<N:
            if i==N-1:
                if clips[i][1]>=T:
                    res += 1
                    return res
                else:
                    return -1
            # i<N-1
            if clips[i][0]<=tmp:
                if clips[i+1][0]>tmp:
                    res += 1
                    curtmp = max(curtmp, clips[i][1])
                    tmp = curtmp
                    if tmp>=T:
                        return res
                    i += 1
                else:
                    i += 1
                    curtmp = max(curtmp, clips[i][1])
            else:
                if tmp>=T:
                    return res
                return -1
