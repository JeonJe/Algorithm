/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) {
            return null;
        }

        ListNode cur = head;

        ArrayList<Integer> temp = new ArrayList<>();
        while(cur != null) {
            temp.add(cur.val);
            cur = cur.next;
        }

        Collections.reverse(temp);

        ListNode newCur = new ListNode(temp.get(0));
        ListNode newHead = newCur;
        for(int i = 1 ; i < temp.size(); i++) {
            newCur.next = new ListNode(temp.get(i));
            newCur = newCur.next;
        }

        return newHead;
    }
}