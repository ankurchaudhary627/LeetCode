import heapq

class Solution:
    def topKFrequent(self, words: List[str], k1: int) -> List[str]:
        words.sort()
        mp = dict()
        for w in words:
            mp[w] = mp.get(w,0)+1
        heap=[]
        for k,v in mp.items():
            heapq.heappush(heap,(-v,k))
        print(heap)
        res=[]
        while k1>0:
            res.append(heapq.heappop(heap)[1])
            k1-=1
        print(res)
        return res