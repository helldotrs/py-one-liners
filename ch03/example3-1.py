import numpy as np

# 2d array from list of lists
b = np.array( [
                [1, 2],
                [3, 4]
              ])
print(f"b:{}\n", b)

# 3d array from list of lists of lists
c = np.array( [
                [
                  [1, 2],
                  [3, 4]
                ],
                [
                  [5, 6],
                  [7, 8]
                ]
              ])
print(f"c: {}\n", c)
