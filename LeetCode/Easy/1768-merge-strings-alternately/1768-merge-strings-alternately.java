class Solution {
  public String mergeAlternately(String word1, String word2) {
    int i = 0;
    int k = 0;

    StringBuilder sb = new StringBuilder();
    while(i < word1.length() && k < word2.length()) {
      sb.append(word1.charAt(i));
      sb.append(word2.charAt(k));
      i++;
      k++;
    }

    while(i < word1.length()) {
      sb.append(word1.charAt(i));
      i++;
    }
    while(k < word2.length()) {
      sb.append(word2.charAt(k));
      k++;
    }

    return sb.toString();
  }
}
