import numpy as np
from pydub import AudioSegment
from pydub.utils import get_array_type

path_to_file = "C:\\Users\\Carlo Giustini\\effectspedal\\bassnotes.mp3"
sound = AudioSegment.from_file(file=path_to_file)
left = sound.split_to_mono()[0]


# Read audio of a bass note being played.

# Apply static filter

# Apply sweeping filter
print("This line will be printed.")