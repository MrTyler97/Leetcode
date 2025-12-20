'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

'''
# My solution O(n^2)
def productExceptSelf(nums: list[int]) -> list[int]:
    #Create array with required length
    ans = [None] * len(nums)
    for index, num in enumerate(nums):
        #Reset product value 
        val = 1
        for i in range(len(nums)):
            #If not on current index, multiply
            if nums[i] != num:
                val *= nums[i] 
        ans[index] = val
                
    return ans

#Optimal Solution O(n)
def productExceptSelf1(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    # This solution uses prefix and postfix values 
    prefix = 1
    for i in range(len(nums)):
        #Store prefix in correct index
        res[i] = prefix
        #update prefix value
        prefix *= nums[i]
        # res = [1,1,2,8]
        
    postfix = 1
    # Iterate through array in reverse
    for i in range(len(nums) - 1, -1, -1):
        # Multiplying prefix and post fix together 
        res[i] *= postfix
        #Update postfix
        postfix *= nums[i]
        
    return res

x = [1,2,4,6]

ans = productExceptSelf(x)
ans2 = productExceptSelf1(x)
print(ans, " ", ans2)