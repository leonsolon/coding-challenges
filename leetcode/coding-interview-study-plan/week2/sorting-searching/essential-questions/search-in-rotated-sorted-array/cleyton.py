#120'


# Runtime: 105 ms, faster than 5.45% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.3 MB, less than 56.61% of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:
    def search(self, nums, target):
        n = len(nums)
        beg = 0
        end = n - 1

        while beg < end:
            mid = (end - beg) // 2 + beg
            if nums[mid] > nums[end]:
                beg = mid + 1
            else:
                end = mid

        k = beg # beg == end

        beg = 0
        end = n - 1

        while beg <= end:
            mid = (end - beg) // 2 + beg
            rot_mid = (mid + k) % n
            if target == nums[rot_mid]:
                return rot_mid
            if target > nums[rot_mid]:
                beg = mid + 1
            else:
                end = end - 1

        return -1


search([7,1,2,3,4,5,6],2)
search([4,5,6,7,0,1,2],1)
search([4,5,6,7,0,1,2],0)
search([3,1],3)
search([1,3],3)

search([4,5,6,7,0,1,2],0)

search([3,4,5,6,7,0,1,2],3)
search([1,2,3,4,5],3)
search([1,2,3,4],3)


