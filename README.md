# PixelSounds

PixelSounds is a project that converts images into audio signals and vice versa.

## Prerequisites

- Python 3.10.4 or higher
- `pip` package manager

## Installation

1. Clone the repository to your local machine or download zip project:
```
git clone https://github.com/s-maurya00/Pixel_Sounds
```
2. Change to the project directory:
```
cd Pixel_Sounds
```

## Environment Setup

1. Create a virtual environment using command:
```
python -m venv env
```
2. Activate the virtual environment using command:
```
.\env\Scripts\activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

### Image to Audio

To generate an audio signal from an image file, run the following command:
```
python image_to_audio.py --input input_image.png --output output_audio.wav
```

- `--input` specifies the input image file path.
- `--output` specifies the output audio file path.

The output audio file will be saved in WAV format.


### Audio to Image

To generate an image file from an audio file, run the following command:
```
python audio_to_image.py --input input_audio.wav --output output_image.png
```


- `--input` specifies the input audio file path.
- `--output` specifies the output image file path.

The output image file will be saved in PNG format.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
