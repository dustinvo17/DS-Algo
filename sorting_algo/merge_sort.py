def sortArray(nums):
  if len(nums) == 1:
    return nums
  mid =len(nums) // 2
  left = nums[0:mid]
  right = nums[mid:len(nums)]
  print(left,right)
  return merge(sortArray(left),sortArray(right))
def merge(a1,a2):
  result = []
  while len(a1) > 0 and len(a2) > 0:
    if a1[0] <= a2[0]:
      result.append(a1.pop(0))
    else:
      result.append(a2.pop(0))
  result.extend(a1)
  result.extend(a2)
  return result
  
arr = [5,2,3,1]
arr = sortArray(arr)
print(arr)
