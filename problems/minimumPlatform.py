def minimumPlatform(arrival, departure):
    n = len(arrival)
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arrival[i] < departure[j]:
            plat_needed += 1
            i += 1
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed -= 1
            j += 1
    return result

arr = [100, 200, 300, 400, 500]
dep = [200, 300, 400, 500, 600]
print("Minimum Platforms Required:", minimumPlatform(arr, dep))