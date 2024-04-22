import re

from discordalerts.lib.colors import GREEN, RED, ORANGE, color_distance, closest_color, colored_text
from discordalerts.lib.constants import Signal

SIGNAL_TO_RGB_MAPPING = {
    Signal.BUY: GREEN,
    Signal.SELL: RED,
    Signal.HOLD: ORANGE,
}

price_re = re.compile(r'\$(\d+\.\d+)')


def price_levels_from_text(text: str):
    """Extract price levels from text."""
    m = price_re.findall(text)
    if len(m) == 0:
        return []
    return [float(price) for price in m]


def print_signal_color_classification(signal_to_rgb_mapping: dict):
    for signal, colors in signal_to_rgb_mapping.items():
        print(f"{signal}: {len(colors)} colors")
        for color in colors:
            # print colored text
            color_name = closest_color(color)
            # print distance from all signal colors
            color_dist = ""
            for signal, signal_color in SIGNAL_TO_RGB_MAPPING.items():
                color_dist += f"{colored_text(color_distance(color, signal_color), signal_color)} "
            print(f"{color[0]},{color[1]},{color[2]}: {colored_text(color_name, color)} | {color_dist}")


def get_stock_signal_from_rgb(r, g, b) -> str:
    # get signal of the closest color
    closest_signal = None
    closest_distance = None
    for signal, signal_color in SIGNAL_TO_RGB_MAPPING.items():
        distance = color_distance(signal_color, (r, g, b))
        if closest_distance is None or distance < closest_distance:
            closest_distance = distance
            closest_signal = signal
    return closest_signal


def get_stock_signal_from_border_color(border_color: str) -> str:
    m = re.match(r'rgb\((\d+), (\d+), (\d+)\)', border_color)
    if m is None or len(m.groups()) != 3:
        raise ValueError(f'Unexpected border color: {border_color}')
    r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return get_stock_signal_from_rgb(r, g, b)
