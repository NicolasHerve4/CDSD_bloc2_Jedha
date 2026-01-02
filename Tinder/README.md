# 💕 Projet Tinder - Analyse Speed Dating

![Tinder Logo](https://full-stack-assets.s3.eu-west-3.amazonaws.com/M03-EDA/Tinder-Symbole.png)

## 📋 Description du Projet

Ce projet analyse les données d'événements de **speed dating** pour comprendre les dynamiques des relations humaines et identifier **les facteurs clés d'un match réussi**.

L'analyse s'appuie sur un dataset contenant les données de **523 participants** sur **21 sessions** (waves) de speed dating, soit **8 378 rencontres** au total.

---

## 🎯 Objectifs du Projet

Comprendre **les relations humaines** en répondant aux questions suivantes :

### Questions Principales
1. 🤔 **Est-ce que les hommes et les femmes ont les mêmes attentes ?**
2. 💘 **Pourquoi matche-t-on ?** Quels sont les critères déterminants ?
3. 🎓 **Le niveau social a-t-il une influence sur les matchs ?**
4. 👵👴 **Les attentes varient-elles selon l'âge ?**
5. 🪞 **Comment nous percevons-nous vs comment sommes-nous perçus ?**

---


## 🧹 Phase 1 : Nettoyage des Données notebook => 'nettoyage.ipynb'

## 📈 Phase 2 : Analyse Exploratoire des Données => 'Analyse.ipynb'

### Répartition par Genre
| Genre | Nombre | % |
|-------|--------|---|
| **Hommes** | 263 | 50,3% |
| **Femmes** | 260 | 49,7% |

**Insight** : Parité parfaite homme/femme dans l'échantillon.

### Répartition par Âge et Genre

| Tranche d'âge | Femmes | Hommes | Total |
|---------------|--------|--------|-------|
| 18-24 | 98 | 82 | 180 |
| 25-34 | 155 | 177 | 332 |
| 35-44 | 6 | 4 | 10 |
| 45-59 | 1 | 0 | 1 |

---

### Objectifs de Participation

**Pourquoi viennent-ils au speed dating ?**

| Objectif | Hommes | Femmes |
|----------|--------|--------|
| **Pour rencontrer de nouvelles personnes** | ~120 | ~115 |
| **Ça avait l'air amusant** | ~80 | ~75 |
| **Pour obtenir une date** | ~35 | ~40 |
| **Relation sérieuse** | ~20 | ~25 |

- **Les personnes ne viennent PAS pour trouver l'amour !**
---

**Répartition des Matchs par Âge**

| Tranche | Femmes | Hommes | Total |
|---------|--------|--------|-------|
| 18-24 | 180 | 150 | 330 |
| 25-34 | 480 | 510 | 990 |
| 35-44 | 8 | 6 | 14 |

---

### Préférences Déclarées : Hommes vs Femmes

#### Préférences Moyennes par Genre

| Critère | **Hommes** | **Femmes** |
|---------|------------|------------|
| **Attractivité** | **24,8** | 17,3 |
| **Intelligence** | 20,2 | **20,3** |
| **Fun** | 17,6 | 17,6 |
| **Sincérité** | 17,3 | 17,3 |
| **Intérêts partagés** | 11,8 | 11,8 |
| **Ambition** | 10,7 | 10,7 |

---

### Notes Données vs Notes Reçues (Matchs uniquement)

#### Notes Moyennes Reçues (sur 10)

| Critère | Femmes reçoivent | Hommes reçoivent |
|---------|------------------|------------------|
| **Intelligence** | 7,81 | **8,05** |
| **Sincérité** | 7,78 | 7,80 |
| **Attractivité** | **7,53** | 7,12 |
| **Fun** | 7,54 | 7,62 |
| **Ambition** | 7,17 | 7,45 |
| **Intérêts partagés** | 6,62 | 6,75 |

---

### Perception de Soi : Auto-évaluation vs Notes Reçues

#### Auto-évaluation Moyenne (sur 10)

| Critère | Femmes | Hommes |
|---------|--------|--------|
| **Sincérité** | **8,41** | 8,14 |
| **Intelligence** | 8,30 | **8,49** |
| **Fun** | 7,88 | 7,51 |
| **Ambition** | 7,61 | 7,57 |
| **Attractivité** | 7,21 | 6,95 |

---

### Conclusions Principales

#### 1. Les Critères de Match Réussi 💘

**Ce qui compte vraiment** :
1. **Attractivité** (pour les hommes : +43% d'importance)
2. **Intelligence** (pour les femmes : critère #1 dans les matchs réels)
3. **Équilibre global** : tous les critères entre 6,5 et 8/10

Les hommes priorisent l'attractivité mais matchent grâce à leur intelligence !

#### 3. Pourquoi Venir au Speed Dating ? 🎉

**Motivations** :
- **45%** : Rencontrer de nouvelles personnes
- **35%** : Passer une soirée amusante
- **10%** : Trouver une relation sérieuse

---

### Recommandations pour un Speed Dating


**Cibler** :
- **25-34 ans** : cœur de cible (63% des participants, 74% des matchs)
- **Professionnels urbains** : étudiants/jeunes actifs
- **Motivations sociales** : mise en avant de l'aspect "fun" vs "désespéré"

---

## 👤 Auteur

**Nicolas Hervé**
- Formation Jedha - Certification Data Science
