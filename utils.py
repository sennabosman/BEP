import random
from variables import visibility, wind, temperature
from gmalthgtparser import HgtParser
hgt_file = 'N46E011.hgt'


def get_height_map():
    with HgtParser(hgt_file) as parser:
        height_map = []
        x = 0
        y = 0
        while y < 101:
            while x < 101:
                pos = parser.get_idx(3013 + y, 1985 + x)
                height = parser.get_value(pos)
                height_map.append((y, x, height))
                x += 1
            x = 0
            y += 1
    return height_map


def finding_radius(visibility):
    """This function returns the finding radius based on the meters of visibility, depending on fog."""
    standard_radius = 1

    if visibility == 500:
        visibility_coefficient = 10
    elif visibility == 250:
        visibility_coefficient = 6
    elif visibility == 100:
        visibility_coefficient = 3
    else:
        return print("Please use one of the following values for the view: 100, 250 or 500.")

    return standard_radius * visibility_coefficient


def battery_decrement(wind, temperature):
    """This function returns the average battery decrement per step based on the wind speed and temperature."""
    standard_decrement = 0.001

    if wind == 10:
        wind_coefficient = 1
    elif wind == 25:
        wind_coefficient = 1.1
    elif wind == 35:
        wind_coefficient = 1.3
    else:
        return print("Please use one of the following values for the wind: 10, 25 or 35.")

    if temperature == -15:
        temperature_coefficient = 1.5
    elif temperature == 0:
        temperature_coefficient = 1.3
    elif temperature == 20:
        temperature_coefficient = 1
    else:
        return print("Please use one of the following values for the temperature: -15, 0 or 20.")

    return standard_decrement * wind_coefficient * temperature_coefficient


def found_person(position_drone, position_person):
    """This function checks if the missing person is within the finding radius of the drone."""
    finding_visibility = finding_radius(visibility)
    check_x = abs(position_drone[0] - position_person[0])
    check_y = abs(position_drone[1] - position_person[1])
    if check_x < finding_visibility and check_y < finding_visibility:
        return True
    return False


def generate_position(width, height):
    """This function generates a random position based on the boundaries of the grid."""
    random_position = [random.randint(0, width - 1), random.randint(0, width - 1), random.randint(0, height - 1)]
    return random_position

