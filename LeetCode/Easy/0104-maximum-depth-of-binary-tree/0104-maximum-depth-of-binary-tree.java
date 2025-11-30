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
 import java.util.*;
 import java.io.*;

class Solution {
    public static int answer = 0;
    public int maxDepth(TreeNode root) {
        answer = 0;
        if(root == null) {
            return 0;
        }

        dfs(root, 1);
        return answer;

    }

    private void dfs(TreeNode current, int depth) {
        if(depth > answer) {
            answer = depth;
        }

        if(current.left != null) {
            dfs(current.left , depth+1);
        }
        
        if(current.right != null) {
            dfs(current.right, depth+1);
        } 
    }


}