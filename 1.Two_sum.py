class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(0, len(nums)):   
            remainder = target - nums[i]
            if remainder in temp:
                return [i, temp[remainder]]
            else:
                temp[nums[i]] = i
