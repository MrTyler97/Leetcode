/*
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]
*/

// My solution
function topKFrequent(nums: number[], k: number){
    //intitalize map 
    const map = new Map<number, number[]>();
    var ans: number[] = []
    // add value and number of elements
    for (const value of nums){
        // get map values or initialize
        const existing = map.get(value) || [];
        // add value to array
        existing.push(value);
        // set new array to value
        map.set(value, existing);
    }
    // loop for number of entries required
    for (var i = 0; i < k; i++){
        // Initialize counter for frequencies
        var count = 0;
        // iterate through keys
        for (const num of map.keys()){
            // check if key values length is the greatest and make sure its not already in answer array
            if(map.get(num)!.length > count && !ans.includes(num)){
                count = map.get(num)!.length;
                ans[i] = num;
            }
        }  
    }
    return ans;
}

// Optimized solution from AI
function topKFrequent2(nums: number[], k: number){
    const map = new Map<number, number>();
    for (const num of nums){
        //increment frequency related to current key
        map.set(num, (map.get(num) || 0) + 1)
    }

    // Turn entries into an array, sort entries in decending order
    const sorted = [...map.entries()].sort((a,b) => b[1] - a[1]);

    // return elements up to k
    return sorted.slice(0,k).map(entry => entry[0]);
}