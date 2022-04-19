import sys
import steganencoder
import stegandecoder

project_name = '''

    ░█████╗░███╗░░░███╗██████╗░░█████╗░██████╗░░██████╗░█████╗░██████╗░██╗██╗░░░██╗░█████╗░
    ██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗
    ███████║██╔████╔██║██████╦╝███████║██████╔╝╚█████╗░███████║██████╔╝██║░╚████╔╝░███████║
    ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║██╔══██╗░╚═══██╗██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║
    ██║░░██║██║░╚═╝░██║██████╦╝██║░░██║██║░░██║██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░██║
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝

                                                        By Ayan Ambesh (ambesh12k@gmail.com)
    '''

help_menu = '''
Usage:
-e to embed
-d to decode

Example: python3 ambarsariya.py -e'''


def main():
    colors = {
        'error': '\033[31;1m[x] ',
        'msg': '\033[36;1m ',
        'success': '\033[33;1m ',
        'white': '\033[37;1m '
    }

    print(colors['msg'] + project_name)

    if '-d' in sys.argv and '-e' in sys.argv:
        print(colors['error'] + "Both -d and -e cannot be used together")
        sys.exit()

    elif '-d' in sys.argv:
        stegandecoder.stegdecode()

    elif '-e' in sys.argv:
        steganencoder.stegencode()

    elif '-h' in sys.argv:
        print(colors['white'] + help_menu)

    else:
        print(colors['error'] + 'No valid option specified\nBye!')
        sys.exit()


if __name__ == "__main__":
    main()
