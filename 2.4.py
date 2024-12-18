def swap_ad(arr):
  n = len(arr)
  for i in range(0, n - 1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
  return arr

numb = list(map(int, input().split()))
swapped_numb = swap_ad(numb)
print(swapped_numb)