class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            Integer count = map.getOrDefault(nums[i], 0);
            map.put(nums[i], count + 1);
        }

        for(Map.Entry<Integer, Integer> e : map.entrySet()) {
            if(e.getValue() == 1) {
                return e.getKey();
            }
        }

        return 0;
    }
}