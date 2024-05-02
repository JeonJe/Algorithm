class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();  
        dfs(0, 0, new ArrayList<>(), candidates, target, answer);
        return answer;
    }

    private void dfs(int depth, int sum, List<Integer> path, int[] candidates, int target, List<List<Integer>> answer) {
        if (sum > target) {
            return;
        }
        if(sum == target){
            answer.add(new ArrayList<>(path));
            return;
        }

        for(int i = depth; i < candidates.length; i++) {
            path.add(candidates[i]);
            dfs(i, sum + candidates[i], path, candidates, target, answer); 
            path.remove(path.size() - 1);  
        }
    }
}