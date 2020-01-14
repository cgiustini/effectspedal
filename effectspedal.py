import numpy as np
import matplotlib.pyplot as plt
import IPython
import wave
import struct
import array
import os
from playsound import playsound
import scipy.signal as signal

wav_fname = "./bassnotes_one.wav"
owav_fname = "./bassnotes_one_output.wav"

# wave_read = wave.open(wav_fname)
# n = wave_read.getnframes()
# data = wave_read.readframes(n)

# def read_whole(filename):
#     wav_r = wave.open(filename, 'r')
#     ret = []
#     while wav_r.tell() < wav_r.getnframes():
#         decoded = struct.unpack("<h", wav_r.readframes(2))
#         ret.append(decoded)
#     return ret

# data = read_whole(wav_fname)

# Read input wav.
sizes = {1: 'B', 2: 'h', 4: 'i'}
wav = wave.open(wav_fname)
channels = wav.getnchannels()
sampwidth = wav.getsampwidth()
samprate = wav.getframerate()
fmt_size = sizes[sampwidth]
fmt = "<" + fmt_size * channels
_data = array.array(fmt_size)
_data.fromfile(open(wav_fname, 'rb'), int(os.path.getsize(wav_fname)/_data.itemsize))
_data = _data.tolist()

# Get one note.
idata = _data
idata = idata[100:-1]
idata = np.array(idata)
N = len(idata)
# idata = a[150000:475000]

fidx = np.arange(0, N)
f = fidx * samprate * (1.0 / float(N))
w = 2 * np.pi * f
wn = fidx * (1.0 / float(N)) * 2 * np.pi

framesize = 64
frames = []

for i in range(len(idata) - framesize):
	frames.append(idata[i:i+framesize])

iframes = []
oframes = []
for i in np.arange(50000, 50100):
	frame = frames[i]
	iframes.append(frame)
	oframes.append(signal.lfilter([1.0], [1.0], frame))


# Process
b, a = signal.butter(2, 0.006, 'high')
# b, a = signal.butter(2, 0.1, 'high')
w, h = signal.freqz(b, a, worN=wn)

# Filter w lfilter.
odata = signal.lfilter(b, a, idata)

an = len(a)
bn = len(b)
y = np.full_like(idata, 0)

# IIR filter implementation.
for i in range(5, len(idata)):
	
	xidx = np.arange(i-bn+1, i+1)
	yidx = np.arange(i-an+1, i)
	y[i] = (np.sum(np.multiply(np.flip(b), idata[xidx])) - np.sum(np.multiply(np.flip(a[1:an]), y[yidx]))) / a[0]

# plt.figure()
# plt.plot(wn, np.abs(np.fft.fft(idata)) / np.max(np.abs(np.fft.fft(idata))), '+-')
# plt.plot(w, np.abs(np.fft.fft(odata)) / np.max(np.abs(np.fft.fft(odata))))
# plt.figure()
# plt.plot(w, np.abs(np.fft.fft(y)) / np.max(np.abs(np.fft.fft(y))))
# # plt.plot(w, np.abs(h) / np.max(abs(h)), '+-')

odata = y


	# y[bn - 1] = (np.multiply(a, xn) - np.multiply(b[0:(bn - 1)], y[0:(bn - 1)])) / b[bn]

# idx = 50000



# Write osginal to output.
owav = wave.open(owav_fname, 'w')
owav.setnchannels(channels)
owav.setsampwidth(sampwidth)
owav.setframerate(samprate)
for i in range(len(odata) - 1):
	data = struct.pack('<h', int(odata[i]))
	owav.writeframesraw(data)
owav.close()

# Play output file.
playsound(owav_fname)


IPython.embed()



# Read audio of a bass note being played.

# Play the audio back

# Apply static filter

# Apply sweeping filter
print("This line will be printed.")