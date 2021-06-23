from PIL import Image
import numpy as np
import os
import sys

def stegdecode():
    imagepath=input("Enter image path: ")
    image = Image.open(imagepath)


    extracted= ''

    i=0
    img=np.array(image)
    for x in range(73):
        r,g,b = img[x,0]
        pixel=r,g,b
        
        if i<216:
            if r==254:
                extracted+='0'
            elif r==255:
                extracted+='1'    

        if i<216:
            if g==254:
                extracted+='0'
            elif g==255:
                extracted+='1'    

        if i<216:
            if b==254:
                extracted+='0'
            elif b==255:
                extracted+='1'    


    chars = []
    for i in range(len(extracted)//8):
        byte = extracted[i*8:(i+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    print(chars[2:-2])
