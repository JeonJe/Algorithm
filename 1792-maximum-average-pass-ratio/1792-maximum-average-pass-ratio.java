class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        //합격 증가률 기준으로 maxHeap
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));

        //pq에 합격률 증가율 기준으로 값 입력 
        for(int[] c : classes) {
            int pass = c[0];
            int total = c[1];
            pq.offer(new double[]{gain(pass, total), pass, total});
        }

        //extraStudent를 추가하여 pq에 다시 추가 
        for(int i = 0; i < extraStudents; i++) {
            double[] cur = pq.poll();
            int newPass = (int) cur[1] + 1;
            int newTotal = (int) cur[2] + 1;
            pq.offer(new double[]{gain(newPass, newTotal), newPass, newTotal});
        }

        //average pass ratio 계산
        double sum = 0.0;

        for(double[] e : pq) {
            int pass = (int) e[1];
            int total = (int) e[2];
            sum += (double) pass / total; 
        }
        
        return sum / pq.size();
    }

    //학생 1명이 추가되었을 때 그 반의 합격 증가률 
    private static double gain(int p, int t) {
        // (p+1)/(t+1) - p/t와 동일
        return (t - p) / (double)(t * (long)(t + 1));
    }
}