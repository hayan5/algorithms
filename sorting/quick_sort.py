def partition(A, p, r):
  #A[p..r] is the array to be partitioned
  #p >= 0, r <= last index in A
  #After partition all elements A[p..q-1] <= A[q] < A[q+1..r] in main quicksort function
  x = A[r] #x is the pivot (last element in array A)
  i = p - 1

  for j in range(p, r):  #start at left of array and include all indices except the pivot
    if A[j] <= x:
      i += 1
      A[i],A[j] = A[j],A[i]
  
  A[i+1],A[r] = A[r],A[i+1] 

  return (i + 1)

def quick_sort(A, p, r):
  #A is the array to be sorted
  #p is left index of A
  #r is right index of A
  if p < r: 
    q = partition(A, p, r)
    quick_sort(A, p, q-1) #left of pivot
    quick_sort(A, q+1, r) #right of pivot


if __name__ == "__main__":
  n = 10
  A = [4,5,6,2,9,1,5,8,3,2]
  print('Array before quick_sort',A)
  quick_sort(A,0,n-1)
  print('Array after quick_sort',A)
  