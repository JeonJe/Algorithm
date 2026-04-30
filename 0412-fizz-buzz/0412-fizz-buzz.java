class Solution {
    public List<String> fizzBuzz(int n) {

        // String[] answer = new String[n + 1];
        List<String> answer = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                // answer[i] = "FizzBuzz";
                answer.add("FizzBuzz");
            } else if (i % 3 == 0) {
                // answer[i] = "Fizz";
                answer.add("Fizz");
            } else if (i % 5 == 0) {
                // answer[i] = "Buzz";
                answer.add("Buzz");
            } else {
                // answer[i] = String.valueOf(i);
                answer.add(String.valueOf(i));
            }
        }

        return answer;

    }
}