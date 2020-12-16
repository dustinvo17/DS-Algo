function firstUniqChar(s: string): number {
    let hashMap:any = {}
    for(let i = 0; i < s.length; i ++) {
        let char = s[i]
        if(!(char in hashMap)) hashMap[char] = 1
        else hashMap[char] +=1
    }
    for(let i = 0; i < s.length; i++) {
        const char = s[i]
        if(hashMap[char] == 1) return i
    }
    return -1
};
