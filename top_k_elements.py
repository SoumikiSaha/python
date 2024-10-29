def find_digits(num_list, k):
    # find frequency
    freq_dict = {}
    for n in num_list:
        keys = freq_dict.keys()
        if n in keys:
            freq_dict[n] += 1
        else:
            freq_dict[n] = 1
    # converting in to list
    freq_list = []
    for key, value in freq_dict.items():
        freq_list.append((key, value))
    # sorting list
    freq_list.sort(key=lambda x : x[1], reverse=True)
    #finding top k elements
    result = []
    for i in range(k):
        result.append(freq_list[i][0])
    return result

nums = [1,2,2,3,3,3]
k = 2
print(find_digits(nums, k))

    