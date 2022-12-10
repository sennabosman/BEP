from gmalthgtparser import HgtParser
hgt_file = 'N46E011.hgt'


def get_height_map():
    with HgtParser(hgt_file) as parser:
        height_map = []
        x = 0
        y = 0
        while y < 101:
            while x < 101:
                pos = parser.get_idx(1985 + y, 3013 + x)
                height = parser.get_value(pos)
                height_map.append((y, x, height))
                x += 1
            x = 0
            y += 1
    return height_map





