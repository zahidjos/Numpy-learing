import numpy as np
matrix=np.array([[5,10,15,20],
                 [20,30,40,50],
                 [12,14,16,18]
                ])
rowData=np.array([2,3,4,5])
print(matrix+rowData)
print(matrix-rowData)
print(matrix*rowData)
cloumData=np.array([[5],
                    [3],
                    [2]
                   ])
print(matrix+cloumData)
print(matrix-cloumData)
print(matrix*cloumData)
