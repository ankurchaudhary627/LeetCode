class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet=set(nums)
        maxCount=0
        for i in hashSet:
            if i-1 not in hashSet:
                temp=i
                currCount=1
                while temp+1 in hashSet:
                    temp+=1
                    currCount+=1
                maxCount=max(maxCount,currCount)
        return maxCount