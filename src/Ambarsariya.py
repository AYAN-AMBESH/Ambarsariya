import os
import sys
from src import steganencoder
from src import stegandecoder

def main():
    colors = {
    'error':'\033[31;1m[x] ',
    'msg':'\033[36;1m ',
    'success':'\033[33;1m ',
    'white':'\033[37;1m '
    }
    
    print(colors['msg'] + '''

    ░█████╗░███╗░░░███╗██████╗░░█████╗░██████╗░░██████╗░█████╗░██████╗░██╗██╗░░░██╗░█████╗░
    ██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗
    ███████║██╔████╔██║██████╦╝███████║██████╔╝╚█████╗░███████║██████╔╝██║░╚████╔╝░███████║
    ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║██╔══██╗░╚═══██╗██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║
    ██║░░██║██║░╚═╝░██║██████╦╝██║░░██║██║░░██║██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░██║
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝

                                                        By Ayan Ambesh (ambesh12k@gmail.com)
    ''')

    if '-d' in sys.argv and '-e' in sys.argv:
        print(colors['error'] + 'Can\'t use both -d and -e')
        sys.exit()
        
    elif '-d' in sys.argv:
        stegandecoder.stegdecode()
        
    elif '-e' in sys.argv:
        steganencoder.stegencode()

    elif '-h' in sys.argv:
        print(colors['white'] + 'Usage:\n -e to embed\n -d to decode\n\n Example: python3 ambarsariya.py -e')

    else:
        print(colors['error'] + 'No valid option specified\nBye!')
        sys.exit()

if __name__=="__main__":
    main()