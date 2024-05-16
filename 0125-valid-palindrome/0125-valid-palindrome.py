class Solution(object):
    def isPalindrome(self, s):
        # 첫번째 풀이
        # 여기서 배울 수 있었던 것은 isalnum이라는 함수다
        # isalnum은 영어 혹은 한글로 되어있느냐를 보는 것이다.
        # 만약 공백이나 특수문자가 나오면 False로 return 한다.
        # 하지만 첫번째 풀이는 썩 좋지 못한 풀이라고 한다.
        # 왜냐하면 memory도 차지하고 다 다 비교하기 때문에 빅오의 제곱이라고 하더라
        # newString = ""
        # for char in s:
        #     if char.isalnum():
        #         newString += char.lower()
        # return newString == newString[::-1]
        
        # 두번째 풀이
        # 두번째 풀이는 two pointer 알고리즘을 활용한 것이다.
        # 딱 한 번만 실행하기 때문에 빅오 n이라고 했다.
        # 그리고 ord라는 함수는 아스키코드를 알려준다.
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphaNumber(s[left]):
                left += 1
            while right > left and not self.alphaNumber(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True

    def alphaNumber(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))