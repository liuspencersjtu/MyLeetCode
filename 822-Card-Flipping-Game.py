class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        C = [i for i in zip(fronts,backs)]
        nums = [i for item in C for i in item]
        dic = {}
        for i in nums:
            dic[i] = True
        for item in C:
            if item[0] == item [1]:
                dic[item[0]] = False
        m = []
        for i in dic:
            if dic[i] == True:
                m.append(i)
        if m ==[]:
            return 0
        return min(m)
        '''
        dic ={}
        for i in C:
            a=i[0]
            dic[a] = 1
            for j in C:
                if not (j[0] == a and j[1] == a):
                    pass
                else:
                    dic[a] = 99999
            a=i[1]
            dic[a] = 1
            for j in C:
                if not (j[0] == a and j[1] == a):
                    pass
                else:
                    dic[a] = 99999
        m = []
        for i in dic:
            if dic[i] == 1:
                m.append(i)
        if m ==[]:
            return 0
        return min(m)
        '''