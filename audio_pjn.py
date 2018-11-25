import numpy as np
import scipy.io.wavfile as wave
from scipy.fftpack import dct
import sys



#############################------Hamming window Generator----#############################################
def Hamming(frame_size):
  ham_wind=np.zeros(frame_size)
  for i in range(frame_size):
     ham_wind[i]=(0.54- 0.46*np.cos((2*(np.pi)*i)/(frame_length-1)))
  return ham_wind

###########################################################





sample_rate,signal=wave.read("/home/fotapjn/pjn_tensor/wavepjn.wav")
print(sample_rate)
#print(signal)
#print(np.shape(signal))
signal1=signal[0:sample_rate]

print("Size of signal1",np.shape(signal1))
premp_signal=signal1[1:]-0.97*signal1[:-1]
premp_signal=np.append(signal[0],premp_signal)
#print(premp_signal[10000:16000])
#print(np.shape(premp_signal))
#Framing 
frame_size=0.025
stride_size=0.01


frame_length= frame_size*sample_rate
stride_length=stride_size*sample_rate

frame_length=int(round(frame_length))
stride_lenght=int(round(stride_length))
signal_length=len(premp_signal)
frame_num= int(np.ceil(float(np.abs(signal_length-frame_length))/stride_length))
print("Total number of frames are=",frame_num)


####################-------Padding of zeros in order to make all frames of same lenght -------------------#####

padded_signal_length=int(frame_num*stride_length+frame_length)
print(padded_signal_length)
z=np.zeros(padded_signal_length-signal_length)
print("Total number of zeros to be padded to make each frame of equal length are =",len(z))
signal_w_padding=np.append(premp_signal,z)
print("Total length of signal with premp and padding =",len(signal_w_padding))


#Hamming
ham_array=Hamming(frame_length)
print(ham_array)


