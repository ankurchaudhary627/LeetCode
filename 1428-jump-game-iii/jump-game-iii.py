class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=[]
        q.append(start)
        vis=set()
        N=len(arr)
        while q:
            idx=q.pop(0)
            vis.add(idx)
            if arr[idx]==0:
                return True
            if idx-arr[idx]>=0 and idx-arr[idx] not in vis:
                q.append(idx-arr[idx])
            if idx+arr[idx]<N and idx+arr[idx] not in vis:
                q.append(idx+arr[idx])
            # print(q)
            # print(vis)
        return False