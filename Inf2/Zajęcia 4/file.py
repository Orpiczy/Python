import matplotlib.pyplot as plt
import numpy as np
x_i=np.array([-1.5, -0.75, 0, 0.75, 1.5])
y_i=np.array([-14.1014,-0.931596,0,0.931596,14.1014])

lag_base= lambda i,x : np.prod(x-np.delete(x_i,i))/np.prod(x_i[i]-np.delete(x_i,i))
Y=[]
X=np.linspace(-1.499,1.499,100)
for x in np.nditer(X):
    L=np.array([lag_base(0,x),lag_base(1,x),lag_base(2,x),lag_base(3,x),lag_base( 4,x)])
    Y.append(y_i@L.transpose())
Y=np.array(Y)

plt.plot(X,Y)
plt.scatter(x_i,y_i)