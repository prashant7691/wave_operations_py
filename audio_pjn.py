import numpy as np
import scipy.io.wavfile as wave
from scipy.fftpack import dct



sample_rate,signal=wave.read("/home/fotapjn/pjn_tensor/wave6.wav")
print(sample_rate)
print(signal[:1000])
print(np.shape(signal))

premp_signal=signal[1:]-0.97*signal[:-1]
premp_signal=np.append(signal[0],premp_signal)
#print(premp_signal[10000:16000])
print(np.shape(premp_signal))
