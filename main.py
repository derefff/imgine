import sys
from PIL import Image, ImageFont, ImageDraw 


sys.path.append('./src')
from cli_parse import *
from image_actions import *

def usage():
    print("todo: print how to use this program")


arg_list = tokenize_cli_arguments()
validate_cli_arguments(arg_list)

apply_arg_list_to_settings(arg_list)
cli_image_combine()

#for k,v in arg_list.items(): print(f" key: {k} value: {v}")
#print(arg_list)