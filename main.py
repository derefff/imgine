import sys
from PIL import Image, ImageFont, ImageDraw 


sys.path.append('./src')
from cli_parse import *
from image_actions import *

def usage():
    print("-in [<file1> ...]     - Include images passed a")
    print("-IN <direcotry>       - Use images in declared path to directory.")
    print("-out / -o <file>      - Set name of output image")
    print("-rows                 - Set number of rows, by default is set to 1")
    print("-cols                 - Set number of cols, by default is set to 2")
    print("-gap                  - Set gap between images, by default is set to 4")




def main():
    if sys.argv[1] == "-h":
        usage()
    else:
        arg_list = tokenize_cli_arguments()
        validate_cli_arguments(arg_list)

        apply_arg_list_to_settings(arg_list)
        cli_image_combine()


#for k,v in arg_list.items(): print(f" key: {k} value: {v}")
#print(arg_list)

if __name__=="__main__":
    main()