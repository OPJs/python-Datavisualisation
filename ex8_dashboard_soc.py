"""
EFREI Paris — Master 1 Cybersécurité
TP Visualisation — Exercice 8 : Mini-projet – Dashboard SOC
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid', font_scale=0.9)
np.random.seed(99)

# ── Données ───────────────────────────────────────────────────────────────────
heures  = list(range(24))
entrant = [12,8,6,5,4,5,9,18,32,38,40,42,38,35,37,41,45,39,28,21,16,14,12,9]
sortant = [8,5,4,4,3,4,7,14,25,30,31,32,30,28,29,31,34,30,22,17,13,11,9,7]

top_ips = ['192.168.1.45','10.0.0.12','172.16.0.8','192.168.2.3',
           '10.0.0.99','192.168.1.120','172.16.0.55','10.0.0.200']
nb_conn = [342, 287, 198, 165, 134, 112, 98, 76]

types_ids = (['Port Scan']*45 + ['Brute Force']*32 + ['DDoS']*18 +
             ['SQLi']*12 + ['XSS']*8 + ['C2 Traffic']*5)
df_ids = pd.DataFrame({'type_alerte': types_ids})

durees_n  = np.random.normal(30, 8, 200)
volumes_n = np.random.normal(500, 80, 200)
durees_s  = [180, 200, 4, 2, 190, 195, 3]
volumes_s = [8500, 9200, 9, 7, 7900, 8800, 12]
classes   = ['Normal']*200 + ['Suspect']*7

# ── Figure 2x2 ────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# ── [0,0] Line plot : trafic entrant/sortant ──────────────────────────────────
ax = axes[0, 0]
ax.plot(heures, entrant, color='steelblue', linewidth=2, marker='o', markersize=3,
        label='Entrant (Mbps)')
ax.plot(heures, sortant, color='coral',     linewidth=2, marker='s', markersize=3,
        label='Sortant (Mbps)')
ax.set_title('Volume de trafic réseau — 24h', fontweight='bold')
ax.set_xlabel('Heure')
ax.set_ylabel('Mbps')
ax.set_xticks(range(0, 24, 2))
ax.legend(fontsize=8)

# ── [0,1] Bar chart horizontal : Top 8 IP ─────────────────────────────────────
ax = axes[0, 1]
# Tri décroissant (déjà trié dans les données)
couleurs_ip = ['#D32F2F']*3 + ['steelblue']*5  # 3 premières en rouge
ax.barh(top_ips[::-1], nb_conn[::-1], color=couleurs_ip[::-1])
ax.set_title('Top 8 IP source par nb connexions', fontweight='bold')
ax.set_xlabel('Nombre de connexions')
for i, (ip, n) in enumerate(zip(top_ips[::-1], nb_conn[::-1])):
    ax.text(n + 3, i, str(n), va='center', fontsize=8)
ax.set_xlim(0, max(nb_conn) * 1.15)

# ── [1,0] Countplot : alertes IDS ─────────────────────────────────────────────
ax = axes[1, 0]
order = df_ids['type_alerte'].value_counts().index
sns.countplot(data=df_ids, x='type_alerte', order=order,
              palette='Set2', ax=ax)
ax.set_title('Alertes IDS par type — journée', fontweight='bold')
ax.set_xlabel('Type d\'alerte')
ax.set_ylabel('Nombre d\'alertes')
ax.tick_params(axis='x', rotation=20)

# ── [1,1] Scatter : volume vs durée ──────────────────────────────────────────
ax = axes[1, 1]
all_x = list(durees_n) + durees_s
all_y = list(volumes_n) + volumes_s
colors_map = {'Normal': 'steelblue', 'Suspect': 'red'}
for cls in ['Normal', 'Suspect']:
    idx = [i for i, c in enumerate(classes) if c == cls]
    xs  = [all_x[i] for i in idx]
    ys  = [all_y[i] for i in idx]
    mk  = 'o' if cls == 'Normal' else 'X'
    sz  = 30 if cls == 'Normal' else 100
    al  = 0.5 if cls == 'Normal' else 0.9
    ax.scatter(xs, ys, s=sz, alpha=al, color=colors_map[cls],
               marker=mk, label=cls)
ax.set_title('Volume vs Durée — Détection d\'anomalies', fontweight='bold')
ax.set_xlabel('Durée (s)')
ax.set_ylabel('Volume (octets)')
ax.legend(fontsize=8)

# ── Titre global ──────────────────────────────────────────────────────────────
fig.suptitle('Dashboard SOC — 24h de surveillance réseau',
             fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('dashboard_soc.png', dpi=200, bbox_inches='tight')
plt.show()
print("dashboard_soc.png sauvegardé.")
