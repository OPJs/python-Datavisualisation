"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 3 : Scatter Plot – Détection d'anomalies réseau
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Connexions normales
duree_normale  = np.random.normal(loc=30,  scale=8,  size=180)
volume_normal  = np.random.normal(loc=500, scale=80, size=180)

# Connexions suspectes
duree_suspecte = [180, 210, 5, 3, 195, 200]
volume_suspect = [8000, 9500, 8, 12, 7800, 10200]

fig, ax = plt.subplots(figsize=(10, 7))

# 1 — Tracé des points
ax.scatter(duree_normale, volume_normal,
           s=40, alpha=0.5, color='steelblue', label='Normal')
ax.scatter(duree_suspecte, volume_suspect,
           s=120, alpha=0.9, color='red', marker='X', label='Suspect', zorder=5)

# 2 — Annotations des 3 points suspects au plus grand volume
suspects_sorted = sorted(zip(volume_suspect, duree_suspecte), reverse=True)[:3]
for vol, dur in suspects_sorted:
    # BONUS — distance euclidienne au centroïde des normales
    cx, cy = np.mean(duree_normale), np.mean(volume_normal)
    dist = np.sqrt((dur - cx)**2 + (vol - cy)**2)
    ax.annotate(f'({dur}s, {vol}B)\nd={dist:.0f}',
                xy=(dur, vol),
                xytext=(dur + 8, vol - 600),
                fontsize=8, color='darkred',
                arrowprops=dict(arrowstyle='->', color='darkred'))

# 3 — Lignes de référence
ax.axvline(100,  color='orange', linestyle='--', linewidth=1.5, label='Seuil durée 100s')
ax.axhline(3000, color='darkorange', linestyle='--', linewidth=1.5, label='Seuil volume 3000B')

# 4 — Zone de danger (quadrant supérieur droit)
xlim = ax.get_xlim() if ax.get_xlim()[1] > 100 else (0, 220)
ylim = ax.get_ylim() if ax.get_ylim()[1] > 3000 else (0, 11000)
ax.set_xlim(-5, 225)
ax.set_ylim(-200, 11000)
ax.fill_betweenx([3000, 11000], 100, 225,
                 color='red', alpha=0.05, label='Zone de danger')

# 5 — Personnalisation
ax.set_title('Détection d\'anomalies réseau — Volume vs Durée de connexion',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Durée de la connexion (secondes)', fontsize=11)
ax.set_ylabel('Volume de données (octets)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('ex3_scatter_anomalie.png', dpi=150)
plt.show()
print("ex3_scatter_anomalie.png sauvegardé.")
