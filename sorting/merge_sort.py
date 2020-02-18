import random

def merge_sort(A, p ,r):
  if p < r:
    q = (p + r)//2
    
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)





if __name__ == "__main__":
  n = int(input("Enter Size of Array: "))
  A =[]
  for i in range(n):
    A.append(random.randint(0,n))
  print('Array before merge_sort',A)
  merge_sort(A, 0, n-1)
  print('Array after merge_sort',A)