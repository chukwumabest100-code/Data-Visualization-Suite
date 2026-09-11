import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

countries = ["Brazil", "Germany", "India", "Japan", "Nigeria", "Canada", "Australia"]
sources = ["Coal", "Natural Gas", "Nuclear", "Renewables"]

data = {
    "Coal":        [12, 41, 68, 29, 8,  14, 37],
    "Natural Gas": [18, 27, 24, 38, 21, 43, 29],
    "Nuclear":     [4,  19, 7,  26, 0,  16, 3],
    "Renewables":  [51, 22, 18, 14, 31, 38, 24],
}

colors = ["#444444", "#E85D24", "#185FA5", "#1D9E75"]

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

y = np.arange(len(countries))
height = 0.18

for i, (source, vals) in enumerate(data.items()):
    bars = ax.barh(y + i * height, vals, height, label=source,
                   color=colors[i], zorder=3, edgecolor="white", linewidth=0.5)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=8.5,
                fontweight="bold", color=colors[i])

ax.set_xlabel("Energy Consumption (EJ)", fontsize=11, labelpad=8)
ax.set_title("Energy Consumption by Source and Country (2023)", fontsize=13, fontweight="bold", pad=14)
ax.set_yticks(y + height * 1.5)
ax.set_yticklabels(countries, fontsize=11)
ax.set_xlim(0, 80)
ax.set_xticks(np.arange(0, 81, 10))
ax.grid(axis="x", linestyle="--", linewidth=0.6, color="#CCCCCC", alpha=0.8)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")
ax.legend(title="Energy Source", fontsize=10, title_fontsize=10,
          loc="lower right", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart07_energy.png", dpi=150, bbox_inches="tight")
print("Saved.")
