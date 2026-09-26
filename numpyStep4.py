import numpy as np
data=np.array([[5,10,20,30,40],
               [10,15,20,25,30],
               [5,10,15,20,15]
               ])
print(data)
print(data[0])
print(data[:,1])
print(data[1,3])

product=np.array([30,40,50,70,80,90])
print(product>50)
print(product[product>50])
print(product[(product>40) & (product<80) ])
