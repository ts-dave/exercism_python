EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_of_layers: int):
    """Calculate preparation time in minutes

    :param num_of_layers: int number of layers of lasagna
    :return: int time lasagna will be ready from

    Function that takes the number of layers of lasagna and returns
    how many minutes it will take all layers to be ready
    """
    return PREPARATION_TIME * num_of_layers


def elapsed_time_in_minutes(num_of_layers: int, elapsed_bake_time: int):
    """Calculate elapsed time in minutes
    :param: num_of_layers
    :param: elapsed_bake_time

    Function takes number of layers and elapsed bake time
    and returns the total elapsed time in minutes
    """
    return (2*num_of_layers) + elapsed_bake_time
