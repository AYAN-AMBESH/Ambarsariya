from PIL import Image   # accessing pixel description
import numpy as np      # using array being faster than list
import os               # for verifying the path of files


def stegdecode():
    colors = {
        'error': '\033[31;1m[x] ',
        'msg': '\033[36;1m ',
        'success': '\033[33;1m ',
        'white': '\033[37;1m '
    }

    imagepath = input(colors['white'] + "Enter image path: ")
    if os.path.exists(imagepath):
        image = Image.open(imagepath)
    else:
        print(colors['error'] + 'File path invalid xD')
        exit()

    extracted = ''
    n = int(input("Enter length of message: "))  # Enter the length of the message

    img = np.array(image)
    for x in range(len(img)):
        r, g, b, a = img[x, 0]
        # print(a,end='')

        if x < (n*8):
            rbit = bin(a)
            rlbit = rbit[-1]
            extracted += str(rlbit)
            continue
        break

    chars = ''
    for i in range(len(extracted) // 8):
        byte = extracted[i * 8:(i + 1) * 8]
        # slicing the string extracted from i*8 to (i+1)*8
        chars += chr(int(byte, base=2))

    print('\n' + colors['success'] + chars)
