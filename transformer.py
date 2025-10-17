def select_columns(data, columns):
    """Select specific columns from the dataset."""
    return [{col: row[col] for col in columns if col in row} for row in data]

def filter_rows(data, condition_func):
    """Filter rows based on a condition function."""
    return [row for row in data if condition_func(row)]

def sort_by(data, column, reverse=False):
    """Sort dataset by a specific column."""
    return sorted(data, key=lambda x: float(x[column]) if x[column] else 0, reverse=reverse)