class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.defaultdict(int)
        res=[]
        for i in nums:
            count[i]+=1
        sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_counts[i][0])
        return res