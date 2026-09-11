import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

data = {
    "Lagos":   [0.4, 0.9, 0.6, 1.1, 0.8, 1.4, 1.1, 1.6, 1.3],
    "London":  [0.3, 1.2, 0.5, 0.7, 1.0, 1.3, 0.9, 1.5, 1.8],
    "Mumbai":  [0.6, 0.8, 1.0, 1.3, 1.1, 1.7, 1.4, 1.9, 2.1],
    "Toronto": [0.2, 0.7, 0.4, 0.9, 1.2, 1.0, 1.3, 1.7, 2.0],
}

colors = {
    "Lagos":   "#E85D24",
    "London":  "#185FA5",
    "Mumbai":  "#1D9E75",
    "Toronto": "#BA7517",
}

markers = {
    "Lagos":   "o",
    "London":  "s",
    "Mumbai":  "^",
    "Toronto": "D",
}

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

for city, vals in data.items():
    line, = ax.plot(years, vals, color=colors[city], marker=markers[city],
                    linewidth=2.2, markersize=7, label=city, zorder=3)
    for x, y in zip(years, vals):
        offset_y = 0.06
        if city == "London" and x == 2016:
            offset_y = 0.10
        if city == "Lagos" and x == 2016:
            offset_y = -0.12
        ax.annotate(f"{y}", (x, y), textcoords="offset points",
                    xytext=(0, 10 if offset_y > 0 else -16),
                    ha="center", fontsize=8.5, color=colors[city], fontweight="bold")

ax.set_xlabel("Year", fontsize=11, labelpad=8)
ax.set_ylabel("Temperature Anomaly (°C above 1990 baseline)", fontsize=10.5, labelpad=8)
ax.set_title("Annual Mean Temperature Anomaly by City (2015–2023)", fontsize=13, fontweight="bold", pad=14)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 2.5, 0.2))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
ax.set_ylim(0, 2.5)
ax.grid(axis="y", linestyle="--", linewidth=0.6, color="#CCCCCC", alpha=0.8)
ax.grid(axis="x", linestyle=":", linewidth=0.4, color="#DDDDDD", alpha=0.6)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")

legend = ax.legend(title="City", fontsize=10, title_fontsize=10,
                   loc="upper left", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/chart02_climate.png", dpi=150, bbox_inches="tight")
print("Saved.")
