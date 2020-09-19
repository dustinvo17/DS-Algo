def qs(arr,start,end):
  if start >= end:
    return
  pivot = partition(arr,start,end)
  qs(arr,start,pivot-1)
  qs(arr,pivot+1,end)

def partition(arr,start,end):
  pivot = arr[start]
  i = start
  j = start + 1
  while j <= end:
    if arr[j] < pivot:
      i += 1
      arr[i],arr[j] = arr[j],arr[i]
    j +=1
  arr[i],arr[start] = arr[start],arr[i]
  return i
def quick_sort(arr):
  return qs(arr,0,len(arr)  -1 )



a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]


quick_sort(a7)
quick_sort(a8)
quick_sort(a9)
print(a7)
assert a7 == [-2, -1, 0, 1, 2, 3, 4]
assert a8 == [1, 2, 3, 4, 5, 6, 7]
assert a9 == [2, 2, 2, 2, 2, 2, 2]
print("If you didn't get an assertion error, this program has run successfully.")