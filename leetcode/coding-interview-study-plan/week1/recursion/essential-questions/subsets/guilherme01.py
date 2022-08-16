class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        len_nums = len(nums)

        def subset_rec(sub_set):
            sub_set.sort()
            if tuple(sub_set) not in visited:
                visited.add(tuple(sub_set))
                if len(sub_set) == len_nums:
                    return
                else:
                    for n in nums:
                        if n not in sub_set:
                            subset_rec(sub_set + [n])

        subset_rec([])
        return visited