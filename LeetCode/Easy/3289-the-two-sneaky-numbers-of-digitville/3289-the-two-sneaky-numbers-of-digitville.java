
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {

  public int[] getSneakyNumbers(int[] nums) {

    Map<Integer, Integer> map = new HashMap<>();
    Arrays.stream(nums)
        .forEach(n -> {
          Integer value = map.getOrDefault(n, 0);
          map.put(n, value + 1);
        });

    return map.entrySet()
        .stream()
        .filter(entry -> entry.getValue() >= 2)
        .map(Map.Entry::getKey)
        .mapToInt(Integer::intValue)
        .toArray();

  }
}
