from bisect import insort # Falhou em 1 dos 171 casos


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        possibilities = set()
        visited = set()

        def add_one_number(combination, new_el, soma):
            if new_el != None:
                insort(combination, new_el)
            combination_t = tuple(combination)
            if combination_t not in visited:
                visited.add(combination_t)
                if soma == target:
                    possibilities.add(tuple(combination))
                else:
                    diff = target - soma
                    if diff <0:
                        return
                    # print(diff, combination)
                    for c in candidates:
                        if c <= diff:
                            add_one_number(combination.copy(), c, soma + c)

        add_one_number([], None, 0)
        return possibilities

