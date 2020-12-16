// Given two strings s and t , write a function to determine if t is an anagram of s.
// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
// Note:
// You may assume the string contains only lowercase alphabets.

// Follow up:
// What if the inputs contain unicode characters? How would you adapt your solution to such case?
function isAnagram(s: string, t: string): boolean {
    let hashMap = {}
    if(s.length !== t.length) return false
    for(let char of s) {
        if(!(char in hashMap)) hashMap[char] = 1
        else hashMap[char] +=1
    }
    for (let char of t) {
        if(!(char in hashMap)) return false
        hashMap[char] -= 1
        if(hashMap[char]  === 0 ) delete hashMap[char]
    }
    return Object.keys(hashMap).length === 0
};
// "abcc" "abca"  {a:1,b:1,c:2}   {a:-1,b:0,c:1}