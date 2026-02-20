class Solution {
    public List<String> commonChars(String[] words) {
          int numOfAlphabet = 26;
        int[] freqCharInWords = new int[numOfAlphabet];
        Arrays.fill(freqCharInWords, Integer.MAX_VALUE);

        for(int i = 0; i < words.length; i++){
            int[] freqCharInAlpha = new int[numOfAlphabet];
            Arrays.fill(freqCharInAlpha, 0);

            for(char c : words[i].toCharArray()){
                int charToInt = (int)(c -'a');
                freqCharInAlpha[charToInt]++;
            }

            for(int j = 0 ; j < freqCharInAlpha.length; j++){
                freqCharInWords[j] = Math.min(freqCharInWords[j], freqCharInAlpha[j]);
            }
        }
        List<String> answer = new ArrayList<>();
        for(int i = 0 ; i < numOfAlphabet; i++ ){
            if(freqCharInWords[i] > 0) {
                while(freqCharInWords[i] > 0){
                    answer.add( Character.toString (i + 'a'));
                    freqCharInWords[i]--;
                }

            }
        }
        return answer;
    }
}