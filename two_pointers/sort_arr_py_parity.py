# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution(object):
    def sortArrayByParity(self, A):
        if len(A) <= 1:
            return A
        
        i = -1
        j = 0
        while j < len(A):
            if A[j] % 2 == 0:
                i += 1
                A[i],A[j] = A[j],A[i]
            j += 1
        return A
        """
        :type A: List[int]
        :rtype: List[int]
        """
