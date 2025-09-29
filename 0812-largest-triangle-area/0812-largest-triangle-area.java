class Solution {
    public double largestTriangleArea(int[][] points) {
        double answer = 0;
        int n = points.length;

        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                for(int k = j+1; k < n; k++) {
                    answer = Math.max(answer, getArea(points, i, j, k));
                }
            }
        }

        return answer / 2.0;
        
    }

    public long getArea(int[][] points, int i, int j, int k) {
        int[] a = points[i];
        int[] b = points[j];
        int[] c = points[k];

        long ux = b[0] - a[0];
        long uy = b[1] - a[1];
        long vx = c[0] - a[0];
        long vy = c[1] - a[1];

        return Math.abs(ux * vy - uy * vx);

    }
}