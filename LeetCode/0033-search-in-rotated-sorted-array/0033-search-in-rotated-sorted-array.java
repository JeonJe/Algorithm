class Solution {
    public int search(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target) {
                return mid;
            }

            //left부터 mid까지 정렬된 경우
            if(nums[left] <= nums[mid]){
                //찾으려는 값이 더 왼쪽에 있거나 , 왼쪽에서 더 찾을 수 없을 때
                if(target < nums[left]  || target > nums[mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                //찾으려는 값이 더 오른쪽에 있거나 , 오른쪽에서 더 찾을 수 없을 때
                if(target > nums[right] || target < nums[mid] ) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
}