from collections import Counter
# Runtime: 727 ms, faster than 58.20% of Python3 online submissions for Task Scheduler.
# Memory Usage: 14.3 MB, less than 90.70% of Python3 online submissions for Task Scheduler.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count_tasks = Counter(tasks)
        i = 0
        time = 0
        while i < len(tasks):
            tasks_sorted = sorted(count_tasks.items(), key=lambda x: x[1], reverse=True)
            for j in range(0, n + 1):
                time += 1
                if j < len(tasks_sorted) and count_tasks[tasks_sorted[j][0]] > 0:
                    count_tasks[tasks_sorted[j][0]] -= 1
                    i += 1
                    if i >= len(tasks):
                        break
            # print(i, time, count_tasks)

        return time


