import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

GREEN = '#1b3a2d'
ACCENT = '#3a7d5c'
LIGHT = '#87b9a0'
RED = '#c0392b'
ORANGE = '#e67e22'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'Times New Roman'],
    'font.size': 11,
    'axes.facecolor': '#fafaf8',
    'figure.facecolor': '#fafaf8',
    'axes.edgecolor': '#999',
    'axes.labelcolor': '#1a1a1a',
    'text.color': '#1a1a1a',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT = 'C:/Users/Rober/Documents/Programming/Ideas/rainwater-power'

df = pd.read_excel('C:/Users/Rober/Downloads/water energy.ods', sheet_name='lugares', engine='odf', header=1)
df.columns = ['country', 'rainfall_mm', 'potential_litres', 'electricity_used', 'pct_from_rain', 'land_area_km2', 'energy_total_land', 'pct_total_land', 'pct_land_10pct', 'years_rain_1yr']
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Actual per-house kWh (10m height, 269m2 roof, no turbine losses)
df['house_kwh'] = df['potential_litres'] * 9.81 * 10 / 3_600_000

# =========================================================
# 1. Per-house kWh across countries (XKCD style)
# =========================================================
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(8, 5))

    showcase = ['Solomon Islands', 'Colombia', 'Papua New Guinea', 'Madagascar',
                'Ireland', 'United Kingdom', 'United States', 'Germany']

    data = []
    for c in showcase:
        row = df[df['country'].str.contains(c, case=False, na=False)]
        if len(row) > 0:
            data.append((c, row.iloc[0]['house_kwh'], row.iloc[0]['rainfall_mm']))

    data.sort(key=lambda x: x[1])
    names = [d[0] for d in data]
    kwh = [d[1] for d in data]

    colors = [ACCENT if k > 15 else LIGHT for k in kwh]
    ax.barh(range(len(names)), kwh, color=colors, edgecolor=GREEN, linewidth=1)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlabel('kWh per year (269m² roof, 10m drop)')
    ax.set_title('Electricity from one rooftop, per year', fontsize=13)

    ax.annotate('Still only enough to\\nrun a few LED bulbs',
                xy=(kwh[-1], len(kwh)-1), xytext=(kwh[-1]+3, len(kwh)-3),
                fontsize=9, arrowprops=dict(arrowstyle='->', color=GREEN),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#fafaf8', edgecolor=GREEN))

    plt.tight_layout()
    fig.savefig(f'{OUT}/per-house-kwh.png', dpi=150)
    plt.close()
    print('1/5 per-house-kwh.png')

# =========================================================
# 2. The twist: country-level land % for 10% of energy
# =========================================================
fig, ax = plt.subplots(figsize=(8, 6))

feasible = df[df['pct_land_10pct'] < 25].sort_values('pct_land_10pct').head(12)
feasible = feasible.iloc[::-1]

names = [c.replace('Congo, Democratic Republic of the', 'DR Congo')
         .replace('Central African Republic', 'C. African Rep.')
         .replace('Congo, Republic of the', 'Rep. Congo')
         for c in feasible['country']]
pcts = feasible['pct_land_10pct'].values

colors = [GREEN if p < 5 else ACCENT if p < 10 else LIGHT for p in pcts]

ax.barh(range(len(names)), pcts, color=colors, edgecolor=GREEN, linewidth=0.5)
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=10)
ax.set_xlabel('% of country land area needed')
ax.set_title('Land needed to produce 10% of national electricity\nfrom rainwater alone', fontsize=12, color=GREEN, fontweight='bold')

for i, (p, n) in enumerate(zip(pcts, names)):
    ax.text(p + 0.3, i, f'{p:.1f}%', va='center', fontsize=9, fontweight='bold', color=GREEN)

legend_elements = [plt.Rectangle((0,0),1,1, facecolor=GREEN, label='< 5% of land'),
                   plt.Rectangle((0,0),1,1, facecolor=ACCENT, label='5-10%'),
                   plt.Rectangle((0,0),1,1, facecolor=LIGHT, label='10-25%')]
ax.legend(handles=legend_elements, loc='lower right', frameon=False, fontsize=9)

plt.tight_layout()
fig.savefig(f'{OUT}/land-needed.png', dpi=150)
plt.close()
print('2/5 land-needed.png')

# =========================================================
# 3. Scatter: rainfall vs electricity consumption
# =========================================================
fig, ax = plt.subplots(figsize=(8, 6))

