class Solution {
    private static Set vowels = new HashSet<Character>(List.of('a','e','i','o','u'));

    public int maxFreqSum(String s) {
        Map<Character, Integer> vowelMap = new HashMap<>();
        Map<Character, Integer> consonantMap = new HashMap<>();
        char[] chars = s.toCharArray();


        int maxVowelCnt = 0;
        int maxConCnt = 0;
        for(char c : chars) {
            Map<Character, Integer> curMap = vowels.contains(c) ? vowelMap : consonantMap;
            Integer newCnt = curMap.getOrDefault(c, 0) + 1;
            curMap.put(c, newCnt);

            if(vowels.contains(c)) {
                maxVowelCnt = Math.max(maxVowelCnt, newCnt);
            } else {
                maxConCnt = Math.max(maxConCnt, newCnt);
            }

        }

        return maxVowelCnt + maxConCnt;
    }
}