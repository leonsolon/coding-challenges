class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrackMe(i,temp):
            if i==len(nums):
                ans.append(temp.copy())
                return
            else:
                backtrackMe(i+1,temp+[nums[i]])
                backtrackMe(i+1,temp)
        backtrackMe(0,[])
        return ans