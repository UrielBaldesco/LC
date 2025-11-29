class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #2d array, each index in the array corresponds to the frequency and each element in the indx is a list. the list inside each index is the number that has that many frequencies 
        
        #step 1: have a dictionary that has a key that is the number and the value that is the frequency
        #step 2: have a 2d array of lsits
        bucket = [[] for _ in range(len(nums)+1)]
        print(bucket)
        
        #step 3: populate count
        count = Counter(nums)
        print(count)

        for key,val in count.items():
            bucket[val].append(key)
        print(bucket)
        res = []
        #step 4:iterate backwards the bucket array and append the numbers to the result until k is 0
        for i in range(len(bucket)-1,0,-1):
            for sublist in bucket[i]:
                res.append(sublist)
                if len(res) == k:
                    return res
        

        
            