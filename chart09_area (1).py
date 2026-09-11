import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = {
    "Subscriptions": [124, 131, 138, 142, 149, 156, 161, 158, 163, 171, 178, 185],
    "Advertising":   [43,  38,  51,  56,  62,  71,  68,  74,  69,  78,  83,  91],
    "Licensing":     [29,  29,  34,  31,  37,  33,  39,  41,  38,  44,  47,  43],
    "Consulting":    [18,  22,  19,  24,  21,  28,  26,  31,  33,  29,  36,  38],
}

colors = ["#185FA5", "#E85D24", "#1D9E75", "#BA7517"]

x = np.arange(len(months))

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

bottom = np.zeros(len(months))
for i, (stream, vals) in enumerate(data.items()):
    vals_arr = np.array(vals)
    ax.fill_between(x, bottom, bottom + vals_arr,
                    color=colors[i], alpha=0.75, label=stream, zorder=3)
    ax.plot(x, bottom + vals_arr, color=colors[i], linewidth=1.2, zorder=4)
    for j, (xv, yv) in enumerate(zip(x, vals_arr)):
        if j % 3 == 0:
            ax.annotate(str(yv), (xv, bottom[j] + yv / 2),
                        ha="center", va="center", fontsize=7.5,
                        fontweight="bold", color="white")
    bottom += vals_arr

for j, xv in enumerate(x):
    total = sum(data[s][j] for s in data)
    ax.annotate(str(total), (xv, bottom[j] + 5),
                ha="center", va="bottom", fontsize=8,
                color="#333333", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=10)
ax.set_ylabel("Revenue ($000s)", fontsize=11, labelpad=8)
ax.set_title("Monthly Revenue by Stream (2023)", fontsize=13, fontweight="bold", pad=14)
ax.set_ylim(0, 420)
ax.set_yticks(np.arange(0, 421, 50))
ax.grid(axis="y", linestyle="--", linewidth=0.6, color="#CCCCCC", alpha=0.7)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")
ax.legend(title="Revenue Stream", fontsize=10, title_fontsize=10,
          loc="upper left", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart09_area.png", dpi=150, bbox_inches="tight")
print("Saved.")
