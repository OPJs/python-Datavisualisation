"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 2 : Alertes par type – Barres groupées
"""

import matplotlib.pyplot as plt
import numpy as np

types_alertes = ['Brute Force', 'Port Scan', 'DDoS', 'Phishing', 'Malware', 'Exfil.']
semaine_1 = [42, 28, 15, 33, 19, 8]
semaine_2 = [67, 31, 9, 45, 27, 14]

x = np.arange(len(types_alertes))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# 1 & 2 — Barres groupées
bars1 = ax.bar(x - width / 2, semaine_1, width, label='Semaine 1', color='steelblue')
bars2 = ax.bar(x + width / 2, semaine_2, width, label='Semaine 2', color='coral')

# 3 — Valeurs au-dessus des barres
ax.bar_label(bars1, padding=2, fontsize=9)
ax.bar_label(bars2, padding=2, fontsize=9)

# BONUS — Taux d'évolution S1 → S2
for i, (s1, s2) in enumerate(zip(semaine_1, semaine_2)):
    taux = (s2 - s1) / s1 * 100
    couleur = 'red' if taux > 30 else ('green' if taux < 0 else 'black')
    signe = '+' if taux >= 0 else ''
    ax.text(x[i] + width / 2, s2 + 4,
            f'{signe}{taux:.0f}%',
            ha='center', va='bottom', fontsize=7.5,
            color=couleur, fontweight='bold')

# 4 — Personnalisation
ax.set_title('Alertes de sécurité par type — Comparaison S1 vs S2', fontsize=13, fontweight='bold')
ax.set_xlabel('Type d\'alerte', fontsize=11)
ax.set_ylabel('Nombre d\'alertes', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(types_alertes, rotation=20, ha='right')
ax.legend(fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# 5 — Sauvegarde
plt.tight_layout()
plt.savefig('ex2_alertes_barres.png', dpi=150)
plt.show()
print("ex2_alertes_barres.png sauvegardé.")
