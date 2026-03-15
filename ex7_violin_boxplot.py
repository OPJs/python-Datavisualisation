"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 7 : Violin + Boxplot – Comparaison par protocole
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(12)

data = {
    'HTTP':  np.random.normal(loc=800, scale=200, size=300).clip(60, 1500),
    'HTTPS': np.random.normal(loc=950, scale=180, size=300).clip(60, 1500),
    'SSH':   np.concatenate([
                 np.random.normal(60,  10,  250),
                 np.random.normal(900, 150, 50)
             ]),
    'DNS':   np.concatenate([
                 np.random.normal(80,  20,  260),
                 np.random.normal(600, 100, 40)
             ])
}
df = pd.DataFrame(data).melt(var_name='protocole', value_name='taille_octets')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 2 — Violin plot
sns.violinplot(data=df, x='protocole', y='taille_octets',
               palette='Set2', ax=ax1)
ax1.axhline(400, color='red', linestyle='--', linewidth=1.5, label='Seuil 400 octets')
ax1.set_title('Distribution des tailles de paquets\n(Violin plot)', fontsize=11, fontweight='bold')
ax1.set_xlabel('Protocole', fontsize=10)
ax1.set_ylabel('Taille (octets)', fontsize=10)
ax1.legend(fontsize=9)

# 3 — Boxplot + stripplot superposé
sns.boxplot(data=df, x='protocole', y='taille_octets',
            palette='Set2', ax=ax2)
sns.stripplot(data=df, x='protocole', y='taille_octets',
              alpha=0.3, jitter=True, color='black', size=2, ax=ax2)
ax2.axhline(400, color='red', linestyle='--', linewidth=1.5, label='Seuil 400 octets')

# BONUS — % paquets DNS > 400 octets
dns_data = df[df['protocole'] == 'DNS']['taille_octets']
pct_dns = (dns_data > 400).mean() * 100
color_titre = 'red' if pct_dns > 10 else 'black'
ax2.set_title(f'Distribution des tailles de paquets (Boxplot)\n'
              f'DNS > 400 oct. : $\\bf{{{pct_dns:.1f}\\%}}$',
              fontsize=11, fontweight='bold', color=color_titre)
ax2.set_xlabel('Protocole', fontsize=10)
ax2.set_ylabel('Taille (octets)', fontsize=10)
ax2.legend(fontsize=9)

fig.suptitle('Analyse des tailles de paquets par protocole — Détection de comportements anormaux',
             fontsize=13, fontweight='bold', y=1.01)

plt.tight_layout()
plt.savefig('ex7_violin_boxplot.png', dpi=150, bbox_inches='tight')
plt.show()
print("ex7_violin_boxplot.png sauvegardé.")
