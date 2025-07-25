class Solution {
    public int[] sortedSquares(int[] nums) {

        int n=nums.length;
        int[] arr=new int[n];
        int left=0;
        int right=n-1;
        int index=n-1;

        while(left<=right){
            int left_ans=nums[left]*nums[left];
            int right_ans=nums[right]*nums[right];

            if(left_ans>right_ans){
                arr[index]=left_ans;
                left++;
                index--;
            }
            else{
                arr[index]=right_ans;
                index--;
                right--;
            }
        }
        return arr;
        
    }
}
