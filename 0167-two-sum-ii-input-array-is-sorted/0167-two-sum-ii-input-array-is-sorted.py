class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left, right = 0, length-1
        
        while left < right :
            sum_two_pointer = numbers[left] + numbers[right]
            if sum_two_pointer == target:
                return [left+1, right+1]
            elif sum_two_pointer < target:
                left += 1
            else:
                right -= 1
        
                