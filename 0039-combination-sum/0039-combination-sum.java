import java.util.*;

class Solution {
    private List<List<Integer>> answer;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        answer = new ArrayList<>();

        Arrays.sort(candidates);

        List<Integer> bucket = new ArrayList<>();
        int curSum = 0;

        dfs(candidates, bucket, curSum, target, 0);

        for (List<Integer> integers : answer) {
            for (Integer integer : integers) {
                System.out.print(integer + " ");
            }
            System.out.println();

        }
        return answer;
    }

    private void dfs(int[] candidates, List<Integer> bucket, int curSum, int target, int start) {
        if (curSum == target) {
            answer.add(new ArrayList<>(bucket));
            return;
        }
        if (curSum > target) return;

        for (int i = start; i < candidates.length; i++) {
            bucket.add(candidates[i]);
            dfs(candidates, bucket, curSum + candidates[i], target, i);
            bucket.removeLast();
        }

    }
}
