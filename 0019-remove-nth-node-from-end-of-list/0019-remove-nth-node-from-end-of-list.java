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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode current = head;
        int size = 0;
        while(current != null){
            size++;
            current = current.next;
        }
        
        int targetIndex = size - n;
        
        if(targetIndex == 0){
            return head.next;
        }
        
        current = head;
        for(int i = 0 ; i < targetIndex-1; i++){
            current = current.next;    
        }
        
        current.next = current.next.next;
        
        return head;
    }
}