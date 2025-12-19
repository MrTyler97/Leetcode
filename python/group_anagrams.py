"""
Docstring for python.group_anagrams

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
"""

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dict = {(list)} #mapping character count to list of anagrams 
    for word in strs:

        # This count array will act as the key in our hash map. 
        count = [0] * 26 #create array for number of characters in each word

        for char in word:
            # get the character array indeces of current word. 
            # ex: [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] = the key = hat

            count[ord(char) - ord("a")] += 1 #ord() returns the Unicode code point (integer) of a given character.

        # convert list to tuple and add current word based on indexed array key
        dict[tuple(count)].append(word)

    return dict.values