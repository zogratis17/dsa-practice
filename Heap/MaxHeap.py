def parent(i):
  return (i-1)//2

def insert(heap, value):
  heap.append(value)
  i = len(heap) - 1
  
  while i > 0 and heap [i] > heap [parent(i)]:
    parent_idx = parent(i)
    heap[i] , heap[parent_idx] = heap[parent_idx], heap[i]
    i = parent_idx

def main():
  n = int(input())
  elements = list(map(int, input().split()))
  heap = [] 
  for elem in elements:
    insert(heap, elem) 
  
  for ele in heap:
    print(ele, end = ' ')

main()