# Color by feasibility
for _, row in df.iterrows():
    if pd.isna(row['pct_land_10pct']) or pd.isna(row['rainfall_mm']):
        continue
    color = GREEN if row['pct_land_10pct'] < 10 else LIGHT if row['pct_land_10pct'] < 50 else '#ddd'
    alpha = 0.8 if row['pct_land_10pct'] < 10 else 0.4
    ax.scatter(row['rainfall_mm'], row['electricity_used'], s=40, color=color, alpha=alpha, edgecolors=GREEN, linewidth=0.3)

# Label the interesting ones
highlights = ['Guinea-Bissau', 'Solomon Islands', 'Central African Republic', 'Madagascar',
              'Sierra Leone', 'Liberia', 'Colombia', 'United States', 'United Kingdom', 'Ireland']
for h in highlights:
    row = df[df['country'].str.contains(h, case=False, na=False)]
    if len(row) > 0:
        r = row.iloc[0]
        offset = (8, 5) if r['electricity_used'] > 1e9 else (8, -10)
        ax.annotate(h.replace('Central African Republic', 'C.A.R.'),
                   (r['rainfall_mm'], r['electricity_used']),
                   fontsize=7, xytext=offset, textcoords='offset points', color=GREEN)

ax.set_xlabel('Average annual rainfall (mm)')
ax.set_ylabel('National electricity consumption (kWh/year)')
ax.set_yscale('log')
ax.set_title('The sweet spot: high rainfall + low consumption', fontsize=12, color=GREEN, fontweight='bold')

# Draw the sweet spot zone
from matplotlib.patches import FancyBboxPatch
rect = FancyBboxPatch((1200, 2e7), 2000, 3e8, boxstyle="round,pad=0.1",
                       facecolor=ACCENT, alpha=0.1, edgecolor=ACCENT, linewidth=1.5, linestyle='--')
ax.add_patch(rect)
ax.text(2200, 1.5e7, 'Sweet spot', fontsize=10, color=ACCENT, fontstyle='italic')

plt.tight_layout()
fig.savefig(f'{OUT}/scatter-sweet-spot.png', dpi=150)
plt.close()
print('3/5 scatter-sweet-spot.png')

# =========================================================
# 4. XKCD: years of rain to power one year (the fun ones)
# =========================================================
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(8, 5))

    fun = [
        ('C. African Rep.', 0.24),
        ('Chad', 0.49),
        ('Guinea-Bissau', 0.71),
        ('Solomon Islands', 0.93),
        ('Sierra Leone', 1.11),
        ('Liberia', 1.30),
        ('Madagascar', 1.48),
        ('Ireland', 324.6),
        ('United Kingdom', 1046.9),
        ('United States', 598.0),
    ]

    names = [f[0] for f in fun][::-1]
    years = [f[1] for f in fun][::-1]

    colors = [RED if y > 100 else LIGHT if y > 1 else GREEN for y in years]

    ax.barh(range(len(names)), years, color=colors, edgecolor=GREEN, linewidth=1)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlabel('Years of rain needed to power the country for one year')
    ax.set_xscale('log')
    ax.set_title("If ALL rain hitting the country\\nwent through turbines...", fontsize=13)

    ax.axvline(x=1, color=GREEN, linestyle='--', linewidth=2, alpha=0.5)
    ax.text(1.2, 9, 'Rain alone\\ncould do it', fontsize=9, color=GREEN, fontstyle='italic')

    plt.tight_layout()
    fig.savefig(f'{OUT}/years-of-rain.png', dpi=150)
    plt.close()
    print('4/5 years-of-rain.png')

# =========================================================
# 5. The comparison: what 2.4% of CAR land looks like
# =========================================================
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(7, 5))

    comparisons = [
        ('C.A.R. rain collectors\nneeded (2.4%)', 14929),
        ('C.A.R. farmland\n(existing, ~3%)', 18700),
        ('London (total area)', 1572),
        ('All UK solar farms\n(existing)', 300),
        ('Central Park, NYC', 3.4),
    ]

    names = [c[0] for c in comparisons][::-1]
    areas = [c[1] for c in comparisons][::-1]
    colors = [GREEN if 'rain' in n.lower() else LIGHT for n in names]

    ax.barh(range(len(names)), areas, color=colors, edgecolor=GREEN, linewidth=1)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel('Area (km²)')
    ax.set_title('How big is 2.4% of the\\nCentral African Republic?', fontsize=13)
    ax.set_xscale('log')

    plt.tight_layout()
    fig.savefig(f'{OUT}/area-comparison.png', dpi=150)
    plt.close()
    print('5/5 area-comparison.png')

print('All charts generated.')
