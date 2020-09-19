def count_num(arr,num):
  start = 0 
  end = len(arr) - 1


  i = None
  j = None

  while True:
    if arr[start] == num:
      
   
      start +=1
     
      if arr[start+1] != num:
        return start + 1
        break
    if arr[end] == num:
   
      end -=1
      if arr[end-1] != num:
        return len(arr)  - end
        break
    mid = int((start+end)//2)
 
    if start > end:
      return -1
      break
    if num < arr[mid]:
      end = mid - 1
    if num > arr[mid]:
       start = mid + 1
    if arr[mid] == num:

      i = i if i is not None  else mid -1
      j = j if j is not None else mid +1
      
      if  arr[i] == num :
        i -=1
      if arr[j] == num :
        j +=1
    
      if arr[i] != num and arr[j] != num:
        return j - (i+1)
        break

print(count_num([1,1,1,3,3,3,3,4,4,4,4,5,5,5,5],5))
