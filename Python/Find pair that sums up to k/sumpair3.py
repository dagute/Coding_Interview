# By using a dictionary:

# Time complexity: O(n)
# Space complexity: O(n)

# arr = [8, 2, 9, 5, 10, 1]
# k = 12

def findPair(arr, k):
  visited = {}
  for element in arr:
    if visited.get(k-element):
      return True
    else:
      visited[element] = True
  return False
