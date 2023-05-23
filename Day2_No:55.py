class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        left = nums[0]
        i = 1
        while left>0:
            if i == len(nums)-1:
                return True
            left = max(left-1,nums[i])
            i += 1
        return False
