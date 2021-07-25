## About
**Ambarsariya** is a project on **stegnography** based upon **LSB(least significant bit)** algorithm.
The algorithm uses bitwise operation on the binary value of text file and binary values of RGB pixels of image.


## Installation 

#### Downloading and installing steps:
git clone the repository on your system: `git clone https://github.com/AYAN-AMBESH/Ambarsariya.git`.
install the requirements on your system: `pip install -r requirements.txt`.


## Usage and Commands
To use the program python 3 should be already installed on your system
The program is usable from command line interface
Commands used:
1. `python ambarsariya.py -h` for help menu.
2. `python ambarsariya.py -e` for encoding a text file inside an image.
3. `python ambarsariya.py -d` for decoding the message from image.


## Limitations
1. The program can only be used with an non transparent png image.
2. The text message to be encoded inside the image should not be more than 23 bytes.


