import numpy as np

#data, rows --> cities
x   = np.array(
  [
    [42, 40, 41, 43, 44, 43], #HK
    [30, 31, 29, 29, 29, 30], #NY
    [ 8, 13, 31, 11, 11,  9], #Berlin
    [11, 11, 12, 13, 11, 12], #Montreal
  ]
)

cities      = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

#test
polluted    = np.nonzero(x < np.average(x))[0]
print(polluted)

# test
polluted    = cities[np.nonzero(x > np.average(x))[0]]
print(polluted)

# 
print(x)

# listing 3-15
print(x > np.average(x))

# one-liner:
polluted    = set(cities[np.nonzero(x > np.average(x))[0]]) #fr how cool is  this line??!
print(polluted)
    
# average, for troubleshooting:
print(np.average(x))
