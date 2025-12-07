class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        not_dup = set()
        for num in nums:
            if num in not_dup:
                return True
            else:
                not_dup.add(num)
        return result