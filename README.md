# 📊 Data Visualisation — Sécurité Réseau & Monitoring SOC


Projet réalisé dans le cadre du Master 1 Cybersécurité (EFREI Paris).  
Série de 8 scripts Python produisant des visualisations appliquées à l'analyse de logs,  
la détection d'anomalies et le monitoring réseau.


## 🛠️ Stack technique
Python 3 · Matplotlib · Seaborn · NumPy · Pandas

## 📁 Scripts

| Fichier | Type de graphique | Contexte |
|---|---|---|
| `ex1_ssh_trafic.py` | Line plot | Détection de pics de tentatives SSH sur 24h |
| `ex2_alertes_barres.py` | Bar chart groupé | Comparaison d'alertes SIEM sur 2 semaines |
| `ex3_scatter_anomalie.py` | Scatter plot | Détection d'exfiltration de données (outliers) |
| `ex4_pie_protocoles.py` | Donut chart | Répartition du trafic réseau par protocole |
| `ex5_histo_durees.py` | Histogramme + KDE | Distribution des durées de session (proxy) |
| `ex6_heatmap_correlation.py` | Heatmap | Corrélation de métriques SNMP sur 30 jours |
| `ex7_violin_boxplot.py` | Violin + Boxplot | Comparaison des tailles de paquets par protocole |
| `ex8_dashboard_soc.py` | Dashboard 4 graphiques | Tableau de bord SOC — 24h de surveillance réseau |





## 🔍 Compétences illustrées
- Analyse et visualisation de logs Apache et SSH
- Détection visuelle d'anomalies et de comportements suspects
- Comparaison de distributions par groupe (violin, boxplot)
- Analyse de corrélation multivariée (heatmap)
- Conception d'un dashboard de supervision (subplots, mise en page)

![ex1_ssh_trafic.png](ex1_ssh_trafic.png)

![ex2_alertes_barres.png](ex2_alertes_barres.png)


![ex2_alertes_barres.png](ex3_scatter_anomalie.png)


![ex2_alertes_barres.png](ex4_pie_protocoles.png)



![ex2_alertes_barres.png](ex5_histo_durees.png)


![ex2_alertes_barres.png](ex6_heatmap_correlation.png)

![ex2_alertes_barres.png](ex7_violin_boxplot.png)


![ex2_alertes_barres.png](dashboard_soc.png)
