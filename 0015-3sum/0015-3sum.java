import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[] nums = {-1, 0, 1, 2, -1, -4};
        System.out.println(new Solution().threeSum(nums));
    }

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> answer = new ArrayList<>();

        int n = nums.length;

        Arrays.sort(nums);

        //하나 고정
        for (int x = 0; x < n - 2; x++) {
            if (x > 0 && nums[x] == nums[x - 1]) {
                continue;
            }

            int left = x + 1;
            int right = n - 1;

            //안에서 투썸
            while (left < right) {
                if (nums[left] + nums[right] + nums[x] == 0) {
                    answer.add(Arrays.asList(nums[x], nums[left], nums[right]));

                    //left가 다음으로 움직일 수 있으면서 다음 수가 현재 값이랑 같으면 넘어감
                    while (left + 1 < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left + 1 < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (nums[left] + nums[right] + nums[x] < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return answer;
    }
}
