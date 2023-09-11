import numpy as np

array = np.array([0,
                  0,
                  0])
if not np.count_nonzero(np.isnan(array)):
    print(np.count_nonzero(np.isnan(array)))