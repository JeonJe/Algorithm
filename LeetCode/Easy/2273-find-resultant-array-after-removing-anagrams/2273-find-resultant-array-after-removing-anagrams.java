class Solution {

    public List<String> removeAnagrams(String[] words) {
      String prevKey = "";
      List<String> result = new ArrayList<>();

      for (String word : words) {
        String sortedWord = getSortedWord(word);
        if(!sortedWord.equals(prevKey)) {
          result.add(word);
          prevKey = sortedWord;
        }
      }
      return result;
  }

  private String getSortedWord(String word) {
    char[] charArray = word.toCharArray();
    Arrays.sort(charArray);
    return new String(charArray);
  }

}