def calculate_min_swap(arr,n):
  pos = 0
  swaps = 0
  for i in range(len(arr)):
    if arr[i] % 2 == n:
      swaps += abs(i - pos)
      pos += 1
  return swaps

def min_swap_to_make_even_odd_seperate(arr):
  odd = calculate_min_swap(arr,1)
  even = calculate_min_swap(arr,0)
  return min(even,odd)


n = int(input.strip()) 
inp_arr = list(map(input.strip().split()))
print(min_swap_to_make_even_odd_seperate(inp_arr))
