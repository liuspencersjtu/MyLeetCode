def check(A):    
            A.sort()
            cnts = [0] * 200010
            for x in A: cnts[x] += 1

            while A:
                x = A.pop()
                if cnts[x] == 0: continue
                cnts[x] -= 1
                if x % 2: return False
                hf = x // 2
                if cnts[hf] == 0: return False
                cnts[hf] -= 1
            return True
        
        pos, neg = [], []
        for x in A:
            if x >= 0: pos.append(x)
            else: neg.append(-x)
        return check(pos) and check(neg)
