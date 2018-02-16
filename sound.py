from numpy import linspace,sin,pi,int16
from scipy.io.wavfile import write
from pylab import plot,show,axis

import numpy as np


# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers
 
 


# all tones, 1 second each, 44100 samples per second
Atone = note(440,1,amp=10000)
Btone = note(494,1,amp=10000)
Ctone = note(523,1,amp=10000)
Dtone = note(587,1,amp=10000)
Etone = note(659,1,amp=10000)
Ftone = note(698,1,amp=10000)
Gtone = note(784,1,amp=10000)
A2tone = note(880,1,amp=10000)
Blank = note(0,0.10,amp=10000)


Octave = np.concatenate((Atone,Btone,Ctone,Dtone,Etone,Ftone,Gtone,A2tone))

Song = np.concatenate((Etone,Blank,Etone,Blank,Ftone,Blank,Gtone,Blank,Gtone,Blank,Ftone,Blank,Etone,Blank,Dtone,Blank,Ctone,Blank,Ctone,Blank,Dtone,Blank,Etone,Blank,Etone,Blank,Dtone,Blank,Dtone))

write('Octave.wav',44100,Octave)
write('Song.wav',44100,Song)
'''
write('Atone.wav',44100,Atone) # writing the sound to a file
write('Btone.wav',44100,Btone)
write('Ctone.wav',44100,Ctone)
write('Dtone.wav',44100,Dtone)
write('Etone.wav',44100,Etone)
write('Ftone.wav',44100,Ftone)
write('Gtone.wav',44100,Gtone)
'''

#plot(linspace(0,2,2*44100),tone)
#axis([0,0.4,15000,-15000])
#show()