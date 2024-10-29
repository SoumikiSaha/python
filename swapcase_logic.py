st = 'Soumiki Saha'
output = []
for s in st:
    if s.isupper():
        output.append(s.lower())
    else:
        output.append(s.upper())
print(''.join(output))