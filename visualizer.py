import matplotlib.pyplot as plt

def plot_histogram(data, column):
    values = [float(row[column]) for row in data if row[column]]
    plt.hist(values, bins=5)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_bar_chart(data, column):
    values = [float(row[column]) for row in data if row[column]]
    names = [row.get("name", f"Item{i}") for i, row in enumerate(data)]
    plt.bar(names, values)
    plt.title(f"Bar Chart of {column}")
    plt.xlabel("Items")
    plt.ylabel(column)
    plt.show()