"""
Docstring for python.long_com_prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
strs = ["flower","flow","flight"]
strs2 = ["flower","food","dog"]

def prefix (arr: list[str]) -> str:
    #if array is empty return empty string
    if not arr: 
        return ""
    ans = ""
    # Reverse nested loop
    # ---------------------------------------------
    # Loop through each char in current word
    for char_index in range(len(arr[0])):
        #Grab current index
        char = arr[0][char_index]
        #Loop through all words in array
        for word in arr:
            #if characters don't match exit
            if word[char_index] != char:
                return ans
        # all match, add char to string
        ans += char
    return ans
result = prefix(strs2)
print(result)
