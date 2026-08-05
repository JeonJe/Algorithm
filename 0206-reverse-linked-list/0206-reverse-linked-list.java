import java.util.*;

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) {
            return null;
        }

        ListNode prev = null;
        ListNode cur = head;

        while(cur != null) {

            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }

        return prev;

    }
}
