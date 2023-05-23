class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = None
        ctr = 0
        flag = 0
        for x in s:
            i = ctr
            while i<len(t):
                if x == t[i]:
                    flag += 1
                    ctr = i+1
                    break
                i += 1
        if flag == len(s):
            return True
        else:
            return False
