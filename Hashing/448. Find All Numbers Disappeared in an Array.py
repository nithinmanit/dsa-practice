class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = set()
        for i in range(len(nums)):
            check.add(i+1)
        for i in nums:
            if i in check:
                check.remove(i)
        return list(i for i in check)