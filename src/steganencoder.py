import os
from PIL import Image
import bitarray
import sys
import numpy as np

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
    :param file:
    :type str:
    :return contents of text file:
    :rtype str:
    """
    if os.path.exists(file):
        if len(file) == 0:
            raise ValueError("File is empty")
        with open(file, 'r') as f:
            return f.read()

    else:
        print(colors['error'] + "File path invalid xD")
        sys.exit()


def strings_to_bit(sfile):
    """
    Converts the
    :param sfile:
    :type str:
    :return array of 0s and 1s based on 8 bit representation of :
    :rtype list:
    """
    stryng = str(sfile)
    byt = bytes(stryng, encoding='utf-8')
    b = bitarray.bitarray()
    b.frombytes(byt)
    return list(b)


def image_reader(imagepath):
    """
    Returns an array of image description
    :param imagepath:
    :type str:
    :return array:
    :rtype list:
    """
    if os.path.exists(imagepath):
        image = Image.open(imagepath)
        return np.array(image)
    else:
        print(colors['error'] + "File path invalid xD")
        sys.exit()


def filewriter(outpath):
    if not os.path.isabs(outpath):
        outpath = os.path.abspath(outpath)
    if os.path.isdir(outpath):
        outpath += '\\lsb.png'
    if not outpath[-4:] == '.png':
        outpath += '.png'
    if not os.path.exists(os.path.dirname(outpath)):
        print(f"{colors['error']}File path invalid xD")
        sys.exit()
    return outpath


def encoder(r, bit_array, i):
    bit = bin(r)
    lastbit = int(bit[-1])
    newlbit = lastbit & bit_array[i]
    return int(bit[:-1] + str(newlbit), 2)


def stegencode():

    file = input(f"{colors['white']}Enter Path of Text File: ")
    sfile = text_file_reader(file)
    # sfile = contents of text file (str)

    bit_array = strings_to_bit(sfile)
    # bit_array = list of 0s and 1s based on sfile's content in 8 bit representation
    print(bit_array)
    image_path = input(f"\n{colors['white']}Enter Image Path: ")
    img = image_reader(image_path)

    outpath = input(f"\n{colors['white']}Enter Output Path: ")
    opath = filewriter(outpath)

    img.setflags(write=True)
    i = 0
    for x in range(len(img)):
        r,g,b,a=img[x,0]
        
        nbrpixel = r
        nbgpixel = g
        nbbpixel = b
        nbapixel = 3

        # print(a,end='')
        if i<len(bit_array):       
            napixel = encoder(nbapixel,bit_array,i)
            i += 1
            img[x,0] = (nbrpixel,nbgpixel,nbbpixel,napixel)        

    image = Image.fromarray(np.uint8(img))

    image.save(opath)
    print('\n' + colors['success'] + 'File saved to: ' + opath)
