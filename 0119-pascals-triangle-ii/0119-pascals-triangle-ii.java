class Solution {
    public List<Integer> getRow(int rowIndex) {

        int[] arr = new int[34];
        for (int i = 0; i < 34; i++) {
            arr[i] = 1;
        }

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < 34; i++) {
            for (int j = i - 1; j > 0; j--) {
                arr[j] = arr[j - 1] + arr[j];
            }

            if (rowIndex == i) {
                for (int z = 0; z <= rowIndex; z++) {
                    answer.add(arr[z]);
                }

                return answer;
            }
        }
        return null;

    }
}