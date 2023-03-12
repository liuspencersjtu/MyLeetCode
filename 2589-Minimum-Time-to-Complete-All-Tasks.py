class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        visited = set()
        tasks.sort(key=lambda x:[x[1]]) # prioritize task which most close to end
        for i, task in enumerate(tasks):
            s, e, d = task
            j = e
            while d>0:
                if j not in visited:
                    d -= 1
                    visited.add(j)
                    for k in range(i+1, len(tasks)):# since the task is not sorted by start, we have to go through all the tasks behind
                        if tasks[k][0]<=j and tasks[k][2]>0:# since this time is already used, we deduct every task that can run simultaneously
                            tasks[k][2]-=1
                j -= 1
        return len(visited) 
