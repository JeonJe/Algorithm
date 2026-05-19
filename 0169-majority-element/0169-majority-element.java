class Solution {
    public int majorityElement(int[] nums) {
        Map< Integer, Integer> count = new HashMap<>();

        for(int num : nums) {
            Integer c = count.getOrDefault(num, 0);
            count.put(num, c+1);
        }

        int majority = (int) Math.ceil((nums.length / count.size()));


        int answer = 0;
        int maxCount = 0;
        for(Map.Entry<Integer, Integer> kv : count.entrySet()) {
            if(kv.getValue() >= majority && kv.getValue() > maxCount) {
                maxCount = kv.getValue();
                answer = kv.getKey();
            }
        }

        return answer;


    }
}