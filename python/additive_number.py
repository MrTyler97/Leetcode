"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

"""
# My solution
def isAdditiveNumber(num):
    
        for index, number in enumerate(num):
            #once we are on index 3
            if index > 1:
                print("Current number via loop variable: ", number)
                #add previous indexes and compare result. convert sting to int 
                if (int(num[index - 1]) + int(num[index - 2])) == int(number):
                    print("Previous number: ", num[index - 1], "Previous - 2 number: ", num[index - 2])
                    continue
                else: return False
        return True
                
#print(isAdditiveNumber("199100199"))

# Correct Solution
def isAdditiveNumber2(num):
    # cant be additive with two numbers
    if len(num) < 3:
        return False
    
    def helper(first, second,remaining):
        # First and second number cannot be larger than the sum
        if len(remaining) < len(first) or len(remaining) < len(second):
            return False
        # Check for 0 in first index of number
        if first[0] == '0' and len(first) > 1 or \
        second[0] == '0' and len(second) > 1:
           return False
       
        # Get additive and conver to string 
        res = str(int(first) + int(second))
         
        # If result equals the first number in remaining block (the sum)
        if res == remaining[0: len(res)]:
            # reached end of sequence
            if len(remaining) == len(res):
                return True
            
            first = second
            second = res
            # set remaining as everything after the result 
            remaining = remaining[len(res):]
            # Recursively call helper with new values
            return helper(str(first), str(second), remaining)
        return False
        
    
    #Get all possible number groups from string.
    
    # First number group 
    index = 0
    # Second number group
    for index2 in range(index + 1, len(num)):
        # Third number group
        for index3 in range(index2 + 1, len(num)):
            # ":" includes every value inbetween
            first = num[index : index2]
            second = num[index2 : index3]
            remaining = num[index3:]
            
            if helper(first, second, remaining):
                return True
    return False

print(isAdditiveNumber2("199100199"))