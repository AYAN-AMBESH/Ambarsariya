import os
from PIL import Image
import bitarray
import sys
import numpy as np

def getcolours():
    return  {
            'error':'\033[31;1m[x] ',
            'msg':'\033[36;1m ',
            'success':'\033[33;1m ',
            'white':'\033[37;1m '
            }

def textfilereader(file):
    colors=getcolours()
    if os.path.exists(file):
        if (len(file)==0):
            raise ValueError("File is empty")    
        with open(file,'r') as f:
            return f.readlines()
            
    else:
        print(colors['error'] + "File path invalid xD")
        sys.exit()

def imagereader(imagepath):
    colors=getcolours()
    if os.path.exists(imagepath):
        image=Image.open(imagepath)
        return np.array(image)
    else:
        print(colors['error'] + "File path invalid xD")
        sys.exit()

def stringstobit(sfile):
    stryng=str(sfile)
    byt=bytes(stryng,encoding='utf-8')
    b = bitarray.bitarray()
    b.frombytes(byt)
    return [int(i) for i in b]
    

def filewriter(outpath):
    colors=getcolours()
    if not os.path.isabs(outpath):
        outpath = os.path.abspath(outpath)
    elif not os.path.exists(os.path.dirname(outpath)):
        print(colors['error'] + "File path invalid xD")
        sys.exit()
    elif os.path.isdir(outpath):
        outpath +='lsb.png'
        return outpath
        
    if not outpath[-4:] == '.png':
        outpath += '.png'
        return outpath

def encoder(r,bit_array,i):
    bit = bin(r)
    lastbit = int(bit[-1])
    newlbit = lastbit & bit_array[i]
    return int(bit[:-1]+str(newlbit),2)


def stegencode():

    colors= getcolours()

    file=input(colors['white'] + "ENTER FILE NAME: ")
    
    sfile=textfilereader(file)
    
    bit_array=stringstobit(sfile)

    imagepath= input(colors['white'] + "Enter image path: ")

    img=imagereader(imagepath)

    outpath = input(colors['white'] + "Enter output path: ")

    opath=filewriter(outpath)
        
    img.setflags(write=1)
    i=0
    for x in range(len(img)):
        r,g,b=img[x,0]
        
        nbrpixel = 255
        nbgpixel = 255
        nbbpixel = 255

        if i<len(bit_array):       
            nbrpixel = encoder(r,bit_array,i)
            i += 1

        if i<len(bit_array):
            nbgpixel = encoder(g,bit_array,i)
            i += 1

        if i<len(bit_array):
            nbbpixel = encoder(b,bit_array,i)
            i += 1

        img[x,0] = (nbrpixel,nbgpixel,nbbpixel)
        

        
    image=Image.fromarray(np.uint8(img))

    image.save(opath)
    print('\n' + colors['success'] + 'File saved to: ' + opath)
