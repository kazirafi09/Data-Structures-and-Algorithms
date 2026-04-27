class Solution {
    public int maxProduct(int[] nums) {
        int max = Integer.MIN_VALUE;
        int left = 0;
        int right = 0;
        int current = nums[left];
        while (left <= right){
            if (nums.length == 1){
                return nums[0];
            }
            if (current >= max) {
                right += 1;
                current *= nums[right];
                if (current > max){
                    max = current;
                }
            } else if (current < max) {
                current = current / nums[left];
                left += 1;
            }
        }
        return max;
    }
}

//not correct