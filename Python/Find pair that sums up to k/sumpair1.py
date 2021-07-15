
# Find pair that sums up to k
# By checking all pairs (brute force solution):

# arr = [4, 1, 5, 7, 2]
# k = 3

# Time complexity: O(n²)
# Space complexity: O(1)

def findPair(arr, k):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == k:
        print(str(arr[i]), str(arr[j]))
        return True
  return False

