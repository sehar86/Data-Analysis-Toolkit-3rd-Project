from toolkit.loader import read_csv
from toolkit.cleaner import drop_missing
from toolkit.stats import mean
from toolkit.visualizer import plot_histogram
from toolkit.summary import data_summary

data = read_csv("data/sample.csv")

data_summary(data)

data = drop_missing(data, "marks")

marks = [float(row["marks"]) for row in data]

total_marks = sum(marks)
average_marks = mean(data, "marks")

print("\n--- Marks Analysis ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

plot_histogram(data, "marks")