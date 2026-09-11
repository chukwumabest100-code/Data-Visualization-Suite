import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

schools = [
    "Greenfield", "Lakeside", "Pinecrest", "Harborview", "Westmoor",
    "Elmwood", "Ridgeway", "Stonegate", "Fairbrook", "Cresthill",
    "Mapleton", "Silverdale", "Ironwood", "Clearwater", "Sunridge"
]

funding = [42, 67, 55, 83, 38, 71, 49, 91, 63, 78, 34, 88, 57, 44, 76]
pass_rate = [61, 74, 68, 85, 57, 79, 64, 91, 72, 83, 53, 89, 69, 62, 81]
student_count = [320, 510, 430, 680, 290, 540, 370, 720, 490, 610, 260, 700, 420, 310, 580]

regions = ["Urban", "Suburban", "Rural", "Urban", "Rural",
           "Suburban", "Rural", "Urban", "Suburban", "Urban",
           "Rural", "Suburban", "Urban", "Rural", "Suburban"]

region_colors = {"Urban": "#185FA5", "Suburban": "#1D9E75", "Rural": "#E85D24"}
colors = [region_colors[r] for r in regions]
sizes = [s / 4 for s in student_count]

fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FAFAFA")

for region, color in region_colors.items():
    idx = [i for i, r in enumerate(regions) if r == region]
    ax.scatter(
        [funding[i] for i in idx],
        [pass_rate[i] for i in idx],
        s=[sizes[i] for i in idx],
        color=color, alpha=0.85, edgecolors="white",
        linewidth=1.2, label=region, zorder=3
    )

for i, school in enumerate(schools):
    ax.annotate(school, (funding[i], pass_rate[i]),
                textcoords="offset points", xytext=(6, 4),
                fontsize=7.5, color="#444444")
    ax.annotate(f"({pass_rate[i]}%)", (funding[i], pass_rate[i]),
                textcoords="offset points", xytext=(6, -8),
                fontsize=7, color="#777777")

ax.set_xlabel("Annual Funding per Student ($000s)", fontsize=11, labelpad=8)
ax.set_ylabel("Student Pass Rate (%)", fontsize=11, labelpad=8)
ax.set_title("School Funding vs Student Pass Rate by Region (2023)", fontsize=13, fontweight="bold", pad=14)

ax.set_xlim(25, 100)
ax.set_ylim(45, 100)
ax.set_xticks(np.arange(30, 101, 10))
ax.set_yticks(np.arange(50, 101, 5))

ax.grid(linestyle="--", linewidth=0.5, color="#CCCCCC", alpha=0.7)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#AAAAAA")
ax.spines["bottom"].set_color("#AAAAAA")

legend_region = ax.legend(title="Region", fontsize=10, title_fontsize=10,
                          loc="lower right", framealpha=0.9, edgecolor="#CCCCCC")
ax.add_artist(legend_region)

for size, label in [(260/4, "260"), (490/4, "490"), (720/4, "720")]:
    ax.scatter([], [], s=size, color="#AAAAAA", alpha=0.7,
               edgecolors="white", label=f"{label} students")
ax.legend(title="Enrollment", fontsize=9, title_fontsize=9,
          loc="upper left", framealpha=0.9, edgecolor="#CCCCCC")

plt.tight_layout()
plt.savefig("chart05_education.png", dpi=150, bbox_inches="tight")
print("Saved.")
