from PIL import Image, ImageFont, ImageDraw 


def load_img(name):
    return Image.open(name)