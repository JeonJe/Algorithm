
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

class Solution {

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int minDepth = 0;
        Deque<Pair> queue = new ArrayDeque<>();
        queue.offer(new Pair(root, 1));

        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            TreeNode curNode = current.node;
            int depth = current.depth;
            if (curNode.left == null && curNode.right == null) {
                return depth;
            }
            if (curNode.left != null) {
                queue.offer(new Pair(curNode.left, depth + 1));
            }
            if (curNode.right != null) {
                queue.offer(new Pair(curNode.right, depth + 1));
            }

        }
        return minDepth;

    }

    public static class Pair {

        TreeNode node;
        int depth;

        public Pair(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}
