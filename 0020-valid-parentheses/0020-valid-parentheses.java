class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack  = new Stack<>();

        Map<Character, Character> characterMapping = new HashMap<>();
        characterMapping.put('}', '{');
        characterMapping.put(']', '[');
        characterMapping.put(')', '(');
        List<Character> opens = List.of('{', '[', '(');

        for(int i = 0; i < s.length(); i++){
            char current = s.charAt(i);
            if(opens.contains(current)){
                stack.add(current);
            } else {
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.pop() != characterMapping.get(current)){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}