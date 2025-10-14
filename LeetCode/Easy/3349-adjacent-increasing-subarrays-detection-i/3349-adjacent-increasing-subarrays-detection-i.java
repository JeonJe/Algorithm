
class Solution {

  public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
    int[] arr = nums.stream()
        .mapToInt(Integer::intValue)
        .toArray();

    int n = arr.length;

    if (k <= 0 || 2 * k > n) return false;


    for (int i = 0; i + (2 * k) <= n; i++) {
      if (isStrictlyIncreasing(arr, k, i) && isStrictlyIncreasing(arr, k, i + k)) {
        return true;
      }
    }

    return false;
  }

  private boolean isStrictlyIncreasing(int[] arr, int increaseSize, int idx) {
    for (int i = idx + 1; i < idx + increaseSize; i++) {

      if (arr[i - 1] >= arr[i]) {
        return false;
      }
    }
    return true;
  }
}
