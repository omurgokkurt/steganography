from PIL import Image
import sys


def encode(image, text_file):
    text = open(text_file.strip('.txt') + '.txt', 'r').read()
    file = image.strip(".png")
    img = Image.open(file + ".png")
    width, height = img.size
    max_char = int(width * height * 0.75)
    print("max text length:", max_char)
    c = 0

    if len(text) > max_char:
        print("text too long")
        return

    new_image = Image.new('RGB', (width, height), color=(0, 0, 0))
    pixels = new_image.load()
    text_bin = ""

    for char in text:
        text_bin += bin(ord(char))[2:].zfill(8)

    for y in range(height):
        for x in range(width):
            temp_pixel = []
            for pixel_rgb in img.getpixel((x, y)):
                if c < len(text_bin) / 2:
                    temp_pixel.append(pixel_rgb - pixel_rgb % 4 + int(text_bin[c * 2:c * 2 + 2], 2))
                    c += 1
                else:
                    temp_pixel.append(pixel_rgb - pixel_rgb % 4)  # Fill the rest with ASCII Null character

            pixels[x, y] = tuple(temp_pixel)

    new_image.save(file + "_encoded.png")
    print("saved as '"+ file + "_encoded.png'")


def decode_to_bin(image):
    file = image.strip(".png")
    img = Image.open(file + ".png")
    width, height = img.size
    text_bin = ""
    c = 0

    for y in range(height):
        for x in range(width):
            for pixel_rgb in img.getpixel((x, y)):
                text_bin += bin(pixel_rgb % 4)[2:].zfill(2)
                if (pixel_rgb % 4) == 0:
                    c += 1
                else:
                    c = 0
                if c > 4:  # Stop reading after reaching Null
                    return text_bin
    return text_bin


def decode(image):
    text_bin = decode_to_bin(image)
    file = open(image.strip('.png') + '_text.txt', 'w')
    text = ""
    for i in range(int(len(text_bin)/8)-1):
        text += chr(int(text_bin[i*8:i*8+8], 2))
    file.write(text)
    print("saved as '"+image.strip('.png') + '_text.txt' + "'")
    file.close()


if sys.argv[1] == 'encode':
    encode(sys.argv[2], sys.argv[3])

elif sys.argv[1] == 'decode':
    decode(sys.argv[2])
