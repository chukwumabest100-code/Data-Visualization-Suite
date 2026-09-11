import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#F8F9FA")
ax.set_facecolor("#F8F9FA")

# Manual treemap layout: (x, y, width, height, label, value, color)
tiles = [
    (0.00, 0.35, 0.28, 0.65, "Samsung\nAsia\n18.3%",    18.3, "#1A5276"),
    (0.00, 0.00, 0.28, 0.35, "Apple\nAsia\n14.1%",      14.1, "#922B21"),
    (0.28, 0.42, 0.22, 0.58, "Xiaomi\nAsia\n12.7%",     12.7, "#1D8348"),
    (0.28, 0.00, 0.22, 0.42, "Samsung\nEurope\n11.4%",  11.4, "#2471A3"),
    (0.50, 0.48, 0.18, 0.52, "Apple\nEurope\n9.8%",      9.8, "#C0392B"),
    (0.50, 0.00, 0.18, 0.48, "Apple\nAmericas\n8.6%",    8.6, "#E74C3C"),
    (0.68, 0.42, 0.16, 0.58, "Samsung\nAmericas\n7.2%",  7.2, "#2980B9"),
    (0.68, 0.00, 0.16, 0.42, "Oppo\nAsia\n6.9%",         6.9, "#27AE60"),
    (0.84, 0.52, 0.16, 0.48, "Xiaomi\nEurope\n4.3%",     4.3, "#48C9B0"),
    (0.84, 0.26, 0.16, 0.26, "Others\nAfrica\n3.8%",     3.8, "#F39C12"),
    (0.84, 0.00, 0.16, 0.26, "Tecno\nAfrica\n2.9%",      2.9, "#E67E22"),
]

for (x, y, w, h, label, val, color) in tiles:
    rect = patches.FancyBboxPatch((x + 0.002, y + 0.002),
                                   w - 0.004, h - 0.004,
                                   boxstyle="round,pad=0.005",
                                   linewidth=2, edgecolor="white",
                                   facecolor=color, alpha=0.88)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, label,
            ha="center", va="center",
            fontsize=9, fontweight="bold", color="white",
            multialignment="center",
            transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title("Global Smartphone Market Share by Brand and Region (2023)",
             fontsize=13, fontweight="bold", pad=14)

plt.tight_layout()
plt.savefig("chart11_treemap.png", dpi=150, bbox_inches="tight")
print("Saved.")
