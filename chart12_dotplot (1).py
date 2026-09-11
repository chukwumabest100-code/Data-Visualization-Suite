import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Oncology", "Emergency"]
shifts = ["Morning", "Afternoon", "Night"]

data = {
    "Morning":   [24, 31, 18, 22, 41, 67],
    "Afternoon": [38, 27, 29, 19, 35, 83],
    "Night":     [51, 44, 36, 28, 47, 112],
}

colors = {"Morning": "#2ECC71", "Afternoon": "#E67E22", "Night": "#8E44AD"}
markers = {"Morning": "o", "Afternoon": "s", "Night": "^"}
offsets = {"Morning": -0.22, "Afternoon": 0, "Night": 0.22}

y = np.arange(len(departments))

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#F0F4F8")
ax.set_facecolor("#E8EEF4")

for dept_idx in range(len(departments)):
    ax.hlines(dept_idx, 0, 120, color="#FFFFFF", linewidth=1.5, zorder=1)

for shift in shifts:
    vals = data[shift]
    y_pos = y + offsets[shift]
    ax.scatter(vals, y_pos,
               color=colors[shift], marker=markers[shift],
               s=120, zorder=4, label=shift,
               edgecolors="white", linewidth=1.2)
    for i, val in enumerate(vals):
        ax.annotate(str(val), (val, y_pos[i]),
                    textcoords="offset points",
                    xytext=(7, 0), va="center",
                    fontsize=8.5, fontweight="bold",
                    color=colors[shift])

ax.set_yticks(y)
ax.set_yticklabels(departments, fontsize=11)
ax.set_xlabel("Average Patient Wait Time (minutes)", fontsize=11, labelpad=8)
ax.set_title("Hospital Patient Wait Times by Department and Shift (2023)",
             fontsize=13, fontweight="bold", pad=14)
ax.set_xlim(0, 135)
ax.set_xticks(np.arange(0, 131, 10))
ax.grid(axis="x", linestyle="--", linewidth=0.5, color="#BBCCD8", alpha=0.8)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#AABBCC")
ax.tick_params(left=False)

ax.legend(title="Shift", fontsize=10, title_fontsize=10,
          loc="lower right", framealpha=0.9, edgecolor="#AABBCC")

plt.tight_layout()
plt.savefig("chart12_dotplot.png", dpi=150, bbox_inches="tight")
print("Saved.")
