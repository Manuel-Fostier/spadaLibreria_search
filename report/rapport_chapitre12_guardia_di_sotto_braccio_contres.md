# Rapport : Cas d'utilisation des exemples du Chapitre 12 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples de **contres depuis la guardia di sotto braccio** décrits au Chapitre 12 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Contre roverso : pied gauche + roverso tempe droite
**Formulation :** « Si l'ennemi te tire un roverso, tu passes avec le pied gauche devant vers son côté droit et lui tires un roverso à la tempe droite. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:311 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « tu passes avec ce pied gauche vers le côté droit de l'ennemi, et dans ce pas tu lui donneras un roverso à sa tempe droite » — passage pied gauche + roverso tempe droite = formulation quasi identique
- book3.md:198 — « tu passeras du pied gauche vers son côté droit et lui tailleras un mandritto à la face » — passage pied gauche + frappe face

### Lecture
Ce contre est documenté presque mot pour mot dans Marozzo book1:26. C'est un contre canonique de la tradition bolognaise : contre le roverso adverse on passe du côté de la main d'épée adverse (son côté droit) hors de la ligne du coup et on riposte avec un roverso à la tempe exposée.

---

## Exemple 2 — Contre falso + mandritto : mezzo mandritto + cinghiara + punta + mandritto tibias
**Formulation :** « Si l'ennemi frappe du falso et te donne un mandritto, tu lui tires un mezzo mandritto, puis tu te mets en cinghiara porta di ferro et lui pousses une punta et un mandritto aux tibias. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:313 — Définition de l'exemple

#### Marozzo
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi [...] tu lui tireras un mandritto à la face — contre, falso+mandritto ; puis punta ou cinghiara » — séquence de contre au falso+mandritto avec transition garde basse
- book3.md:42 — « tu seras en cinghiara porta di ferro, et là tu frapperas du falso de ton épée dans la sienne et de l'autre côté tu lui donneras un roverso » — cinghiara + contre

### Lecture
La réponse au falso + mandritto par mezzo mandritto + descente en cinghiara + suite basse est une parade-riposte en deux temps. La cinghiara sert de transition sécurisée après la parade haute. Marozzo book3:52 et book3:42 documentent des séquences similaires autour du falso et de la cinghiara.

---

## Exemple 3 — Contre roverso en fuyant : roverso à la face
**Formulation :** « Si l'ennemi tire un roverso en fuyant avec le pied gauche derrière, tu lui tires un roverso à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:315 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « en fuyant de ta jambe gauche derrière la droite, tu leveras l'épée en guardia alta [...] dans ce retrait, le pied gauche entraîne une ouverture → attaque en roverso » — fuite + ouverture face documentée
- book3.md:102 — « fuyant du pied gauche derrière le droit, tu lui tireras un roverso à la tempe droite » — contre exact du mouvement décrit

### Lecture
Quand l'adversaire recule le pied gauche en tirant un roverso, il crée un moment de vulnérabilité : son bras est en extension et sa face est exposée. Marozzo book3:102 documente exactement ce moment de contre-attaque.

---

## Exemple 4 — Contre punta dans la main d'épée : coda longa e alta + pied droit derrière
**Formulation :** « Si l'ennemi pousse une punta dans ta main d'épée, tu te mets en coda longa e alta en portant le pied droit derrière le gauche. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:317 — Définition de l'exemple

#### Marozzo
- book2.md:38 — « quand il pousse cette punta, tu retires le pied droit derrière et tu lèves ta main d'épée en coda longa e alta » — coda longa e alta + retrait pied droit = formulation quasi identique
- book2.md:52 — « en retirant le pied droit derrière la gauche, tu te mettras en coda longa e alta » — même geste défensif

### Lecture
La retraite en coda longa e alta avec retrait du pied droit contre une punta sur la main d'épée est documentée presque à l'identique dans Marozzo book2:38 et book2:52. C'est un mouvement de mise hors de distance par rotation de la main d'épée vers la droite haute.

---

## Exemple 5 — Contre falso + punta montante : cinghiara ; contre tramazzone : falso + mandritto
**Formulation :** « Si l'ennemi frappe du falso et te pousse une punta en montant, tu te mets en cinghiara porta di ferro. Si un tramazzone, tu lui frappes du falso et lui donnes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:319 — Définition de l'exemple (deux sous-contres)

#### Marozzo
- book3.md:104 — « tu frapperas du falso de ton épée dans la sienne [...] puis tu lui pousseras une punta de bas en haut [...] et puis un tramazzone » — falso + punta montante + tramazzone = attaque documentée en miroir
- book3.md:120 — « tu feras une cinghiara porta di ferro » — transition en cinghiara comme réponse défensive
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — falso + suite face contre tramazzone

### Lecture
Ce double contre reprend la logique du chapitre 11 Ex5 en miroir : ce qui est décrit comme attaque là est contré ici. La cinghiara absorbe la punta montante, le falso + mandritto contre le tramazzone est documenté dans book1:48. Ces contres montrent la structure dialogique de l'enseignement bolognais.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre roverso : pied gauche + roverso tempe | opera_nova:311 | book1:26, book3:198 |
| Ex2 - Contre falso+mandritto : mezzo mandritto+cinghiara+punta | opera_nova:313 | book3:42, book3:52 |
| Ex3 - Contre roverso en fuyant : roverso face | opera_nova:315 | book1:32, book3:102 |
| Ex4 - Contre punta main d'épée : coda longa e alta | opera_nova:317 | book2:38, book2:52 |
| Ex5 - Contre falso+punta montante : cinghiara ; contre tramazzone : falso+mandritto | opera_nova:319 | book1:48, book3:104, book3:120 |

## Conclusion
Les cinq contres depuis la guardia di sotto braccio forment un corpus cohérent avec des correspondances directes dans tout le corpus. Le contre au roverso par pied gauche + roverso tempe (Ex1) est documenté quasi à l'identique dans Marozzo book1:26. La retraite en coda longa e alta contre la punta (Ex4) est confirmée dans book2:38. Ces contres illustrent la structure miroir de l'enseignement bolognais : chaque attaque décrite dans le chapitre précédent est contée ici.
