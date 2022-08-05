from bisect import insort # Falhou em 1 dos 171 casos


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        possibilities = set()
        dict_comb = {}
        for c in candidates:
            dict_comb[c] = 0

        def add_one_number(combination, sum_dict):
            diff = target - sum_dict
            if diff < 0:
                return
            # print(diff, sum_dict, combination)
            for c in candidates:
                combination[c] += 1
                if c == diff:
                    unique_comb = []
                    for k, v in combination.items():
                        unique_comb += [k] * v
                    possibilities.add(tuple(unique_comb))
                elif c < diff:
                    # print(sum_dict, c)
                    add_one_number(combination, sum_dict + c)
                combination[c] -= 1

        add_one_number(dict_comb.copy(), 0)
        return possibilities