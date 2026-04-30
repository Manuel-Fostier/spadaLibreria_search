# Rapport : Cas d'utilisation des exemples du Chapitre 14 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples de **contres depuis la porta di ferro stretta** décrits au Chapitre 14 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
cinghiara porta di ferro|sotto braccio|punta.*main d.épée|falso.*mandritto.*face
```

---

## Exemple 1 — Contre tramazzone : mandritto face (pied droit)
**Formulation :** « Si l'ennemi te tire un tramazzone, tu avances avec le pied droit et lui tires un mandritto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:335 — Définition de l'exemple

#### Marozzo
- book3.md:92 — « contre un tramazzone, tu avances du pied droit et lui donnes un mandritto à la face dans son coup » — contre-en-temps avec avancée du pied droit + mandritto face = formulation quasi identique
- book1.md:32 — « dans ce retour, tu lui donneras un grand mandritto dans la tête » — mandritto tête comme contre-coup au tramazzone

### Lecture
Ce contre est l'un des plus directement documenté dans Marozzo book3:92 avec une formulation quasi identique. Avancer dans le tramazzone adverse permet de sortir de sa ligne en entrant en mesure courte, où un mandritto face est possible avant que le tramazzone ait terminé son arc.

---

## Exemple 2 — Contre punta + tramazzoni : couvrir + guardia di testa + mandritto
**Formulation :** « Si l'ennemi pousse une punta puis tire des tramazzoni, tu couvres la punta et tu passes en guardia di testa en lui frappant un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:337 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu te mets en guardia di testa et que tu lui frappes un mandritto ou une punta » — guardia di testa + mandritto comme contre au tramazzone
- book3.md:208 — « tu couvres la punta avec ta bocle [...] et dans ce même temps tu lui tires un mandritto tondo » — couverture punta + contre mandritto = structure identique

### Lecture
Le contre punta → couverture + guardia di testa → mandritto est un enchaînement codifié présent chez Marozzo dans book1:48 et book3:208. La guardia di testa est la garde intermédiaire entre la couverture de punta et le mandritto de riposte.

---

## Exemple 3 — Contre punta + feinte roverso : mandritto → guardia di faccia → roverso cuisse
**Formulation :** « Si l'ennemi pousse une punta et feinte un roverso pour te donner un mandritto, tu réalises un mandritto en guardant en guardia di faccia et tu lui tires un roverso à la cuisse. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:339 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « en répondant à sa punta, tu lui pousses ta bocle dans son poing d'épée, et dans ce pas tu lui tires un roverso à la cuisse » — riposte bocle + roverso cuisse dans un temps
- book3.md:188 — « dans le roverso cuisse tu te mets en guardia di faccia » — guardia di faccia → roverso cuisse

### Lecture
La séquence de contre à la feinte punta+roverso+mandritto par guardia di faccia → roverso cuisse exploite la vulnérabilité basse de l'adversaire lors de son attaque haute. Marozzo documente le roverso cuisse depuis guardia di faccia dans book3:188 et le passage bocle + roverso cuisse dans book1:56.

---

## Exemple 4 — Contre falso : cinghiara porta di ferro + punta
**Formulation :** « Si l'ennemi frappe du falso, tu te mets en cinghiara porta di ferro et lui pousses une punta. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:343 — Définition de l'exemple

#### Marozzo
- book3.md:120 — « tu feras une cinghiara porta di ferro, et là tu pousses une punta à la cuisse » — cinghiara porta di ferro + punta = séquence identique
- book3.md:132 — « depuis la cinghiara porta di ferro, tu pousseras une punta à l'ennemi » — cinghiara + punta confirmée
- book1.md:32 — Transition vers garde basse + punta comme réponse au falso

### Lecture
La réponse au falso par descente en cinghiara + punta est documentée dans Marozzo book3:120 de façon identique. Le falso adverse crée un moment où la ligne basse est ouverte, que la cinghiara exploite immédiatement.

---

## Exemple 5 — Contre tramazzone : falso + mandritto face
**Formulation :** « Si l'ennemi tire un tramazzone, tu lui frappes du falso et lui donnes un mandritto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:345 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi [...] tu lui tireras un mandritto à la face » — falso dans épée + mandritto face
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — falso + suite à la face contre coup circulaire

### Lecture
Ce contre reprend la séquence universelle falso + mandritto face, ici appliquée au tramazzone. Le falso intercepte le tramazzone en son arc descendant et redirige vers un mandritto. Marozzo documente cette riposte dans book1:32 et book1:48.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre tramazzone : mandritto face pied droit | opera_nova:335 | book1:32, book3:92 |
| Ex2 - Contre punta+tramazzoni : guardia di testa+mandritto | opera_nova:337 | book1:48, book3:208 |
| Ex3 - Contre punta+feinte roverso : guardia di faccia+roverso cuisse | opera_nova:339 | book1:56, book3:188 |
| Ex4 - Contre falso : cinghiara porta di ferro+punta | opera_nova:343 | book1:32, book3:120, book3:132 |
| Ex5 - Contre tramazzone : falso+mandritto face | opera_nova:345 | book1:32, book1:48 |

## Conclusion
Les cinq contres depuis la porta di ferro stretta de Manciolino correspondent tous à des techniques bien documentées dans le corpus. Le contre au tramazzone par pied droit + mandritto face (Ex1) est documenté quasi à l'identique dans Marozzo book3:92. La cinghiara + punta contre le falso (Ex4) est confirmée dans book3:120. Ces contres complètent le tableau des chapitres 13-14 sur la porta di ferro stretta, confirmant la cohérence des deux auteurs sur les défenses depuis cette garde.
