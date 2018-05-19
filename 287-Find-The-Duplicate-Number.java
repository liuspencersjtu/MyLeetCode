class Solution {
    public int findDuplicate(int[] nums) {
        int l = nums.length;
        for (int i = 0; i < l; i++){
            int item = nums[i];
            for (int k = i+1;k<l;k++){
                if (nums[k] == item){
                    return item;
                }
            }
        }
        return -1;
    }
}