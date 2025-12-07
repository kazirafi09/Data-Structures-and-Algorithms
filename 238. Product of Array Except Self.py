class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            answer[i] = pre
            pre *= nums[i]

        for i in range(n - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]

        return answer
