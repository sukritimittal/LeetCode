#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        if(n == 0){
            return 0;
        }
        arr[n-1] = nums[n-1];
        if(n == 1){
            return arr[n-1];
        }
        arr[n-2] = Math.max(nums[n-2], nums[n-1]);
        int i = n-3;
        while(i>=0){
            arr[i] = Math.max(nums[i] + arr[i+2], arr[i+1]);
            i--;
        }
        return arr[0];
        
    }
}
