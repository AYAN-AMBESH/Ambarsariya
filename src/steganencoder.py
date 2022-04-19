import os       # for verifying the path of files
import random   # for adding random values to unused values

from PIL import Image   # accessing pixel description
import bitarray         # converting to 8-bit representation
import numpy as np      # using array being faster than list

# colors to be used while printing on cli
colors = {
    'error': '\033[31;1m[x] ',
    'msg': '\033[36;1m ',
    'success': '\033[33;1m ',
    'white': '\033[37;1m '
}


def text_file_reader(file):
    """
    Reads a file through given path and returns its content
    :param: file
    :type: str
    :return: contents of text file
    :rtype: str
    """
    if os.path.exists(file):
        if len(file) == 0:
            raise ValueError("File is empty")
        with open(file, 'r') as f:
            return f.read()

    else:
        print(colors['error'] + "File path invalid xD")
        exit()


def strings_to_bit(sfile):
    """
    Converts the passed string to 8-bit representation
    :param: sfile
    :type: str
    :return: array of 0s and 1s based on 8 bit representation of
    :rtype: list
    """
    stryng = str(sfile)
    byt = bytes(stryng, encoding='utf-8')
    b = bitarray.bitarray()
    b.frombytes(byt)
    return list(b)


def image_reader(imagepath):
    """
    Returns an array of image description
    :param: imagepath
    :type: str
    :return: array
    :rtype: numpy.ndarray
    """
    if os.path.exists(imagepath):
        image = Image.open(imagepath)
        return np.array(image)
    else:
        print(colors['error'] + "File path invalid xD")
        exit()


def absolute_path_of(outpath):
    """
    Returns the absolute path for output according to the input entered
    :param: outpath
    :type: str
    :return: absolute path
    :rtype: str
    """
    if not os.path.isabs(outpath):
        outpath = os.path.abspath(outpath)
    if os.path.isdir(outpath):
        outpath += '\\lsb.png'
    if not outpath[-4:] == '.png':
        outpath += '.png'
    if not os.path.exists(os.path.dirname(outpath)):
        print(f"{colors['error']}File path invalid xD")
        exit()
    return outpath


def encoder(r, bit_array, i):
    """
    Encryption algorithm
    :param r: Value of Alpha
    :type r: Int
    :param bit_array: array of 8-bit rep
    :type bit_array: np.array
    :param i: iterated int
    :type i: int
    :return: value of new alpha (either 0 or 1)
    :rtype: int
    """
    bit = bin(r)
    lastbit = int(bit[-1])
    newlbit = lastbit & bit_array[i]
    return int(bit[:-1] + str(newlbit), base=2)


def stegencode():
    """
    Main function:
    Text File Input
    Image Path Input
    Output Path Input
    Changes the image description
    Saves new image
    """
    file = input(f"{colors['white']}Enter Path of Text File: ")
    sfile = text_file_reader(file)
    # sfile = contents of text file (str)

    bit_array = strings_to_bit(sfile)
    print(bit_array)
    # bit_array = list of 0s and 1s based on sfile's content in 8 bit representation

    image_path = input(f"\n{colors['white']}Enter Image Path: ")
    img = image_reader(image_path)

    outpath = input(f"\n{colors['white']}Enter Output Path: ")
    output_path = absolute_path_of(outpath)
    # output_path = absolute output path with png file name

    img.setflags(write=True)

    for x in range(len(img)):
        r, g, b, a = img[x, 0]

        if x < len(bit_array):
            a = 1
            a = encoder(a, bit_array, x)
        else:
            a = random.randint(0, 1)
        img[x, 0] = (r, g, b, a)

    image = Image.fromarray(np.uint8(img))
    print(img)

    image.save(output_path)
    print('\n' + colors['success'] + 'File saved to: ' + output_path)
