class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = list(A)
        b = list(B)
        n = len(a)
        if len(b) != n:
            return False
        diff = 0
        place = []
        for i in range(n):
            if a[i] != b[i]:
                diff += 1
                place.append(i)
        if diff == 2:
            if a[place[0]] == b[place[1]] and a[place[1]] == b[place[0]]:
                return True
        if diff == 0:
            if len(set(a))<n:
                return True
        return False