class Solution:
    def combine(self, n: int, k: int):
        soln = []
        sub = []

        def backtrack(last: int):
            if len(sub) == k:
                soln.append(sub.copy())

            if last > n:
                return

            for i in range(last, n + 1):
                sub.append(i)
                backtrack(i + 1)
                sub.pop()

        backtrack(1)

        return soln

print(Solution().combine(4,3))