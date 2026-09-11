import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
         12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

rates = {
    "Summer": [
        8.2, 8.2, 8.2, 8.2, 8.2, 8.2,
        11.4, 11.4, 15.7, 15.7, 15.7, 15.7,
        18.3, 18.3, 18.3, 18.3, 21.6, 21.6,
        24.9, 24.9, 21.6, 18.3, 11.4, 8.2, 8.2
    ],
    "Winter": [
        7.1, 7.1, 7.1, 7.1, 7.1, 7.1,
        13.8, 13.8, 19.4, 19.4, 19.4, 19.4,
        16.2, 16.2, 16.2, 16.2, 22.7, 22.7,
        27.3, 27.3, 22.7, 16.2, 13.8, 7.1, 7.1
    ],
    "Spring/Autumn": [
        6.4, 6.4, 6.4, 6.4, 6.4, 6.4,
        9.8, 9.8, 13.1, 13.1, 13.1, 13.1,
        14.7, 14.7, 14.7, 14.7, 17.5, 17.5,
        19.8, 19.8, 17.5, 14.7, 9.8, 6.4, 6.4
    ],
}

colors = {
    "Summer":       "#D4380D",
    "Winter":       "#0958D9",
    "Spring/Autumn":"#389E0D",
}

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor("#FFFAE6")
ax.set_facecolor("#FFF8DC")

for season, vals in rates.items():
    ax.step(hours, vals, where="post", color=colors[season],
            linewidth=2.5, label=season, zorder=3)
    unique_points = []
    seen = set()
    for h, v in zip(hours[:-1], vals[:-1]):
        if v not in seen:
            unique_points.append((h, v))
            seen.add(v)
    for h, v in unique_points:
        ax.annotate(f"{v}p", (h, v),
                    textcoords="offset points",
                    xytext=(4, 6), fontsize=7.8,
                    fontweight="bold", color=colors[season])

time_labels = [f"{h:02d}:00" for h in range(0, 25, 2)]
ax.set_xticks(range(0, 25, 2))
ax.set_xticklabels(time_labels, fontsize=8.5, rotation=35, ha="right")
ax.set_yticks(np.arange(0, 31, 2))
ax.set_ylim(0, 32)
ax.set_xlim(0, 24)

ax.set_xlabel("Hour of Day", fontsize=11, labelpad=8)
ax.set_ylabel("Electricity Tariff Rate (pence/kWh)", fontsize=11, labelpad=8)
ax.set_title("Electricity Tariff Rates by Time of Day and Season",
             fontsize=13, fontweight="bold", pad=14)

ax.axvspan(0, 6, alpha=0.06, color="#555555", label="Off-peak zone")
ax.axvspan(18, 21, alpha=0.08, color="#FF4444", label="Peak zone")

ax.grid(axis="y", linestyle="--", linewidth=0.5, color="#DDCC88", alpha=0.8)
ax.grid(axis="x", linestyle=":", linewidth=0.4, color="#DDCC88", alpha=0.5)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#BBAA66")
ax.spines["bottom"].set_color("#BBAA66")

ax.legend(fontsize=10, title="Season", title_fontsize=10,
          loc="upper left", framealpha=0.9, edgecolor="#CCBB77")

plt.tight_layout()
plt.savefig("chart13_step.png", dpi=150, bbox_inches="tight")
print("Saved.")
