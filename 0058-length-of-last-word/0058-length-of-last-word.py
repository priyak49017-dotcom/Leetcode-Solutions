class Solution(object):
    def lengthOfLastWord(self, s):
        str=s.split()
        lst=str[-1]
        return len(lst)