class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_index = {} 
        for i, num in enumerate(nums):
            if num in last_seen_index:
                last_index = last_seen_index[num]
                if (i - last_index) <= k:
                    return True
            last_seen_index[num] = i
        return False