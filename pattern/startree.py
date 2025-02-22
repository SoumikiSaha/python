
"""
Pattern:
   *
  ***
 *****
*******

"""


rows = 4  # Number of rows in the pyramid

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))

print("------" * 10)

"""
Pattern:

*******
 *****
  ***
   *
   
"""



for i in range(rows, 0, -1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))


