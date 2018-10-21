class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name)==1:
            for i in typed:
                if i != name:
                    return False
            return True
        p1,p2 = 0,0
        l1 = len(name)-1
        l2 = len(typed)-1
        while p1<l1:
            if name[p1+1]!=name[p1]:
                if p2>=l2 or name[p1]!=typed[p2]:
                    print(p1,p2,1)
                    return False
                p1+=1
                p2+=1
                while p2<l2 and typed[p2]==typed[p2-1]:
                    p2+=1
            else:
                if p2>=l2 or name[p1+1]!=typed[p2+1]:
                    print(p1,p2,2,l1)
                    return False
                p1+=1
                p2+=1
        print(p1)   
        for i in typed[p2:]:
            if i != name[p1]:
                print(p1,p2)
                return False
        return True
            