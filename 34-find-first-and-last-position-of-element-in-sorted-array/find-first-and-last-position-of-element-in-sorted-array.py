class Solution:
    def binSearch1(self, start, end, arr, val):
        idx=None
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==val:
                idx=mid
                end=mid-1
            elif arr[mid]<val:
                start+=1
            else:
                end-=1
        return idx

    def binSearch2(self, start, end, arr, val):
        idx=None
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==val:
                idx=mid
                start=mid+1
            elif arr[mid]<val:
                start+=1
            else:
                end-=1
        return idx

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N=len(nums)
        left = self.binSearch1(0,N-1, nums, target)
        if left is None:
            return [-1,-1]
        right = self.binSearch2(left, N-1, nums, target)
        print(left,right)
        return [left, right]