import extcolors
import sys

colors, pixel_total = extcolors.extract("gameboy.png")

# extcolors.image_result(colors, 150, "gameboy.png")



for color_code, pixel_count in colors:
#     color_percent = float(pixel_count) / float(pixel_total) * 100.0
#     print("{0:15}:{1:>7}% ({2})".format(str(color_code), "{0:.2f}".format(color_percent), pixel_count))
# print("\nPixels in output: {} of {}".format(sum([c[1] for c in colors]), pixel_total))
    R = color_code[0]
    G = color_code[1]
    B = color_code[2]
    print(R,G,B, pixel_count)
