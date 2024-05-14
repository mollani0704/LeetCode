class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(list(s))
        t = sorted(list(t))

        if(len(s) != len(t)):
            return False

        count = 0

        for i in range(0, len(s)):
            if(s[i] == t[i]):
                count = count + 1
            else: 
                count = 0
        if(count == len(s)):
            return True
        else:
            return False


    
        