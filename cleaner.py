def drop_missing(data, column):
    """Remove rows with missing values in a specific column."""
    return [row for row in data if row.get(column)]

def fill_missing(data, column, value):
    """Fill missing values with a default value."""
    for row in data:
        if not row.get(column):
            row[column] = value
    return data