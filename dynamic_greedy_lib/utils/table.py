def initialize(rows, columns, default=None):
    """
    Initialize a table with n rows and m columns, all filled
    with default value.

    :param rows: number of rows
    :param columns: number of columns
    :param default: value to fill table (default is None)
    :return: array of arrays
    """
    table = []

    for row in range(rows):
        # Create empty row
        table.append([])

        # Create column entries
        for column in range(columns):
            table[row].append(default)

    return table
