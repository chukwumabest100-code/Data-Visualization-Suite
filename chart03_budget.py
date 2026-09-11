import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

categories = ["Q1", "Q2", "Q3", "Q4"]
departments = ["Engineering", "Marketing", "Sales", "Operations"]

data = {
    "Engineering": [142, 156, 138, 171],
    "Marketing":   [89,  103, 97,  112],
    "Sales":       [201, 187, 223, 198],
    "Operations":  [74,  68,  81,  79],
}

colors = ["#185FA5", "#E85D24", "#1D9E75", "#BA7517"]

x = np.arange(len(categories))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

for i, (dept, vals) in enumerate(data.items()):
    bars = ax.bar(x + i * width, vals, width, label=dept,
                  color=colors[i], zorder=3, edgecolor="white", linewidth=0.5)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,
                str(val), ha="center", va="bottom", fontsize=8.5,
                fontweight="bold", color=colors[i])

ax.set_xlabel("Quarter", fontsize=11, labelpad=8)
ax.set_ylabel("Budget Spent ($000s)", fontsize=11, labelpad=8)
ax.set_title("Departmental Budget Expenditure by Quarter (2023)", fontsize=13, fontweight="bold", pad=14)
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 260)
ax.set_yticks(np.arange(0, 261, 40))
ax.grid(axis="y", linestyle="--", linewidth=0.6, color="#CCCCCC", alpha=0.8)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")
ax.legend(title="Department", fontsize=10, title_fontsize=10,
          loc="upper right", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart03_budget.png", dpi=150, bbox_inches="tight")
print("Saved.")
