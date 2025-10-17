def data_summary(data):
    """Print summary: total rows, empty/non-empty counts."""
    if not data:
        print("No data available.")
        return
    total_rows = len(data)
    print(f"Total Rows: {total_rows}")
    columns = data[0].keys()
    for col in columns:
        non_empty = sum(1 for row in data if row[col])
        empty = total_rows - non_empty
        print(f"{col}: Non-empty={non_empty}, Empty={empty}")