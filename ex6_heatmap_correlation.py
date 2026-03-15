"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 6 : Heatmap – Matrice de corrélation des métriques réseau
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(7)
n = 720
base = np.random.normal(100, 15, n)

df = pd.DataFrame({
    'bande_passante_Mbps': base + np.random.normal(0, 5, n),
    'nb_connexions':       base * 0.8 + np.random.normal(20, 8, n),
    'latence_ms':          100 - base * 0.3 + np.random.normal(0, 10, n),
    'paquets_perdus_pct':  np.random.exponential(0.5, n),
    'cpu_firewall_pct':    base * 0.5 + np.random.normal(30, 6, n),
    'nb_alertes_ids':      np.random.poisson(3, n).astype(float)
})

# 1 — Matrice de corrélation
corr = df.corr().round(2)

# 3 — Masque triangle inférieur
mask = np.tril(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(9, 7))

# 2 — Heatmap
sns.heatmap(corr, annot=True, fmt='.2f',
            cmap='coolwarm', vmin=-1, vmax=1,
            linewidths=0.5, mask=mask,
            ax=ax, annot_kws={'size': 10})

# 4 — Labels pivotés
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=9)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=9)

# 5 — Titre
ax.set_title('Matrice de corrélation — Métriques réseau (30 jours)',
             fontsize=13, fontweight='bold', pad=15)

# BONUS — Paires fortement corrélées (|r| > 0.7)
print("\n=== Paires de métriques fortement corrélées (|r| > 0.7) ===")
cols = corr.columns.tolist()
paires = []
for i in range(len(cols)):
    for j in range(i + 1, len(cols)):
        r = corr.iloc[i, j]
        if abs(r) > 0.7:
            paires.append((cols[i], cols[j], r))
            print(f"  {cols[i]:25s} ↔  {cols[j]:25s}  r = {r:+.2f}")

plt.tight_layout()
plt.savefig('ex6_heatmap_correlation.png', dpi=150)
plt.show()
print("ex6_heatmap_correlation.png sauvegardé.")
