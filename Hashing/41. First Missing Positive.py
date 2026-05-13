class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = set()
        for i in range(len(nums)):
            d.add(i+1)
        for i in nums:
            if i in d:
                d.remove(i)
        if d:
            for i in d:
                return i
        else:
            return len(nums) + 1