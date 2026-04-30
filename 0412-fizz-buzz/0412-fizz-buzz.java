class Solution {
    public List<String> fizzBuzz(int n) {

        String[] answer = new String[n + 1];

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                answer[i] = "FizzBuzz";
            } else if (i % 3 == 0) {
                answer[i] = "Fizz";
            } else if (i % 5 == 0) {
                answer[i] = "Buzz";
            } else {
                answer[i] = String.valueOf(i);
            }
        }

        return Arrays.stream(answer)
                .filter(s -> s != null)
                .toList();

    }
}