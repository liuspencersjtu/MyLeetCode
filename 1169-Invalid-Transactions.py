class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        queue = []
        res = set()
        transactions = [it.split(',') for it in transactions]
        transactions.sort(key=lambda x: int(x[1]))
        for trans in transactions:
            while queue and int(queue[0][1])<int(trans[1])-60:
                queue.pop(0)
            for his in queue:
                if his[0]==trans[0] and his[3]!=trans[3]:
                    res.add(','.join(his))
                    res.add(','.join(trans))
            if int(trans[2])>1000:
                res.add(','.join(trans))
            queue.append(trans)
        return list(res)
                    
