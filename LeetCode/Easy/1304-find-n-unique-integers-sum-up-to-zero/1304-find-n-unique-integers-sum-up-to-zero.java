class Solution {
    public int[] sumZero(int n) {
        int[] array = new int[n];
        Arrays.fill(array, 0);

        for (int i = 0; i < n - 1; i += 2) {
            array[i] = i + 1;
            array[i + 1] = -1 * (i + 1);

        }
        if (n % 2 != 0) {
            array[n - 1] = 0;

        }

        return array;
    }
}