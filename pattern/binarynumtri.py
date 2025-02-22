"""
Pattern:

1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1

"""

rows = 5  # Number of rows in the triangle

for i in range(1, rows + 1):
    # Initialize the starting number for each row (alternates between 1 and 0)
    start = i % 2  # Rows alternate starting with 1 (odd rows) or 0 (even rows)
    for j in range(1, i + 1):
        # Print the binary value and toggle between 1 and 0
        print(start, end=" ")
        start = 1 - start  # Toggle: 1 becomes 0, and 0 becomes 1
    print()  # Move to the next line
