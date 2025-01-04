class Solution:
    def binSearch(self,l,r,x,arr):
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[]
        for n in nums:
            if not lis:
                lis.append(n)
            else:
                if n>lis[-1]:
                    lis.append(n)
                else:
                    idx=self.binSearch(0,len(lis)-1,n,lis)
                    lis[idx]=n
            # print(lis)
        return len(lis)
        # sub = []
        # for x in nums:
        #     if len(sub) == 0 or sub[-1] < x:
        #         sub.append(x)
        #     else:
        #         idx = bisect_left(sub, x)  # Find the index of the first element >= x
        #         sub[idx] = x  # Replace that number with x
        #     print(sub)
        # return len(sub)
