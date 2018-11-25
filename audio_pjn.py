import numpy as np
import scipy.io.wavfile as wave
from scipy.fftpack import dct



sample_rate,signal=wave.read("/home/fotapjn/pjn_tensor/wave8.wav")
print(sample_rate)
print(signal[:1000])
print(np.shape(signal))
signal1=signal[0:sample_rate,1]

print("Size of signal1",np.shape(signal1))
premp_signal=signal[1:]-0.97*signal[:-1]
premp_signal=np.append(signal[0],premp_signal)
#print(premp_signal[10000:16000])
print(np.shape(premp_signal))


#Framing 

frame_size=0.025
stride_size=0.01


frame_length= frame_size*sample_rate
stride_length=stride_size*sample_rate

frame_length=int(round(frame_length))
stride_lenght=int(round(stride_length))
signal_length=lenght(premp_signal)







