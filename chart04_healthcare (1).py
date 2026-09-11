import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

regions = ["North", "South", "East", "West", "Central"]

data = {
    "Preventive":     [34, 41, 28, 37, 31],
    "Emergency":      [52, 48, 61, 44, 57],
    "Surgical":       [29, 35, 22, 41, 33],
    "Rehabilitation": [18, 24, 15, 27, 21],
}

colors = ["#1D9E75", "#E85D24", "#185FA5", "#BA7517"]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

x = np.arange(len(regions))
bottoms = np.zeros(len(regions))

for i, (cat, vals) in enumerate(data.items()):
    vals_arr = np.array(vals)
    bars = ax.bar(x, vals_arr, bottom=bottoms, label=cat,
                  color=colors[i], zorder=3, edgecolor="white", linewidth=0.8)
    for j, (bar, val) in enumerate(zip(bars, vals)):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bottoms[j] + val / 2,
                str(val), ha="center", va="center",
                fontsize=9, fontweight="bold", color="white")
    bottoms += vals_arr

ax.set_xlabel("Region", fontsize=11, labelpad=8)
ax.set_ylabel("Number of Cases (thousands)", fontsize=11, labelpad=8)
ax.set_title("Healthcare Cases by Type and Region (2023)", fontsize=13, fontweight="bold", pad=14)
ax.set_xticks(x)
ax.set_xticklabels(regions, fontsize=11)
ax.set_ylim(0, 160)
ax.set_yticks(np.arange(0, 161, 20))
ax.grid(axis="y", linestyle="--", linewidth=0.6, color="#CCCCCC", alpha=0.8)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")
ax.legend(title="Case Type", fontsize=10, title_fontsize=10,
          loc="upper right", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart04_healthcare.png", dpi=150, bbox_inches="tight")
print("Saved.")
