class MyHashMap {
    private static class Entry {
        int key;
        int value;
        Entry next;
        //파라미터와 변수 이름이 동일하면 값이 업데이트 X
        Entry(int k, int v, Entry n) {
            key = k;
            value = v;
            next = n;
        }
    }

    //소수 버킷 사이즈 사용으로 분포를 고르게 
    private Entry[] table;
    private static int SIZE = 769;

    public MyHashMap() {
        table = new Entry[SIZE];
    }

    private int idx(int key) {
        return Math.floorMod(key, SIZE);
    }

    public void put(int key, int value) {
        int i = idx(key);
        for (Entry e = table[i]; e != null; e = e.next) {
            if (e.key == key) {
                e.value = value;
                return;
            }
        }
        // head 추가
        table[i] = new Entry(key, value, table[i]);
    }

    public int get(int key) {
        int i = idx(key);

        for (Entry e = table[i]; e != null; e = e.next) {
            if (e.key == key) {
                return e.value;
            }
        }
        return -1;
    }

    public void remove(int key) {
        int i = idx(key);
        Entry prev = null; 
        Entry cur = table[i];

        while(cur != null) {
            if(cur.key == key) {
                if(prev == null) {
                    //table의 head를 업데이트
                    table[i] = cur.next;
                } else {
                    prev.next = cur.next;
                }
            }
            prev = cur;
            cur = cur.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */