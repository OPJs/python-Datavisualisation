"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 1 : Trafic SSH – Courbe temporelle
"""

import matplotlib.pyplot as plt

heures = list(range(24))
tentatives = [3, 2, 1, 1, 2, 4, 8, 15, 22, 18, 20, 19,
              16, 21, 24, 30, 45, 38, 28, 18, 12, 8, 5, 3]
seuil_alerte = 25

fig, ax = plt.subplots(figsize=(12, 6))

# 1 — Courbe principale
ax.plot(heures, tentatives,
        color='steelblue', linewidth=2,
        marker='o', markersize=5,
        label='Tentatives SSH')

# 2 — Ligne seuil d'alerte
ax.axhline(seuil_alerte, color='red', linestyle='--', linewidth=1.5,
           label=f'Seuil alerte ({seuil_alerte})')

# 3 — Zone critique au-dessus du seuil
ax.fill_between(heures, tentatives, seuil_alerte,
                where=[t > seuil_alerte for t in tentatives],
                color='red', alpha=0.15,
                label='Zone critique')

# 4 — Personnalisation
ax.set_title('Trafic SSH — Tentatives de connexion sur 24h', fontsize=14, fontweight='bold')
ax.set_xlabel('Heure de la journée', fontsize=12)
ax.set_ylabel('Nb tentatives', fontsize=12)
ax.set_xticks(range(0, 24, 2))
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)

# BONUS — Annotation du pic maximum
pic_heure = tentatives.index(max(tentatives))
pic_val = max(tentatives)
ax.annotate(f'Pic : {pic_val} tentatives\n(heure {pic_heure}h)',
            xy=(pic_heure, pic_val),
            xytext=(pic_heure - 4, pic_val + 3),
            fontsize=9, color='darkred',
            arrowprops=dict(arrowstyle='->', color='darkred'))

# 5 — Sauvegarde et affichage
plt.tight_layout()
plt.savefig('ex1_ssh_trafic.png', dpi=150)
plt.show()
print("ex1_ssh_trafic.png sauvegardé.")
