import numpy as np
original =np.array([10,20,30,40,50])
print(original)
viewData=original.view()
viewData[1]=88
print(viewData)
print(original)
copyData=original.copy()
copyData[1]=33
print(copyData)
print(original)
data=np.array([1,2,3,4,5,6])
slicingData=data[1:4]
slicingData[1]=10
print(slicingData)
print(data)
copyData=data[1:4].copy()
copyData[1]=20
print(copyData)
print(data)