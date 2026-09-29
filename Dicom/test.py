import numpy as np
import pydicom
from PIL import Image
import os



def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm']:
                names.append(filename)

    return names

print(get_names('Test_Images'))

def convert_dcm_jpg(name):

    im = pydicom.dcmread('Test_Images/' + name)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255
    final_image = np.uint8(rescaled_image)

    final_image = Image.fromarray(final_image)
    return final_image

names = get_names('Test_Images')
for name in names:
    image = convert_dcm_jpg(name)
    image.save(name + '.jpg')