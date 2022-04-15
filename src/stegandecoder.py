from PIL import Image
import numpy as np
import os
import sys


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
        sys.exit()

    extracted = ''

    i = 0
    img = np.array(image)
    for x in range(len(img)):
        r,g,b,a=img[x,0]
        # print(a,end='')
        if i <456:# this value is len of bit array, if you change your text in abc.txt then change accordingly the length of bit array here
            rbit=bin(a)
            rlbit=rbit[-1]
            extracted+=str(rlbit)   
            i+=1

    chars = []
    for i in range(len(extracted) // 8):
        byte = extracted[i * 8:(i + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    print('\n' + colors['success'] + ''.join(chars[2:-2]))
