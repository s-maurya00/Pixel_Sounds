import argparse
import numpy as np
from scipy.io import wavfile
from PIL import Image

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Convert an audio file to an image file')

# Add the command line arguments
parser.add_argument('--input_file', type=str, required=True, help='input audio file path')
parser.add_argument('--output_file', type=str, help='output image file path', default='output.tiff')

# Parse the arguments
args = parser.parse_args()

# Load the audio file
sample_rate, audio = wavfile.read(args.input_file)

# Reshape the audio data into a 2D array
n_pixels = int(len(audio) / sample_rate * 100)
audio_arr = np.reshape(audio, (n_pixels, -1))

# Normalize the array
audio_arr = audio_arr / np.max(np.abs(audio_arr))

# Convert the array to an image
img = Image.fromarray(np.uint8(audio_arr * 255))

# Save the image file
img.save(args.output_file, format='TIFF')
print(f"Image file saved to {args.output_file}")
