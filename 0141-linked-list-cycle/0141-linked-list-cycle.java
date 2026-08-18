import java.util.HashSet;
import java.util.Set;

class Solution {

    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = null;
        if (head.next != null) {
            fast = head.next.next;
        }

        while (fast != null) {
            if (fast == slow) {
                return true;
            }

            slow = slow.next;

            if (fast.next != null && fast.next.next != null) {
                fast = fast.next.next;
            } else {
                return false;
            }

        }
        return false;
    }

}
