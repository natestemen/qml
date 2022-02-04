import csv
from random import sample

lines = []
class_0_count = 0
with open("banknote_auth_full.txt", mode="r") as f:
    csv_file = csv.reader(f)

    max_0 = 0
    for i, line in enumerate(csv_file):
        if line[-1] == "0":
            class_0_count += 1
            max_0 = i
        lines.append(line)

class_0_percent = int(round(100 * class_0_count / len(lines)))
class_1_percent = 100 - class_0_percent

class_0_data = sample(lines[:max_0], class_0_percent)
class_1_data = sample(lines[max_0 + 1 :], class_1_percent)

all_data = class_0_data + class_1_data

with open("banknote_auth_100.csv", mode="w") as f:
    fieldnames = ["variance", "skewness", "curtosis", "entropy", "class"]
    csv_writer = csv.writer(f)
    csv_writer.writerow(fieldnames)
    csv_writer.writerows(sample(all_data, 100))
