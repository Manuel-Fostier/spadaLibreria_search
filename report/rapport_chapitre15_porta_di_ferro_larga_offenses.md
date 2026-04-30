# Rapport : Cas d'utilisation des exemples du Chapitre 15 (Manciolino)
## Objet
Ce rapport analyse les sept exemples d'**offenses contre quelqu'un en porta di ferro larga** décrits au Chapitre 15 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
porta di ferro larga.*falso|falso.*roverso.*porta di ferro larga|punta trivellata|deux punte
```

---

## Exemple 1 — Falso + roverso
**Formulation :** « Contre quelqu'un en porta di ferro larga, tu peux lui frapper du falso et lui donner un roverso. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:347 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi [...] tu lui tireras un roverso à la face » — falso + roverso face depuis ou contre garde basse
- book3.md:102 — « tu pareras avec un falso de ton épée de bas en haut, et frappant avec un roverso sgualembrato à sa tempe droite » — falso + roverso = séquence standard

### Lecture
Le couple falso + roverso contre la porta di ferro larga est l'une des bottes les plus universelles du corpus. Marozzo la documente dans book1:32 et book3:102. La porta di ferro larga, garde basse à droite avec pointe vers le bas, est vulnérable au falso qui écarte sa lame avant le roverso.

---

## Exemple 2 — Falso + mandritto face (pied gauche pousse pied droit)
**Formulation :** « Ou frapper du falso et lui donner un mandritto à la face, en poussant le pied gauche et en passant avec le pied droit. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:349 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu frappes du falso [...] tu lui tireras un mandritto à la face » — falso + mandritto face = séquence canonique
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso [...] tu lui tailleras un mandritto sgualembrato à la face » — avec variation de pas similaire
- book3.md:134 — « tu frapperas du falso de ton épée vers l'extérieur [...] tu lui tailleras un mandritto sgualembrato à la face accompagné d'un tramazzone » — falso + mandritto face

### Lecture
Le falso + mandritto face avec mouvement de pied est documenté dans book1:32, book3:52 et book3:134. Ces trois passages confirment que cette séquence est l'une des bottes fondamentales contre toute garde basse dans la tradition bolognaise.

---

## Exemple 3 — Deux punte + fendente tête
**Formulation :** « Ou lui pousser deux punte et un fendente à la tête. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:351 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « tu lui pousseras une punta par l'extérieur de son épée à la face [...] tu avançant de ton pied droit fortement vers son côté gauche en lui chassant une autre punta [...] puis un fendente » — deux punte + fendente = séquence identique
- book3.md:240 — « tu pousseras une punta à l'ennemi [...] et lui en pousseras une autre » — doubles punte documentées

### Lecture
La séquence deux punte + fendente est documentée presque à l'identique dans Marozzo book1:56. C'est une attaque progressive qui exploite les deux lignes de la punta (extérieure et intérieure) avant de conclure avec le fendente.

---

## Exemple 4 — Pied droit + roverso tête
**Formulation :** « Ou avancer avec le pied droit et lui tirer un roverso à la tête. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:353 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « tu lui donneras un roverso à sa tempe droite » — roverso tête avec pas en avant
- book3.md:102 — « tu lui tireras un roverso à la tempe droite » — roverso tête depuis/contre garde basse

### Lecture
Le roverso tête avec avancée du pied droit est un coup simple et direct. Marozzo le documente dans book1:26 et book3:102. Contre la porta di ferro larga qui est une garde basse, l'avancée du pied droit en roverso est efficace car la tête adverse est exposée.

---

## Exemple 5 — Falso → guardia di faccia + tramazzone
**Formulation :** « Ou bien frapper du falso et, en fuyant avec le pied gauche derrière, te mettre en guardia di faccia pour tirer un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:355 — Définition de l'exemple

#### Marozzo
- book3.md:134 — « tu frapperas du falso de ton épée vers l'extérieur de son épée [...] et tu lui tailleras un mandritto sgualembrato à la face accompagné d'un tramazzone » — falso + tramazzone avec passage par garde intermédiaire
- book3.md:242 — « et dans ce pas tu tireras un roverso [...] tu te mettras en guardia di faccia » — guardia di faccia comme transition entre falso et coup final

### Lecture
La séquence falso → guardia di faccia → tramazzone est une attaque en deux temps. Le falso ouvre la ligne, la guardia di faccia est la position intermédiaire qui permet d'orienter le tramazzone. Marozzo book3:134 et book3:242 documentent les éléments de cette chaîne.

---

## Exemple 6 — Falso en guardia alta
**Formulation :** « Ou frapper du falso en montant en guardia alta. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:357 — Définition de l'exemple

#### Marozzo
- book3.md:262 — « tu frapperas du falso de ton épée de bas en haut en te levant en guardia alta » — falso en montant vers guardia alta = formulation quasi identique
- book3.md:420 — « tu peux lever en guardia alta dans le temps de sa frappe » — lever en guardia alta dans un temps adverse

### Lecture
Le falso de bas en haut en montant vers la guardia alta est documenté quasi à l'identique dans Marozzo book3:262. C'est un coup de transition qui intercepte en bas et remonte en haute garde pour préparer un mandritto.

---

## Exemple 7 — Punta trivellata + tramazzone
**Formulation :** « Ou lui pousser une punta trivellata et un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:359 — Définition de l'exemple
- opera_nova.md:713 — Reprise de la punta trivellata dans les assauts

#### Marozzo
- book3.md:188 — « tu lui pousseras une punta trivellata [...] tu tireras un tramazzone » — punta trivellata + tramazzone = séquence identique
- book3.md:659 — « tu lui pousseras une punta trivellata à la face » — punta trivellata documentée comme botte distincte

### Lecture
La punta trivellata (punta en vrille/rotation du poignet) est documentée chez Marozzo dans book3:188 avec exactement la même suite tramazzone. C'est une botte spécialisée dont l'existence dans les deux corpus confirme qu'il s'agit d'une technique codifiée de l'école bolognaise.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Falso + roverso | opera_nova:347 | book1:32, book3:102 |
| Ex2 - Falso + mandritto face | opera_nova:349 | book1:32, book3:52, book3:134 |
| Ex3 - Deux punte + fendente tête | opera_nova:351 | book1:56, book3:240 |
| Ex4 - Pied droit + roverso tête | opera_nova:353 | book1:26, book3:102 |
| Ex5 - Falso → guardia di faccia + tramazzone | opera_nova:355 | book3:134, book3:242 |
| Ex6 - Falso en guardia alta | opera_nova:357 | book3:262, book3:420 |
| Ex7 - Punta trivellata + tramazzone | opera_nova:359 | book3:188, book3:659 |

## Conclusion
Les sept offenses contre la porta di ferro larga de Manciolino sont toutes confirmées dans le corpus. La punta trivellata + tramazzone (Ex7) est particulièrement bien documentée dans Marozzo book3:188 avec la même séquence. Le falso + mandritto face (Ex2) est la botte la plus universelle du corpus. La porta di ferro larga, garde basse à droite, appelle le falso comme botte d'ouverture dans les deux traditions.
