"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 4 : Répartition des protocoles – Donut Chart
"""

import matplotlib.pyplot as plt

protocoles  = ['HTTPS', 'HTTP', 'DNS', 'SSH', 'FTP', 'SMTP', 'Autre']
volumes_gb  = [48.3, 12.1, 5.8, 3.2, 1.9, 2.7, 4.1]
couleurs    = ['#2196F3','#64B5F6','#4CAF50','#FF5722','#FFC107','#9C27B0','#78909C']
BLUE_DARK   = '#0D47A1'

# BONUS — deux graphiques côte à côte
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# ── Graphique gauche : Donut ──────────────────────────────────────────────────
explode = [0, 0, 0, 0.08, 0, 0, 0]   # SSH mis en évidence

wedges, texts, autotexts = ax.pie(
    volumes_gb,
    labels=protocoles,
    colors=couleurs,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    pctdistance=0.78,
)

# 3 — Trou central (donut effect)
circle = plt.Circle((0, 0), 0.6, color='white')
ax.add_patch(circle)
total = sum(volumes_gb)
ax.text(0, 0, f'{total:.1f} Go', ha='center', va='center',
        fontsize=16, fontweight='bold', color=BLUE_DARK)

# 4 — Légende externe avec valeurs en Go
ax.legend(wedges,
          [f'{p} — {v:.1f} Go' for p, v in zip(protocoles, volumes_gb)],
          loc='lower left', bbox_to_anchor=(-0.35, -0.05),
          fontsize=8.5)

ax.set_title('Répartition du trafic par protocole', fontsize=12, fontweight='bold', pad=15)

# ── Graphique droit : Bar chart horizontal (BONUS) ────────────────────────────
sorted_pairs = sorted(zip(volumes_gb, protocoles, couleurs), reverse=True)
vols_s, prots_s, cols_s = zip(*sorted_pairs)

bars = ax2.barh(prots_s, vols_s, color=cols_s, edgecolor='white')
ax2.bar_label(bars, fmt='%.1f Go', padding=4, fontsize=9)
ax2.set_xlabel('Volume (Go)', fontsize=10)
ax2.set_title('Volume par protocole (trié)', fontsize=12, fontweight='bold')
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='--', alpha=0.4)

# 5 — Sauvegarde
plt.tight_layout()
plt.savefig('ex4_pie_protocoles.png', dpi=150)
plt.show()
print("ex4_pie_protocoles.png sauvegardé.")
