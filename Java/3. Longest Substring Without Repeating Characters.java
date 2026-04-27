class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int minimum_subarray_size = Integer.MAX_VALUE; 
        int total = 0;

        while (right < nums.length) {
            total += nums[right];
            right += 1;
            
            while (total >= target) {
                int window_length = (right - left);
                if (window_length < minimum_subarray_size) {
                    minimum_subarray_size = window_length;
                }
                total -= nums[left];
                left += 1;
            }
        }

        if (minimum_subarray_size == Integer.MAX_VALUE) {
            return 0;
        }
        return minimum_subarray_size;
    }
}