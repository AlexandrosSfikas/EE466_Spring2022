import numpy as np
import matplotlib.pyplot as plt

Fs = 300 # sample rate
Ts = 1/Fs # sample period
N = 2048 # number of samples to simulate

t = Ts*np.arange(N)
S1 = 20 * np.exp(1j*2*np.pi*100*t) # simulates sinusoid at 100 Hz
S2 = 20 * np.exp(1j*2*np.pi*200*t) # simulates sinusoid at 200 Hz
TransmittedX = S1 + S2
n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # complex noise with unity power
noise_power = 2
ReceivedX = TransmittedX + n * np.sqrt(noise_power)

PSD = (np.abs(np.fft.fft(ReceivedX))/N)**2
PSD_log = 10.0*np.log10(PSD)
PSD_shifted = np.fft.fftshift(PSD_log)
f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step

plt.plot(f, PSD_shifted)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()