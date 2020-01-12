import numpy as np
import matplotlib.pyplot as plt
import IPython
import wave
import struct
import array
import os

wav_fname = "./bassnotes.wav"

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

sizes = {1: 'B', 2: 'h', 4: 'i'}
wav = wave.open(wav_fname)
channels = wav.getnchannels()
fmt_size = sizes[wav.getsampwidth()]
fmt = "<" + fmt_size * channels
a = array.array(fmt_size)
a.fromfile(open(wav_fname, 'rb'), int(os.path.getsize(wav_fname)/a.itemsize))

IPython.embed()

# Read audio of a bass note being played.

# Apply static filter

# Apply sweeping filter
print("This line will be printed.")