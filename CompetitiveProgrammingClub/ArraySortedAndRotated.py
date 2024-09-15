from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        numCopy = nums.copy()
        numCopy.sort()
        prev = nums[0]
        count = 0
        pos = 0
        for i in range(1,len(nums)):
            if nums[i] < prev:
                count+=1
                pos = i
            prev = nums[i]
        
        ans = False

        if count==0:
            ans = True
        elif count==1:
            makeArray = nums[pos:] + nums[0:i]
            if makeArray==numCopy:
                ans = True

        return ans


p1 = Solution()
nums = [3,4,5,1,2]
print(p1.check(nums))