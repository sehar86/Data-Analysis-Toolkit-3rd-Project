import statistics

def mean(data, column):
    values = [float(row[column]) for row in data if row[column]]
    return statistics.mean(values)

def median(data, column):
    values = [float(row[column]) for row in data if row[column]]
    return statistics.median(values)

def mode(data, column):
    values = [float(row[column]) for row in data if row[column]]
    return statistics.mode(values)

def variance(data, column):
    values = [float(row[column]) for row in data if row[column]]
    return statistics.variance(values)

def correlation(data, col1, col2):
    x = [float(row[col1]) for row in data if row[col1] and row[col2]]
    y = [float(row[col2]) for row in data if row[col1] and row[col2]]
    n = len(x)
    if n == 0:
        return None
    mean_x, mean_y = statistics.mean(x), statistics.mean(y)
    num = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    den = (sum((x[i]-mean_x)**2 for i in range(n)) * sum((y[i]-mean_y)**2 for i in range(n))) ** 0.5
    return num/den if den else 0