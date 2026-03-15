"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 5 : Distribution des durées de session – Histogramme
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

np.random.seed(0)

sessions_normales = np.random.exponential(scale=480, size=800)
sessions_signalees = np.concatenate([
    np.random.normal(loc=3800, scale=400, size=60),
    np.random.uniform(low=1, high=15, size=40)
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# ── ax1 : Sessions normales (échelle log) ─────────────────────────────────────
sns.histplot(sessions_normales, bins=40, color='steelblue', kde=False, ax=ax1)
ax1.set_xscale('log')
moy_n   = np.mean(sessions_normales)
med_n   = np.median(sessions_normales)
ax1.axvline(moy_n, color='red',    linestyle='--', linewidth=1.5, label=f'Moyenne : {moy_n:.0f}s')
ax1.axvline(med_n, color='orange', linestyle=':',  linewidth=1.5, label=f'Médiane : {med_n:.0f}s')
ax1.set_title('Sessions normales — Distribution (échelle log)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Durée (secondes) — échelle logarithmique', fontsize=10)
ax1.set_ylabel('Nombre de sessions', fontsize=10)
ax1.legend(fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.5)

# ── ax2 : Sessions signalées avec KDE ─────────────────────────────────────────
sns.histplot(sessions_signalees, bins=30, color='coral', kde=True, ax=ax2)
moy_s   = np.mean(sessions_signalees)
med_s   = np.median(sessions_signalees)
ax2.axvline(moy_s, color='darkred',    linestyle='--', linewidth=1.5, label=f'Moyenne : {moy_s:.0f}s')
ax2.axvline(med_s, color='darkorange', linestyle=':',  linewidth=1.5, label=f'Médiane : {med_s:.0f}s')
ax2.set_title('Sessions signalées — Distribution avec KDE', fontsize=12, fontweight='bold')
ax2.set_xlabel('Durée (secondes)', fontsize=10)
ax2.set_ylabel('Nombre de sessions', fontsize=10)
ax2.legend(fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('ex5_histo_durees.png', dpi=150)
plt.show()
print("ex5_histo_durees.png sauvegardé.")
