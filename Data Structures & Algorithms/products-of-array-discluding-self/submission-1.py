class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)
        prefix_list = [1] *  len(nums)
        postfix_list = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(0,len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            postfix_list[i] = postfix
            postfix *= nums[i]
            
        
        for i in range(0,len(nums)):
            res[i]= prefix_list[i] * postfix_list[i]
        
        return res


        