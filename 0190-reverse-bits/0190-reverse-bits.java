
// class Solution {
//     public int reverseBits(int n) {

//         int answer = 0;
//         for (int i = 0; i < 32; i++) {
//             int bitFlag = (n >> i) & 1;
//             answer += (bitFlag << (31 - i));
//         }
//         return answer;
//     }
// }
class Solution {
    public int reverseBits(int n) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<>();

        for(int i = 0; i<32; i++) {
            stack.add(n % 2);
            n /= 2;
        }

        int j = 0;
        while(!stack.isEmpty()) {
            int bit = stack.getLast();
            stack.removeLast();
            answer += bit * Math.pow(2, j); 
            j += 1;
        }

        return answer;       
    }
}