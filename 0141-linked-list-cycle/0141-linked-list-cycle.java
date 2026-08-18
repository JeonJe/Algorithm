/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.HashSet;
import java.util.Set;

class Solution {

    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();
        ListNode cur = head;

        while(cur != null) {
            if(set.contains(cur)) {
                return true;
            }
            set.add(cur);
            cur = cur.next;
        }
        return false;
    }

}
