class Solution: # Estourou memória
    def climbStairs(self, n: int) -> int:
        possib_steps = []

        def next_step(steps, gap):
            if gap >= 1:
                step1 = steps + [1]
                gap1 = gap - 1
                next_step(step1, gap1)
                if gap >= 2:
                    step2 = steps + [2]
                    gap2 = gap - 2
                    next_step(step2, gap2)
            elif gap == 0:
                possib_steps.append(steps)

        next_step([], n)
        return len(possib_steps)