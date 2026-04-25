class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int[] numbers = new int[nums.length];
        int index = nums.length - 1;
        while (left <= right){
            if (nums[right] * nums[right] > nums[left] * nums[left]){
                numbers[index] = nums[right] * nums[right];
                right -= 1;
                index -= 1;
            } else{
                numbers[index] = nums[left] * nums[left];
                left += 1;
                index -= 1;
            }
        }
        return numbers;
    }
}