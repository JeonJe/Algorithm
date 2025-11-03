class Solution {

  public boolean hasSameDigits(String s) {
    while (s.length() > 2) {
      s = operationToString(s);
    }
    return isSame(s);

  }

  private String operationToString(String s) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length() - 1; i++) {
      sb.append(operation(s.charAt(i), s.charAt(i + 1)));
    }
    return sb.toString();
  }


  private String operation(Character c1, Character c2) {
    int sum = Character.getNumericValue(c1) + Character.getNumericValue(c2);
    return Integer.toString(sum % 10);
  }

  private boolean isSame(String s) {
    if (s.length() != 2) {
      return false;
    }
    return s.charAt(0) == s.charAt(1);
  }
}
