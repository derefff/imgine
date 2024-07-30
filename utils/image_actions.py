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

def adjust_size(images, w, h):
    adj_imgs = []
    for img in images:
        frac_w = abs(img.width - w)/2
        frac_h = abs(img.height - h)/2
        subrect = (frac_w,frac_h, frac_w+w, frac_h+h)
        print(f"frac_w{ frac_w} frac_h {frac_h}")
        adj_imgs.append(img.crop(subrect))
    
    return adj_imgs

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
    images = adjust_size(images, width, height)