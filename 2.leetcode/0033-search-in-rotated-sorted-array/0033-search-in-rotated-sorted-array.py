class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        # <= 인 이유는 nums의 원소가 1개인 경우도 처리하기 위해
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            #left sorted portion
            if nums[l] <= nums[mid]:
                # 찾으려는값이 더 오른쪽에 있거나 왼쪽에서는 더 찾을 수 없을 때
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 찾으려는 값이 더 왼쪽에 있거나 오른쪽에서는 더 찾을 수 없을 때
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1