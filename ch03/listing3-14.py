import numpy as np

#data, rows --> cities
x   = np.array(
  [
    [42, 40, 42, 43, 44, 43], #HK
    [30, 30, 29, 30, 31, 30], #NY
    [8, 11, 13, 11, 11, 9], #Berlin
    [11, 12, 10, 11, 13, 22], #Montreal
  ]
)

#test
polluted  = np.nonzero(x < np.average(x))[0]

# test
polluted  = (cities[np.nonzero(x < np.average(x))[0]]
print(polluted)

# one-liner:
polluted  = set(cities[np.nonzero(x < np.average(x))[0]]) #fr how cool is  this line??!
print(polluted)
    
