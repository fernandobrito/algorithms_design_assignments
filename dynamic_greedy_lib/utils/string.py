def split_to_int(string, divider=' '):
    """
    Splits a string using split(divider) and convert all elements to integers

    :param string: string to be split
    :param divider: divider used on split. default: ' '
    :return: list with integers
    """
    return [int(number) for number in string.split(divider)]