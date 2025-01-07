class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm={}
        for n in nums:
            hm[n]=hm.get(n,0)+1
        res=-1
        sorted_keys=list(sorted(hm.keys()))
        print(sorted_keys)
        temp=1
        for i in range(len(sorted_keys)-1):
            if sorted_keys[i+1]-sorted_keys[i]==1:
                temp+=1
            else:
                res=max(res,temp)
                temp=1
        return len(sorted_keys) if res==-1 else max(res,temp)