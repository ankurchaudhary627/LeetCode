class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[1001]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=len(nums)-1:
                dp[i]=1
            elif nums[i]>0:
                dp[i] = min(dp[i+1:i+nums[i]+1])+1
                # if i==0:
                #     print(dp[i+1:i+nums[i]+1])
                #     print(min(dp[i+1:i+nums[i]+1])+1)
            # print(dp)
        return 0 if dp[0] == 1001 else dp[0]
            