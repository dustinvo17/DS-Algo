# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]
class Solution(object):
    def plusOne(self, digits):
        j = len(digits) - 1
        while j >= 0:
            item = digits[j]
            item += 1
            if item == 10:
                digits[j] = 0
                j -= 1
            else:
                digits[j] = item
                return digits
                break
        # reach end of list and still have a carry of 1 then insert 1 in the beginning
        if j == -1:
            digits.insert(0,1)
        return digits

        """
        :type digits: List[int]
        :rtype: List[int]
        """
