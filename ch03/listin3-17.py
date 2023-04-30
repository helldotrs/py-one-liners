import numpy as np

# data: popular instagram accounts (followers in mil)
insta = np.array(
                  [
                    [232, "@instagram"],
                    [133, "@selenagomez"],
                    [59,  "@victoriassecret"],
                    [120, "@cristiano"],
                    [111, "@beyonce"],
                    [76,  "@nike"]
                  ]
)

#one-liner
superstars  = insta[insta[:,0].astype(float) > 100, 1]

print(superstars)
