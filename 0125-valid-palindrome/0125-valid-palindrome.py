class Solution(object):
    def isPalindrome(self, s):
        # 첫번째 풀이
        # 여기서 배울 수 있었던 것은 isalnum이라는 함수다
        # isalnum은 영어 혹은 한글로 되어있느냐를 보는 것이다.
        # 만약 공백이나 특수문자가 나오면 False로 return 한다.
        newString = ""
        for char in s:
            if char.isalnum():
                newString += char.lower()
        return newString == newString[::-1]
        