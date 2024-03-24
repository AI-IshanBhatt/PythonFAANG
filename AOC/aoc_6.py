# from functools import reduce
#
import time


times = [35696887]
distances = [213116810861248]


start = time.perf_counter()
ways = 1

for timex, d in zip(times, distances):
    w = 0
    for i in range(timex+1):
        speed = i
        distance_travel = timex - i
        total_travel = speed * distance_travel
        if total_travel >= d:
            w += 1
    ways *= w

end_time = time.perf_counter()
print(ways)
print(f"Time taken brute_force {end_time-start}")

def with_binary_search(times, distances):
    low, high = 1, times

    # Moving to left
    while low < high:
        mid = (high + low) // 2
        distance_travel = mid * (times - mid)

        if distance_travel > distances:
            high = mid
        else:
            low = mid + 1

    left_side = high

    low, high = 1, times
    while low < high:
        mid = (high + low) // 2
        distance_travel = mid * (times - mid)

        if distance_travel > distances:
            low = mid + 1
        else:
            high = mid

    return left_side, high


answer = 1

start = time.perf_counter()

l,r = with_binary_search(35696887, 213116810861248)
print(r-l)

end = time.perf_counter()
print(f"Time taken binary search {end - start}")
