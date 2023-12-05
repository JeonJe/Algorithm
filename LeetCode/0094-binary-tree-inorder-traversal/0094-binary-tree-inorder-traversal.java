/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> answer = new ArrayList<>();
        inroder(root, answer);
        return answer;
    }
    private void inroder(TreeNode cur, List<Integer> list){
        if (cur == null) {
            return;
        } else {
            inroder(cur.left, list);
            list.add(cur.val);
            inroder(cur.right, list);
        }
        
    }
}