def permutation(nums,set_arr=[],answers=[]):
  if len(nums) == 0:
    answers.append(set_arr.copy())
  

  for i in range(0,len(nums)):
    new_nums = nums.copy()
    item = new_nums[i]
    new_nums.remove(item)
    
    set_arr.append(item)
    permutation(new_nums,set_arr,answers)
    set_arr.pop()
    
  return answers
    



