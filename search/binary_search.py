# A: sorted array, l: left index, r: right index, x target
def binary_search(A, l, r, x):
  
  if r >= l:
    mid = (l + r) // 2

    #target found
    if A[mid] == x:
      return mid

    if A[mid] > x:
      return binary_search(A, l, mid-1, x)

    if A[mid] < x:
      return binary_search(A, mid+1, r, x)

  return -1
