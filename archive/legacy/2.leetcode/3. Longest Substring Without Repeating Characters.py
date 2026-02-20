
class Solution:
    def lengthOfLongestSubstring(self, ss: str) -> int:
        used = {}
        max_length = start = 0

        for idx, char in enumerate(ss):
            # 이미 등장했던 문자라면 'start' 위치를 갱신
            # 현재 슬라이딩 윈도우 밖에 있는 문자는 예전에 사용했더라도 무시해야함
            if char in used and start <= used[char]:
                start = used[char] + 1

                # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, idx - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = idx

        return max_length



print(Solution().lengthOfLongestSubstring("abcabcbb"))