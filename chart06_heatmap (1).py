import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

subjects = ["Mathematics", "English", "Biology", "Chemistry", "Physics", "History", "Geography"]
terms = ["Term 1", "Term 2", "Term 3", "Term 4"]

data = np.array([
    [72, 68, 74, 81],
    [85, 79, 83, 87],
    [63, 71, 67, 75],
    [58, 64, 69, 73],
    [61, 59, 65, 70],
    [88, 84, 91, 86],
    [76, 80, 78, 83],
])

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor("#FFFFFF")

im = ax.imshow(data, cmap="RdYlGn", aspect="auto", vmin=50, vmax=95)

ax.set_xticks(np.arange(len(terms)))
ax.set_yticks(np.arange(len(subjects)))
ax.set_xticklabels(terms, fontsize=11)
ax.set_yticklabels(subjects, fontsize=11)

ax.set_xticks(np.arange(len(terms) + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(len(subjects) + 1) - 0.5, minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="minor", bottom=False, left=False)

for i in range(len(subjects)):
    for j in range(len(terms)):
        val = data[i, j]
        text_color = "black" if 65 <= val <= 80 else "white"
        ax.text(j, i, str(val), ha="center", va="center",
                fontsize=12, fontweight="bold", color=text_color)

cbar = fig.colorbar(im, ax=ax, pad=0.02)
cbar.set_label("Average Score (%)", fontsize=10)
cbar.ax.tick_params(labelsize=9)

ax.set_title("Student Average Scores by Subject and Term (2023)", fontsize=13, fontweight="bold", pad=14)
ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")

plt.tight_layout()
plt.savefig("chart06_heatmap.png", dpi=150, bbox_inches="tight")
print("Saved.")
