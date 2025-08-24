class MyHashSet {
    private static final int SIZE = 769;
    private final List<Integer>[] buckets;

    public MyHashSet() {
        buckets = new List[SIZE];
        for(int i = 0; i < SIZE; i++) {
            buckets[i] = new LinkedList<>();
        }
    }

    private int hash(int key) {
        return key % SIZE;
    }
    
    public void add(int key) {
        int i = hash(key);
        List<Integer> bucket = buckets[i];
        for(int x : bucket) {
            if(x == key) {
                return ;
            }
        }
        bucket.add(key);
    }
    
    public void remove(int key) {
        int i = hash(key);
        Iterator<Integer> it = buckets[i].iterator();
        while(it.hasNext()) {
            if(it.next() == key) {
                it.remove();
                return ;
            }
        }
    }
    
    public boolean contains(int key) {
        int i = hash(key);
        List<Integer> bucket = buckets[i];

        for(int x : bucket) {
            if(x == key) {
                return true;
            }
        }
        return false;
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */