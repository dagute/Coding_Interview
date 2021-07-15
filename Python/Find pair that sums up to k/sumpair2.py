# By sorting the array:

# Time complexity: O(nlogn)
# Space complexity: O(1) if you are allowed to modify the input, O(n) else

# arr = [1, 3, 5, 7, 9, 12]
# k = 14


def findPair(arr, k):
  arr.sort()
  left = 0
  right = len(arr)-1
  while left < right:
    if arr[left] + arr[right] == k:
      return True
    elif arr[left] + arr[right] < k:
      left += 1
    else:
      right -= 1
  return False