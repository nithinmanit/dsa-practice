#283. Move Zeroes
#Not as optimal as the standard solution.
#Classic Two pointers
#Easy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if 0 not in nums:
            return
        for i in range(len(nums)):
            if nums[j] == 0 and nums[i] != 0 and i > j:
                nums[j] = nums[i]
                nums[i] = 0
                j += 1
            else:
                continue