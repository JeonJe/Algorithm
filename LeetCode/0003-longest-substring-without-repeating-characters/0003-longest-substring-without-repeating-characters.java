class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int longestSubStringLength = 0;

        for (int right = 0; right < s.length(); right++) {
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }
            charSet.add(s.charAt(right));
            longestSubStringLength = Math.max(longestSubStringLength, right - left + 1);
        }
        return longestSubStringLength;
    }
}