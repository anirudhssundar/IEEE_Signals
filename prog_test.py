
#import necessary libraries

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
 
#set frequency of the wave 
frequency = 264
#frequency2 = 1000    #we'll use this later
 
num_samples = 8000     
 
sampling_rate = 8000.0   # The sampling rate of the analog to digital convert
 
amplitude = 16000	
 
file = "test.wav"		#the sound file we are writing to

sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

#creating a sine wave


#sine_wave2 = [np.sin(2 * np.pi * frequency2 * x/sampling_rate) for x in range(num_samples)]

sine_wave=np.array(sine_wave)    #convert to a numpy array



#sine_wave2=np.array(sine_wave2)
#sine_final = sine_wave+sine_wave2


nframes=num_samples
 
comptype="NONE"
 
compname="not compressed"
 
nchannels=1
 
sampwidth=2 #2bytes = 16 bits

wav_file=wave.open(file, 'w')
 
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes,comptype, compname))

for s in sine_final:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))


struct.pack('h', int(s*amplitude))

