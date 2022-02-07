# %%
import csv
import matplotlib.pyplot as plt
from itertools import combinations

# %%
features = ["variance", "skewness", "curtosis", "entropy"]
data = {"variance": [], "skewness": [], "curtosis": [], "entropy": [], "class": []}
with open("banknote_auth_100.csv") as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        data["variance"].append(float(row["variance"]))
        data["skewness"].append(float(row["skewness"]))
        data["curtosis"].append(float(row["curtosis"]))
        data["entropy"].append(float(row["entropy"]))
        data["class"].append(int(row["class"]))

# %%
plt.figure(figsize=(15, 12))
plt.subplots_adjust(hspace=0.3)
plt.suptitle("Feature comparisons", fontsize=18, y=0.95)

for n, (f1, f2) in enumerate(combinations(features, 2)):
    ax = plt.subplot(3, 2, n + 1)
    ax.scatter(data[f1], data[f2], c=data["class"])

    ax.set_xlabel(f1)
    ax.set_ylabel(f2)

plt.show()

# %%
full_data = {"variance": [], "skewness": [], "curtosis": [], "entropy": [], "class": []}
with open("banknote_auth_full.txt") as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        full_data["variance"].append(float(row[0]))
        full_data["skewness"].append(float(row[1]))
        full_data["curtosis"].append(float(row[2]))
        full_data["entropy"].append(float(row[3]))
        full_data["class"].append(int(row[4]))


# %%
plt.figure(figsize=(15, 12))
plt.subplots_adjust(hspace=0.3)
plt.suptitle("Feature comparisons", fontsize=18, y=0.95)

for n, (f1, f2) in enumerate(combinations(features, 2)):
    ax = plt.subplot(3, 2, n + 1)
    ax.scatter(full_data[f1], full_data[f2], c=full_data["class"])

    ax.set_xlabel(f1)
    ax.set_ylabel(f2)

plt.show()

# %%
import pandas as pd

# %%
df = pd.read_csv(
    "banknote_auth_full.txt",
    names=["variance", "skewness", "curtosis", "entropy", "class"],
)

# %%
inner = df[df["variance"].between(-2.5, 2)]

# %%
plt.figure(figsize=(15, 12))
plt.subplots_adjust(hspace=0.3)
plt.suptitle(
    "Feature comparisons (for data with variance in [-2.5, 2])", fontsize=18, y=0.95
)

for n, (f1, f2) in enumerate(combinations(features, 2)):
    ax = plt.subplot(3, 2, n + 1)
    ax.scatter(inner[f1], inner[f2], c=inner["class"])

    ax.set_xlabel(f1)
    ax.set_ylabel(f2)

plt.show()

# %%
fig = plt.figure(figsize=(15, 12))
plt.suptitle(
    "3D Feature comparisons (for data with variance in [-2.5, 2])", fontsize=18, y=0.95
)

for n, (f1, f2, f3) in enumerate(combinations(features, 3)):
    ax = fig.add_subplot(2, 2, n + 1, projection="3d")
    ax.scatter(inner[f1], inner[f2], inner[f3], c=inner["class"])

    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_zlabel(f3)

plt.show()

# %%
