class Solution {
    public static Set<Character> vowels = new HashSet<>(List.of('a', 'e', 'i','o','u', 'A','E','I','O','U'));

    public String sortVowels(String s) {
        List<Character> temp = new ArrayList<Character>();
        char[] chars = s.toCharArray();

        for(char c : chars) {
            if(vowels.contains(c)) {
                temp.add(c);
            }
        }

        List<Character> sorted = temp.stream()
        .sorted(Character::compare)
        .collect(Collectors.toList());

        StringBuilder sb = new StringBuilder();
        int idx = 0;
        for(char c : chars) {
            char cur = vowels.contains(c) ? sorted.get(idx++) : c;
            sb.append(cur);
        }

        return sb.toString();
    }
}