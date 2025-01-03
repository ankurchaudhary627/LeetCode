class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        res=dict()
        for i in nums2:
            res[i]=-1
        for i in range(len(nums2)):
            while st and nums2[i]>nums2[st[-1]]:
                x=st.pop(-1)
                res[nums2[x]]=nums2[i]
            st.append(i)
        print(res)
        op=[]
        for i in nums1:
            op.append(res[i])
        return op