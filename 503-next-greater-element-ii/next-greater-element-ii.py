class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        res=[-1]*len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while st and nums[i]>nums[st[-1]]:
                    x=st.pop(-1)
                    res[x]=nums[i]
                st.append(i)
        return res
        