def find_longest_recurrent_sequence(keywords):
    longest_sequence = ""
    for word in keywords:
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                sequence = word[start:end]
                count = sum(sequence in keyword for keyword in keywords)
                if count > 1 and len(sequence) > len(longest_sequence):
                    longest_sequence = sequence
    return longest_sequence

keywords = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog']
result = find_longest_recurrent_sequence(keywords)
print("Longest recurrent sequence:", result)
