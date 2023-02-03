import random
from variables import visibility, wind, temperature
from gmalthgtparser import HgtParser
hgt_file = 'N46E011.hgt'


def get_height_map():
    with HgtParser(hgt_file) as parser:
        height_map = []
        x = 0
        y = 0
        while y < 100:
            while x < 100:
                pos = parser.get_idx(3013 + y, 1985 + x)
                height = parser.get_value(pos)
                height_map.append((y, x, height))
                x += 1
            x = 0
            y += 1
    return height_map


def finding_radius(visibility, drone):
    """This function returns the finding radius based on the meters of visibility, depending on fog."""

    if drone == 1 or drone == 4 or drone == 5:
        standard_radius = 2
    elif drone == 7:
        standard_radius = 3.5
    elif drone == 2:
        standard_radius = 2.5
    elif drone == 3:
        standard_radius = 3
    else:
        standard_radius = 1.5

    if visibility == 500:
        visibility_coefficient = 1
    elif visibility == 250:
        visibility_coefficient = 0.8
    elif visibility == 100:
        visibility_coefficient = 0.75
    else:
        return print("Please use one of the following values for the view: 100, 250 or 500.")

    return standard_radius * visibility_coefficient


def battery_decrement(wind, temperature, drone):
    """This function returns the average battery decrement per step based on the wind speed and temperature."""

    if drone == 1:
        standard_decrement = 0.000538
    elif drone == 2:
        standard_decrement = 0.000370
    elif drone == 3:
        standard_decrement = 0.000397
    elif drone == 4:
        standard_decrement = 0.000407
    elif drone == 5:
        standard_decrement = 0.000417
    elif drone == 6:
        standard_decrement = 0.000303
    else:
        standard_decrement = 0.000439

    if wind == 10:
        wind_coefficient = 1
    elif wind == 25:
        wind_coefficient = 1.1
    elif wind == 35:
        wind_coefficient = 1.15
    else:
        return print("Please use one of the following values for the wind: 10, 25 or 35.")

    if temperature == -15:
        temperature_coefficient = 1.1
    elif temperature == 0:
        temperature_coefficient = 1.05
    elif temperature == 20:
        temperature_coefficient = 1
    else:
        return print("Please use one of the following values for the temperature: -15, 0 or 20.")

    return standard_decrement * wind_coefficient * temperature_coefficient


def found_person(position_drone, position_person, drone):
    """This function checks if the missing person is within the finding radius of the drone."""
    finding_visibility = finding_radius(visibility, drone)
    check_x = abs(position_drone[0] - position_person[0])
    check_y = abs(position_drone[1] - position_person[1])
    if check_x < finding_visibility and check_y < finding_visibility:
        return True
    return False


def generate_position(width, height):
    """This function generates a random position based on the boundaries of the grid."""
    random_position = [random.randint(0, width - 1), random.randint(0, width - 1), random.randint(0, height - 1)]
    return random_position

