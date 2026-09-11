import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rainfall = [12, 18, 34, 67, 112, 143, 138, 121, 89, 54, 27, 14]

crop_yields = {
    "Maize":  [1.2, 1.4, 2.1, 3.4, 4.8, 5.6, 5.9, 5.4, 4.1, 2.8, 1.7, 1.3],
    "Wheat":  [2.8, 3.1, 3.7, 4.2, 4.6, 3.9, 3.1, 2.7, 3.3, 4.1, 3.6, 2.9],
    "Cassava":[3.4, 3.2, 3.8, 4.4, 5.1, 5.7, 6.2, 6.4, 5.8, 4.9, 4.1, 3.6],
}

line_colors = {
    "Maize":   "#E8A838",
    "Wheat":   "#7B3F00",
    "Cassava": "#2D6A4F",
}

x = np.arange(len(months))

fig, ax1 = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor("#F0FFF4")
ax1.set_facecolor("#E8F8EE")

bars = ax1.bar(x, rainfall, color="#A8D5E2", alpha=0.65,
               zorder=2, edgecolor="#7BBDD0", linewidth=0.6, label="Rainfall")
for bar, val in zip(bars, rainfall):
    ax1.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 2, str(val),
             ha="center", va="bottom", fontsize=7.8,
             fontweight="bold", color="#4A90A4")

ax1.set_xlabel("Month", fontsize=11, labelpad=8)
ax1.set_ylabel("Monthly Rainfall (mm)", fontsize=11, labelpad=8, color="#4A90A4")
ax1.tick_params(axis="y", labelcolor="#4A90A4")
ax1.set_ylim(0, 180)
ax1.set_yticks(np.arange(0, 181, 20))
ax1.set_xticks(x)
ax1.set_xticklabels(months, fontsize=10)

ax2 = ax1.twinx()
ax2.set_facecolor("none")

for crop, vals in crop_yields.items():
    ax2.plot(x, vals, color=line_colors[crop], linewidth=2.4,
             marker="o", markersize=6, label=crop, zorder=4,
             markeredgecolor="white", markeredgewidth=1)
    for xi, yi in zip(x, vals):
        ax2.annotate(f"{yi}", (xi, yi),
                     textcoords="offset points",
                     xytext=(0, 8), ha="center",
                     fontsize=7.5, fontweight="bold",
                     color=line_colors[crop])

ax2.set_ylabel("Crop Yield (tonnes/hectare)", fontsize=11,
               labelpad=8, color="#2D6A4F")
ax2.tick_params(axis="y", labelcolor="#2D6A4F")
ax2.set_ylim(0, 9)
ax2.set_yticks(np.arange(0, 9.1, 1))

ax1.set_title("Monthly Rainfall and Crop Yield (2023)",
              fontsize=13, fontweight="bold", pad=14)

ax1.grid(axis="y", linestyle="--", linewidth=0.5,
         color="#AADDC0", alpha=0.7, zorder=1)
for spine in ["top"]:
    ax1.spines[spine].set_visible(False)
ax1.spines["left"].set_color("#AADDC0")
ax1.spines["bottom"].set_color("#AADDC0")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           fontsize=10, title="Series", title_fontsize=10,
           loc="upper left", framealpha=0.9, edgecolor="#AADDC0")

plt.tight_layout()
plt.savefig("chart15_dualaxis.png", dpi=150, bbox_inches="tight")
print("Saved.")
