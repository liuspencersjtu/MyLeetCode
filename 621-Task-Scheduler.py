class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = collections.Counter(tasks)
        part_count = max(d.values()) - 1
        empty_slots = part_count * (n-(len([i for i in d.values() if i == max(d.values())])-1))
        available_tasks = len(tasks) - len([i for i in d.values() if i == max(d.values())]) * max(d.values())
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles
        
