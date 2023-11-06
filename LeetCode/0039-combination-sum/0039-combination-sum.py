class Solution:
    def combinationSum(self, candidates, target):
        def dfs(path, sum_path):
            if sum_path == target:
                sorted_path = path[:]
                sorted_path.sort()
                if sorted_path not in answer:
                    answer.append(sorted_path)
                return

            if sum_path > target:
                return

            for i in range(len(candidates)):
                if (sum_path + candidates[i] <= target):
                    path.append(candidates[i])
                    dfs(path, sum_path + candidates[i])
                    path.pop()

        answer = []
        dfs([], 0)
        return list(answer)