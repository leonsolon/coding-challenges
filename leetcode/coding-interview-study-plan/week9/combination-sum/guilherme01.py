from bisect import insort # Falhou em 1 dos 171 casos


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        possibilities = set()

        def add_one_number(combination):
            diff = target - sum(combination)
            if diff <0:
                return
            # print(diff, combination)
            for c in candidates:
                if c == diff:
                    new_comb = combination + [c]
                    new_comb.sort()
                    possibilities.add(tuple(new_comb))
                elif c < diff:
                    add_one_number(combination + [c])

        add_one_number([])
        return possibilities