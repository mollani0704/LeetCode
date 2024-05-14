class Solution(object):
    def isAnagram(self, s, t):

        # HashMap을 이용한 정답
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        # 내가 푼 정답
        # s = sorted(list(s))
        # t = sorted(list(t))

        # if(len(s) != len(t)):
        #     return False

        # count = 0

        # for i in range(0, len(s)):
        #     if(s[i] == t[i]):
        #         count = count + 1
        #     else: 
        #         count = 0
        # if(count == len(s)):
        #     return True
        # else:
        #     return False


    
        