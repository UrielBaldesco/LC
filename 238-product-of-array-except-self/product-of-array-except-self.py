class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix, postfix = 1,1
        output = [1] * n #auxillary array initialized with 1 for all values 
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
            