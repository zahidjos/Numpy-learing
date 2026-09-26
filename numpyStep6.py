import numpy as np
data =np.array([[5,7,8],
                [10,12,14],
                [15,16,17]
                ])
print(data)
print(np.sum(data,axis=0))
print(np.sum(data,axis=1))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))