from PIL import Image, ImageFont, ImageDraw
import os

settings = {
    'images': [],
    'rows': 1,
    'cols': 2,
    'gapX': 4,
    'gapY': 4,
    'font-size': 14,
    'output-name': 'output.png',
    'overlay-numbers': False,
    'overlay-letters': False,
    'inverse-font-color': False,

}

def apply_arg_list_to_settings(arg_list):
    for arg in arg_list:
        for opt, value in arg.items():
            match opt:
                case "-rows":
                    settings["rows"] = int(value[0])
                case "-cols":
                    settings["cols"] = int(value[0])
                case "-gap":
                    settings["gapX"] = int(value[0])
                    settings["gapY"] = int(value[0])
                case "-fs" | "-fontsize":
                    settings["font-size"] = int(value[0])
                case "-in":
                    if "-IN" not in arg:
                        settings["images"] = value
                case "-IN":
                    for file in os.listdir(value[0]):
                        if not os.path.splitext(file)[-1] in [".png",".jpeg",".jpg"]:
                            continue
                        else:
                            settings['images'].append(value[0]+"/"+file)

                case "-out" | "-o":
                    settings["output-name"] = value[0]
                case "-on":
                    settings["overlay-numbers"] = True
                    settings["overlay-letters"] = False
                case "-oa":
                    settings["overlay-letters"] = True
                    settings["overlay-numbers"] = False
                case "-ifc" | "-inversefontcolor":
                    settings["inverse-font-color"] = True


    #print(settings)
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
        adj_imgs.append(img.crop(subrect))

    return adj_imgs

def add_overlay(images):
    font_size = int(settings["font-size"])

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
        #font = ImageFont.truetype("LiberationSans-Regular.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    for i, img in enumerate(images):
        draw = ImageDraw.Draw(img)
        text = ""

        if settings['overlay-numbers']:
            text = f"{i + 1})"
        if settings['overlay-letters']:
            text = f"{chr(97 + i)})"  # 97 -> ASCII 'a'

        if text:
            fill_color = "white" if settings["inverse-font-color"] else "black"
            draw.text((15,15), text, fill=fill_color, font=font)

    return images

def merge(images, w, h):
    width = w * settings['cols'] + settings['gapX'] * (settings['cols']-1)
    height = h * settings['rows'] + settings['gapY'] * (settings['rows']-1)

    output = Image.new("RGB", (width, height), (255,255,255))

    current_column = 0
    current_row = 0

    for i in range(len(images)):
        x = current_column * (w + settings['gapX'])
        y = current_row * (h + settings['gapY'])

        output.paste(images[i], (x, y))

        current_column += 1
        if current_column >= settings['cols']:
            current_column  = 0
            current_row += 1

    return output


def cli_image_combine():
    # here will go everyting
    images = []
    for i in settings['images']:
        images.append(load_img(i))

    width, height = determine_size(images)
    images = adjust_size(images, width, height)

    if settings['overlay-numbers'] or settings['overlay-letters']:
      images = add_overlay(images)

    merge(images, width, height).save(settings['output-name'])