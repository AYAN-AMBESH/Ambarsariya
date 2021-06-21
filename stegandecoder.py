from PIL import Image
import numpy as np
import binascii
imagepath=input("Enter image path: ")
image = Image.open(imagepath)


extracted= ''

i=0
img=np.array(image)
for x in range(73):
    r,g,b = img[x,0]
    pixel=r,g,b
    
    if i<216:
        print(r)
        if r==254:
            extracted+='0'
        elif r==255:
            extracted+='1'    

    if i<216:
        
        print(r)
        if g==254:
            extracted+='0'
        elif g==255:
            extracted+='1'    

    if i<216:

        print(r)
        if b==254:
            extracted+='0'
        elif b==255:
            extracted+='1'    

print(extracted)