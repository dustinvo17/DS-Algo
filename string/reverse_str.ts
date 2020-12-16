/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    var start = 0
    var end = s.length - 1
    while (start < end) {
        var temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start +=1
        end -=1
    }
};