class Solution {
    public List<String> commonChars(String[] words) {
        int[] alpha = new int[26];
        Arrays.fill(alpha, Integer.MAX_VALUE);

        for(String word: words){
            int[] freqInWord = new int[26];
            for (char c : word.toCharArray()) {
                freqInWord[c - 'a']++;
            }
            for (int i = 0 ; i < 26; i++){
                alpha[i] = Math.min(alpha[i], freqInWord[i]);
            }
        }
        List<String> answer = new ArrayList<>();
        for(int i = 0 ; i < 26; i++) {
            for(int j  = 0; j < alpha[i]; j++){
                answer.add(Character.toString(('a' + i)));
            }
        }
        return answer;
    }
}