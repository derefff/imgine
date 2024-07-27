import sys
from PIL import Image, ImageFont, ImageDraw 


sys.path.append('./utils')
from cli_parse import *

def usage():
    print("todo: print how to use this program")

tokenize_cli_arguments()
validate_cli_arguments()

#for k,v in arg_list.items(): print(f" key: {k} value: {v}")
#print(arg_list)