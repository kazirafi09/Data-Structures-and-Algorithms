class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        total_combinations = []
        duplicates = set()
        
        for i in range(len(nums) - 2):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
                
                l = i + 1
                r = len(nums) - 1
                
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    
                    if total > 0:
                        r -= 1
                    elif total < 0:
                        l += 1
                    else: 
                        total_combinations.append([nums[i], nums[l], nums[r]])
                    
                        l += 1
                        r -= 1
                    
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                            
        return total_combinations