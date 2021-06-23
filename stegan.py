import os
from PIL import Image
import bitarray
import sys
import numpy as np

def listToString(s): 
    
    str1 = "" 
    ele=''
    for ele in s: 
        str1 += str(ele)
    return str1 

file=input("ENTER FILE NAME: ")
if os.path.exists(file):
    if (len(file)==0):
        raise ValueError("File is empty")    
    with open(file,'r') as f:
        String_of_File=f.readlines()
        y=len(file)

else:
    print("File path invalid xD")
    sys.exit()
    
stryng=str(String_of_File)
byt=bytes(stryng,encoding='utf-8')
b = bitarray.bitarray()
b.frombytes(byt)
bit_array=[int(i) for i in b]

imagepath= input("Enter image path: ")
if os.path.exists(imagepath):
    image=Image.open(imagepath)
    img = np.array(image)
else:
    print("File path invalid xD")
    sys.exit()

outpath = input("Enter output path: ")

if not os.path.isabs(outpath):
    outpath = os.path.abspath(outpath)
elif not os.path.exists(os.path.dirname(outpath)):
    print("File path invalid xD")
    sys.exit()
elif os.path.isdir(outpath):
    outpath += 'lsb.png'
    
if not outpath[-4:] == '.png':
    outpath += '.png'
    
img.setflags(write=1)
i=0
for x in range(len(img)):
    r,g,b=img[x,0]
    
    new_bit_red_pixel = 255
    new_bit_green_pixel = 255
    new_bit_blue_pixel = 255

    if i<len(bit_array):
        r_bit = bin(r)
        r_last_bit = int(r_bit[-1])
        r_new_last_bit = r_last_bit & bit_array[i]
        new_bit_red_pixel = int(r_bit[:-1]+str(r_new_last_bit),2)
        i += 1

    if i<len(bit_array):
        g_bit = bin(g)
        g_last_bit = int(g_bit[-1])
        g_new_last_bit = g_last_bit & bit_array[i]
        new_bit_green_pixel = int(g_bit[:-1]+str(g_new_last_bit),2)
        i += 1

    if i<len(bit_array):
        b_bit = bin(b)
        b_last_bit = int(b_bit[-1])
        b_new_last_bit = b_last_bit & bit_array[i]
        new_bit_blue_pixel = int(b_bit[:-1]+str(b_new_last_bit),2)
        i += 1

    img[x,0] = (new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel)
    

    
image=Image.fromarray(np.uint8(img))

image.save(outpath)
