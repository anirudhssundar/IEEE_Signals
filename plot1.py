import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3,1/8000.0) 

sine_wave=2048*np.sin(2*x*np.pi)
cos_wave=2048*np.cos(2*x*np.pi)
exponent_wave=2048*np.exp(x)

plt.plot(x,np.sine_wave)
plt.show()



plt.plot(x,np.cos_wave)
plt.show()



plt.plot(x,np.exponent_wave)
plt.show()
