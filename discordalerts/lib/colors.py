import webcolors

RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


def closest_color(requested_color):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_color_name(requested_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
        actual_name = None
    return actual_name, closest_name


def color_distance(color1, color2):
    return sum([(a - b) ** 2 for a, b in zip(color1, color2)])

def get_rgb_from_hex(hex_color):
    return webcolors.hex_to_rgb(hex_color)


def colored_text(text, color):
    return f'\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m'
