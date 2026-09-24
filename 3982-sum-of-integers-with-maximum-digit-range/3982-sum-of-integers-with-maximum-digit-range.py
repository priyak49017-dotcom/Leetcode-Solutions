class Solution(object):
    def maxDigitRange(self, nums):
        max_range=-1
        ans=0
        for num in nums:
            digits=str(num)
            mx=max(digits)
            mn=min(digits)
            digit_range=int(mx)-int(mn)
            if digit_range > max_range:
                max_range=digit_range
                ans=num
            elif digit_range == max_range:
                ans+=num
        return ans