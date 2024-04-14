class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack  = new Stack<>();

        Map<Character, Character> brackets = new HashMap<>();
        brackets.put('}', '{');
        brackets.put(']', '[');
        brackets.put(')', '(');

        List<Character> openBrackets = List.of('{', '[', '(');

        for(int i = 0; i < s.length(); i++){
            char current = s.charAt(i);
            if(openBrackets.contains(current)){
                stack.add(current);
            } else {
                if (stack.isEmpty() || stack.pop() != brackets.get(current)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}