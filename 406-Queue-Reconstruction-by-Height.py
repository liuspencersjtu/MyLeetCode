class Solution:
    def __init__(self):
        self.memo = {}
        
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort()
        a = people.pop(0)
        t = 0
        if self.memo.get(a[0],-1)==-1:
            self.memo[a[0]]=0
        else:
            self.memo[a[0]]+=1
            t = self.memo[a[0]]
        print(a)
        i = 0
        n = len(people)
        while i<n and people[i][0] == a[0]:
            people[i][1]-=1
            i+=1
        queue = self.reconstructQueue(people)
        queue.insert(a[1],a)
        queue[a[1]][1]+=t
        return queue
