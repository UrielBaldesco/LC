class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        '''
        heap where each node is a tuple 
            the tuple is (the number, the frequency)
        
        step 1: create a frequency map
        step 2: create a heap list 
        step 3: populate the heap, restrict the heap to length of k
        '''
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap,(val,key)) #the frequency should be change the order
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        return [key for (val, key) in heap]
 #iterates through each tuple, ignores the first index in the tuple and only care about the second index of the tuple -- aka the actual number, the first index is the frequency which we dont want