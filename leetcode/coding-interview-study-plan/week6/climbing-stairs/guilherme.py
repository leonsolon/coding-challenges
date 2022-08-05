from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        max_steps_2 = n // 2

        possib = 0
        for step_2 in range(0, max_steps_2 + 1):
            step_1 = n - 2 * step_2
            possib += factorial(step_1 + step_2) / (factorial(step_1) * factorial(step_2))
            # print(step_1,step_2, possib)

        return int(possib)