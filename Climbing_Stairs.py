#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Note: Given n will be a positive integer.

class Solution {
    public int climbStairs(int n) {
        int[] arr = new int[n];
        if(n == 1){
            return 1;
        }
        arr[0] = 1;
        arr[1] = 2;
        
        int i = 2;
        while(i < n){
            arr[i] = arr[i-1] + arr[i-2];
            
            i++;
        }
        return arr[n-1];
    }
}
