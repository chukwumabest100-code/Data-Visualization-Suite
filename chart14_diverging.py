import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

countries = ["Australia", "Canada", "Germany", "UAE", "UK", "France", "Japan", "USA"]

age_groups = ["18-29", "30-44", "45-59", "60+"]

data = {
    "18-29": [42, 38, 29, 67, -18, -23, -31, 54],
    "30-44": [61, 72, 44, 83, -12, -8,  -19, 89],
    "45-59": [-14, 23, -9, 31, -27, -31, -42, 37],
    "60+":   [-38, -11, -22, -6, -41, -53, -61, 12],
}

colors = {
    "18-29": "#0099CC",
    "30-44": "#00CC88",
    "45-59": "#FF8800",
    "60+":   "#CC3355",
}

y = np.arange(len(countries))
height = 0.18

fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor("#F5F0FF")
ax.set_facecolor("#EEE8FF")

for i, age in enumerate(age_groups):
    vals = data[age]
    y_pos = y + (i - 1.5) * height
    bars = ax.barh(y_pos, vals, height,
                   color=colors[age], label=age,
                   zorder=3, edgecolor="white", linewidth=0.6)
    for bar, val in zip(bars, vals):
        x_pos = val + (1.5 if val >= 0 else -1.5)
        ha = "left" if val >= 0 else "right"
        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                f"{val:+d}", va="center", ha=ha,
                fontsize=8, fontweight="bold", color=colors[age])

ax.axvline(0, color="#888888", linewidth=1.2, zorder=5)
ax.set_yticks(y)
ax.set_yticklabels(countries, fontsize=11)
ax.set_xlabel("Net Migration (thousands)", fontsize=11, labelpad=8)
ax.set_title("Net Migration by Country and Age Group (2023)",
             fontsize=13, fontweight="bold", pad=14)
ax.set_xlim(-80, 110)
ax.set_xticks(np.arange(-80, 111, 20))
ax.grid(axis="x", linestyle="--", linewidth=0.5, color="#CCBBEE", alpha=0.8)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAACC")
ax.spines["bottom"].set_color("#AAAACC")

ax.text(-75, 8.1, "← Emigration", fontsize=9, color="#CC3355", fontstyle="italic")
ax.text(5,   8.1, "Immigration →", fontsize=9, color="#00CC88", fontstyle="italic")

ax.legend(title="Age Group", fontsize=10, title_fontsize=10,
          loc="lower right", framealpha=0.9, edgecolor="#AAAACC")

plt.tight_layout()
plt.savefig("chart14_diverging.png", dpi=150, bbox_inches="tight")
print("Saved.")
