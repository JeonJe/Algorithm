class MyLinkedList {

    public static class Node {
       int value;
        Node next;
        public Node(int v) {
            value = v;
        }
    }

    private final Node head;
    private int size;

    public MyLinkedList() {
        head = new Node(0);
        size = 0;
    }
    
    public int get(int index) {
        if(index < 0 || index >= size) {
            return -1;
        }
        Node cur = head.next;
        for(int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur.value;
        
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0|| index > size) {
            return ;
        }
        Node prev = head;
        for(int i = 0; i < index; i++) {
            prev = prev.next;
        }
        Node n = new Node(val);
        n.next = prev.next;
        prev.next = n;
        size++;
        
    }
    
    public void deleteAtIndex(int index) {
        if(index < 0|| index >= size) {
            return ;
        }
        Node prev = head;
        for(int i = 0; i < index; i++) {
            prev = prev.next;
        }
        prev.next = prev.next.next;
        size--;
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */