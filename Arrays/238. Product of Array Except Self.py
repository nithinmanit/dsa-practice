class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        suff = nums[-1]
        for i in range(n):
            if i == 0:
                res[i] = 1
            else:
                res[i] = nums[i-1] * res[i-1]
        for j in range(n):
            if j == 0:
                continue
            else:
                res[n-1-j] = suff * res[n-j-1]
                suff *= nums[n-j-1]
        return res