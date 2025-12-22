/*
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
*/

function isValid(s: String): boolean{

    const stack: String[] = [];
    // Map closing to opening 
    const map: {[key: string]: string} = {")":"(", "]": "[", "}": "{"};
    
    for (var char of s) {
        // Check for correct characters 
        if (char in map){
            // check for empty stack 
            if (stack.length > 0 && stack[stack.length - 1] === map[char]){ // get opening bracket from current closing bracket
                stack.pop()
            }
            else return false;
        }
        else{
            stack.push(char)
        }
    }
    if (stack.length === 0 ){
        return true;
    }
    return false;
}