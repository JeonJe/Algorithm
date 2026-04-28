class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        
        int rcnt = 0;
        
        int n = words.length;
        // startIndex 에서 오른쪽으로 진행 , -> target 찾을때까지 
        for(int i = 0; i < n; i++) {
            if(target.equals(words[(startIndex + i) % n])) {
                break;
            }
            rcnt++;
        }


        int lcnt = 0;
        // startIndex에서 왼쪽으로 진행 -> target을 찾을때까지 
        for(int i = 0; i < n; i++) {
            if(target.equals(words[(startIndex - i + n) %n])) {
                break;
            }
            lcnt++;
        }


        // 오른쪽, 왼쪽 모두 배열의 길이만큼 확인 -> 없음 
        if(rcnt == n && lcnt == n) {
            return -1;
        }
        return Math.min(rcnt, lcnt);
    }
}