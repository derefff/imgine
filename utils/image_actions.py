from PIL import Image, ImageFont, ImageDraw 

settings = {
    'images': [],
    'image-folder': ''
    'rows': 2,
    'cols': 2,
    'gapX': 4,
    'gapY': 4,
    'output-name': 'output.png'
}

def load_img(name):
    return Image.open(name)

#getting the min width and min height 
def determine_size(images):
    width = images[0].width
    height = images[0].height
    for img in images:
        if img.width < width:
            width = img.width
        
        if img.height < height:
            height = img.height

    return width, height

'''
1. load images
2. dtermine/adjust image sizes
3. marge and save images
'''

def cli_image_combine():
    # here will go everyting
    images = []

    for i in settings['images']:
        images.append(load_img(i))

    width, height = determine_size(images)