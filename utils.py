import random


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
    finding_radius = 10
    check_x = abs(position_drone[0] - position_person[0])
    check_y = abs(position_drone[1] - position_person[1])
    if check_x < finding_radius and check_y < finding_radius:
        return True
    return False


def generate_position(width, height):
    """This function generates a random position based on the boundaries of the grid."""
    random_position = [random.randint(0, width - 1), random.randint(0, width - 1), random.randint(0, height - 1)]
    return random_position

