import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as wav

r, data = wav.read('test.wav', mmap=False)


data_fft =  np.fft.fft(data)  #fast fourier transform of the data signal

frequencies = np.abs(data_fft) #the np.fft function returns complex values, we take the absolute value since we are dealing with reals


plt.subplot(2,1,1)
 
plt.plot(data[:300])
 
plt.title("Original audio wave")
 
plt.subplot(2,1,2)
 
plt.plot(frequencies)
 
plt.title("Frequencies found")
 
plt.xlim(0,1200)
 
plt.show()