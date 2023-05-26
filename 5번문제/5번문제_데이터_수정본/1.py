from PIL import Image
import numpy as np

def extract_bits_from_image(file_name):
    img = Image.open(file_name)
    img = img.convert("RGBA")

    width, height = img.size
    data = img.load()

    ret = []
    for y in range(height):
        for x in range(width):
            r, g, b, a = data[x, y]
            ret.append(a >> 7)

    return ret

def binarray_to_bytearray(bin):
    data = bytearray()
    for i in range(0, len(bin), 8):
        data.append(int(''.join(str(x) for x in bin[i:i+8]), 2))

    return data

bin_array = extract_bits_from_image('1.png')
byte_array = binarray_to_bytearray(bin_array)

with open('1.data', 'wb') as f:
    f.write(byte_array)