import java.util.*;

class Solution {
    private static char[] vowel = {'A', 'E', 'I', 'O', 'U'};
    private static String target;
    private static int counter = -1;
    private static int answer;

    public int solution(String word) {

        //길이가 1부터 5까지, A부터 U까지 완탐
        ArrayList<Character> current = new ArrayList<>();
        target = word;
        dfs(current, 0);

        return answer;
    }


    //완탐
    private static void dfs(ArrayList<Character> current, int depth) {
        counter++;
        if (target.length() == current.size()) {
            if (isSame(current)) {
                answer = counter;
                return;
            }
        }
        if (depth == 5) {
            return;
        }
        for (char c : vowel) {
            current.add(c);
            dfs(current, depth + 1);
            current.remove(current.size() - 1);
        }
    }

    private static boolean isSame(ArrayList<Character> current) {
        for (int i = 0; i < target.length(); i++) {
            if (target.charAt(i) != current.get(i)) {
                return false;
            }
        }
        return true;
    }

}
