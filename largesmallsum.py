def LargeSmallSum(arr):
    if arr:
        arr = arr.split()
        if len(arr) > 3:
            odds = sorted([arr[_f] for _f in range(len(arr)) if _f % 2 != 0])
            evens = sorted([arr[_f] for _f in range(len(arr)) if _f % 2 == 0])
            return odds[1] + evens[-2]
        else:
            return 0
    else:
        return 0

print(LargeSmallSum('3 2 1 7 5 4'))