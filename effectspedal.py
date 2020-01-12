import numpy as np
import matplotlib.pyplot as plt
import IPython
import wave
import struct
import array
import os
from playsound import playsound
import scipy.signal as signal

wav_fname = "./bassnotes.wav"
owav_fname = "./bassnotes_one.wav"

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
a = array.array(fmt_size)
a.fromfile(open(wav_fname, 'rb'), int(os.path.getsize(wav_fname)/a.itemsize))
a = a.tolist()

# Get one note.
idata = a[150000:475000]

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

N = len(idata)
# w = (2 * np.pi / float(N)) * np.arange(0, N)
w = np.arange(0, N)
b, a = signal.butter(3, [0.2, 0.8], 'bandpass')
w, h = signal.freqs(b, a, worN=w)


odata = signal.lfilter(b, a, idata)

plt.plot(w, np.abs(np.fft.fft(idata)) / np.max(np.abs(np.fft.fft(idata))))
plt.plot(w, np.abs(np.fft.fft(odata)) / np.max(np.abs(np.fft.fft(odata))))
plt.plot(w, np.abs(h) / np.max(abs(h)))

# idx = 50000


# Process
# odata = idata


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