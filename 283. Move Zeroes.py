class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fp = 0
        for sp in range(len(nums)):
            if nums[sp] != 0:
                nums[fp], nums[sp] = nums[sp], nums[fp]
                fp += 1
        return nums
