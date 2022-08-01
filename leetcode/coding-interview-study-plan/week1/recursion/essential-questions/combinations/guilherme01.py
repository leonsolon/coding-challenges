class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if k==1:
            ans = []
            for i in range(1, n+1):
                ans.append([i])
            return ans
        if k>1:
            ans = []
            for el1 in Solution().combine(n,1):
                for el2 in Solution().combine(n, k-1):
                    if el1[0] not in el2:
                        new_el = el1 + el2
                        new_el.sort()
                        if new_el not in ans:
                            ans.append(new_el)

            return ans