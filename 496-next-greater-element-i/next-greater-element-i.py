class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        while nums1:
            x=nums1.pop(0)
            print(x)
            pos=None
            for i in range(len(nums2)):
                if nums2[i]==x:
                    pos=i
                    break
            # print("pos1",pos)
            found=False
            for i in range(pos+1,len(nums2)):
                if nums2[i]>x:
                    res.append(nums2[i])
                    found=True
                    break
            if not found:
                res.append(-1)
            # print("@@")
        return res