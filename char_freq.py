st = "programmer"
answer = []
dictionary = {}
for i in st:
    keys = dictionary.keys()
    if i in keys:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
highest = 0
highest_key = ''
for d in dictionary:
    answer.append("%s : %s" % (d, dictionary[d]))
    if dictionary[d] >= highest:
        highest = dictionary[d]
        highest_key = d
print("letter count: ", "\n".join(answer))
print("highest value: ",highest_key, " : ", dictionary[highest_key])