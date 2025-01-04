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

    def increasingTriplet(self, nums: List[int]) -> bool:
        lis=[]
        found=False
        for n in nums:
            if not lis:
                lis.append(n)
            else:
                if n>lis[-1]:
                    lis.append(n)
                else:
                    idx=self.binSearch(0,len(lis)-1,n,lis)
                    lis[idx]=n
            #         print(idx)
            print(lis)
            if len(lis)>=3:
                found=True
                break
        return True if found else False