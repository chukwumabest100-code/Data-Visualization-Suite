import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

countries = ["USA", "China", "Brazil", "Germany", "India",
             "Nigeria", "Japan", "Mexico", "France", "Ethiopia"]

gdp_per_capita = [63, 12, 15, 51, 7, 5, 42, 10, 44, 3]
life_expectancy = [79, 77, 75, 81, 70, 55, 84, 73, 83, 66]
population = [331, 1411, 214, 83, 1380, 211, 126, 130, 68, 117]
continent = ["Americas", "Asia", "Americas", "Europe", "Asia",
             "Africa", "Asia", "Americas", "Europe", "Africa"]

continent_colors = {
    "Americas": "#C0392B",
    "Asia":     "#8E44AD",
    "Europe":   "#16A085",
    "Africa":   "#D4AC0D",
}

colors = [continent_colors[c] for c in continent]
sizes = [p * 0.6 for p in population]

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#FFFDF5")
ax.set_facecolor("#FFFBEE")

scatter = ax.scatter(gdp_per_capita, life_expectancy,
                     s=sizes, c=colors, alpha=0.7,
                     edgecolors="white", linewidth=1.5, zorder=3)

for i, country in enumerate(countries):
    ax.annotate(country,
                (gdp_per_capita[i], life_expectancy[i]),
                textcoords="offset points", xytext=(8, 5),
                fontsize=9, fontweight="bold", color=colors[i])
    ax.annotate(f"${gdp_per_capita[i]}k",
                (gdp_per_capita[i], life_expectancy[i]),
                textcoords="offset points", xytext=(8, -7),
                fontsize=8, color="#666666")

for continent, color in continent_colors.items():
    ax.scatter([], [], c=color, s=80, label=continent,
               edgecolors="white", linewidth=1)

for pop, label in [(83, "83M"), (330, "330M"), (1400, "1.4B")]:
    ax.scatter([], [], c="#AAAAAA", s=pop * 0.6, alpha=0.6,
               edgecolors="white", linewidth=1, label=label)

ax.set_xlabel("GDP per Capita ($000s)", fontsize=11, labelpad=8)
ax.set_ylabel("Life Expectancy (years)", fontsize=11, labelpad=8)
ax.set_title("GDP per Capita vs Life Expectancy\n(bubble size = population, 2023)",
             fontsize=13, fontweight="bold", pad=14)

ax.set_xlim(0, 72)
ax.set_ylim(50, 90)
ax.set_xticks(np.arange(0, 73, 10))
ax.set_yticks(np.arange(50, 91, 5))
ax.grid(linestyle="--", linewidth=0.5, color="#DDCCAA", alpha=0.8)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#BBAA88")
ax.spines["bottom"].set_color("#BBAA88")

ax.legend(fontsize=9, title="Continent / Population",
          title_fontsize=9, loc="lower right",
          framealpha=0.9, edgecolor="#CCBBAA")

plt.tight_layout()
plt.savefig("chart10_bubble.png", dpi=150, bbox_inches="tight")
print("Saved.")
