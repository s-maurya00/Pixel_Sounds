import argparse
import numpy as np
from scipy.io import wavfile
from PIL import Image

# set up the argument parser
parser = argparse.ArgumentParser(description='Convert an image file to an audio file')
parser.add_argument('--input_file', help='the input image file')
parser.add_argument('--output_file', help='the output audio file', default='output.wav')
args = parser.parse_args()

# load the image and convert to a NumPy array
img = Image.open(args.input_file).convert('L')
img_arr = np.array(img)

# normalize the image array to between -1 and 1
img_norm = (img_arr / 255) * 2 - 1

# set the frequency of the sound wave
freq = 44100

# create the time array for the sound wave
time_array = np.linspace(0, len(img_norm) / freq, len(img_norm))

# create the sound wave from the image array
audio = np.sin(2 * np.pi * freq * time_array * img_norm.T)

# save the sound wave to a file
wavfile.write(args.output_file, freq, audio)
print(f'Successfully saved {args.output_file}')
