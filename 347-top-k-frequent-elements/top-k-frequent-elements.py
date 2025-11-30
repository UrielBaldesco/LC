class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #create a map with key as number, val is the freq
        count = Counter(nums)
        heap = [] #heap is a list with an order
        for key,val in count.items(): #iterate the key,vals in the map
            heapq.heappush(heap, (val,key)) #populate the heap
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for (val,key) in heap]

