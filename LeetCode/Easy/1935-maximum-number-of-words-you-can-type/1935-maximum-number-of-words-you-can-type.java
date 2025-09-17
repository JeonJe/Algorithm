class Solution {

    public int canBeTypedWords(String text, String brokenLetters) {
        HashSet<Character> brokens = new HashSet<>();
        String[] words = text.split(" ");
        
        for(char bl : brokenLetters.toCharArray()) {
            brokens.add(bl);
        }

        int answer = 0;
        for(String word : words) {
            if(isFull(word, brokens)) {
                answer++;
            }
        }

        return answer;
        
    }

    private boolean isFull(String word, HashSet s) {

        for(char w : word.toCharArray()) {
            if(s.contains(w)) {
                return false;
            }
        }
        return true;

    }
}