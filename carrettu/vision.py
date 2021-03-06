import webcolors
from PIL import Image

# pass a numpy array and checks to see how much black is inside (assuming black = 0)

# TODO: determine if a whole array of RGB values is green or not (or somehow send information saying if there's a lot of green or not)
def examine_image(image):
    pass

# this takes in a tuple (something like (0,0,0) which is an RGB value, and returns either "green" or "not green" [this could be true/false too])
def examine_color_tuple(triple):
    try:
        color_name = webcolors.rgb_to_name(triple)
    except ValueError:
        closest_name = closest_color(triple)
        color_name = None
    if (color_name == None):
        if 'green' in closest_name:
            return 'green'
        else:
            return 'not green'
    else:
        if 'green' in color_name:
            return 'green'
        else:
            return 'not green'

# if color is not standard CSS value, changes to standard CSS value
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def dominant_colors(image):
    image = Image.fromarray(image, 'RGB')
    colors = image.getcolors(maxcolors=512)
    if colors is None:
        return colors
    colors = sorted(colors, key=lambda c: c[0])
    return [c[1] for c in reversed(colors[-3:])]

def main():
    test = (0, 255, 129)
    print(examine_image(test))

if __name__ == '__main__':
    main()
