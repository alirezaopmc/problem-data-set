n = int(input())
a = list(map(int, input().split()))

current_subarray = max_subarray = a[0]

# Start with the 2nd element since we already used the first one.
for num in a[1:]:
    # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
    current_subarray = max(num, current_subarray + num)
    max_subarray = max(max_subarray, current_subarray)

print(max_subarray)