import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

categories = ["Infrastructure", "Education", "Healthcare", "Innovation", "Trade", "Governance"]
N = len(categories)

countries = {
    "Germany":   [82, 88, 85, 79, 76, 83],
    "Brazil":    [54, 63, 61, 48, 57, 52],
    "Japan":     [91, 86, 89, 93, 81, 78],
    "Nigeria":   [38, 47, 43, 31, 52, 36],
    "Canada":    [78, 84, 82, 74, 79, 88],
}

colors = ["#185FA5", "#E85D24", "#1D9E75", "#BA7517", "#9B59B6"]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

for idx, (country, values) in enumerate(countries.items()):
    vals = values + values[:1]
    ax.plot(angles, vals, color=colors[idx], linewidth=2.2, label=country, zorder=3)
    ax.fill(angles, vals, color=colors[idx], alpha=0.08)
    for angle, val in zip(angles[:-1], values):
        ax.annotate(str(val),
                    xy=(angle, val),
                    xytext=(angle, val + 3.5),
                    fontsize=7.5,
                    color=colors[idx],
                    fontweight="bold",
                    ha="center", va="center")

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, fontweight="500")
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=8, color="#888888")
ax.set_ylim(0, 105)
ax.grid(color="#CCCCCC", linestyle="--", linewidth=0.6, alpha=0.8)
ax.spines["polar"].set_color("#CCCCCC")

ax.set_title("Country Competitiveness Index by Dimension (2023)",
             fontsize=13, fontweight="bold", pad=28)

ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15),
          fontsize=10, title="Country", title_fontsize=10,
          framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart08_radar.png", dpi=150, bbox_inches="tight")
print("Saved.")
