# Rapport : Cas d'utilisation des exemples du Chapitre 19 (Manciolino)
## Objet
Ce rapport analyse les sept exemples d'**offenses depuis la coda longa e alta, pied gauche devant** décrits au Chapitre 19 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
coda longa e alta.*falso|falso.*roverso.*coda longa|punta.*mandritto.*coda|coda longa e stretta
```

---

## Exemple 1 — Falso + mandritto
**Formulation :** « Depuis la coda longa e alta avec le pied gauche devant, tu peux frapper du falso et donner un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:417 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « depuis la porta di ferro [...] tu frappes du falso et tu lui tireras un mandritto à la face » — falso + mandritto depuis garde basse-gauche
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso de ton épée [...] tu lui tailleras un mandritto sgualembrato » — falso + mandritto
- book3.md:695 — « depuis coda longa e alta, tu frapperas du falso [...] tu lui donneras un mandritto » — falso + mandritto depuis coda longa e alta = formulation identique

### Lecture
Le falso + mandritto depuis la coda longa e alta est documenté quasi à l'identique dans Marozzo book3:695. C'est la botte principale depuis cette garde : le falso de bas en haut ouvre la ligne, le mandritto frappe en descendant.

---

## Exemple 2 — Falso + feinte mandritto + roverso
**Formulation :** « Ou bien frapper du falso, feinter un mandritto et lui donner un roverso. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:419 — Définition de l'exemple

#### Marozzo
- book3.md:695 — « depuis coda longa e alta, tu frapperas du falso [...] tu feinteras un mandritto et lui donneras un roverso » — falso + feinte mandritto + roverso = formulation identique

### Lecture
Cette séquence est documentée quasi à l'identique dans Marozzo book3:695. La feinte mandritto → roverso exploite la réaction adversaire : quand il couvre le mandritto, le roverso frappe le côté opposé découvert.

---

## Exemple 3 — Punta + mandritto
**Formulation :** « Ou lui pousser une punta et lui donner un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:421 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « tu lui pousseras une punta par l'extérieur [...] en lui chassant une autre punta » — punta + suite attaque
- book3.md:693 — « depuis coda longa e alta, tu pousseras une punta [...] tu lui tireras un mandritto » — punta + mandritto depuis coda longa e alta = formulation identique

### Lecture
La punta + mandritto depuis la coda longa e alta est documentée dans Marozzo book3:693. La garde pied gauche devant favorise la punta tendue vers l'avant, le mandritto suit dans l'ouverture créée.

---

## Exemple 4 — Punta + roverso
**Formulation :** « Ou lui pousser une punta et lui donner un roverso. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:423 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « tu lui pousseras une punta [...] tu lui tireras un roverso à la jambe » — punta + roverso
- book3.md:695 — « punta [...] tu lui tireras un roverso » — punta + roverso depuis coda longa e alta

### Lecture
La punta + roverso est une botte progressive en deux lignes. Marozzo documente cette séquence dans book3:695 et book1:56 dans des contextes où la punta haute force une défense qui expose le flanc au roverso.

---

## Exemple 5 — Changement de pieds + fendente
**Formulation :** « Ou changer les pieds et lui tirer un fendente. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:425 — Définition de l'exemple

#### Marozzo
- book2.md:198 — « en changeant les pieds [...] tu lui tireras un fendente à la tête » — changement de pieds + fendente
- book2.md:232 — « tu changeras les pieds et lui donneras un fendente » — changement de pieds + fendente comme botte depuis garde

### Lecture
Le changement de pieds + fendente est documenté dans Marozzo book2:198 et book2:232. C'est un coup qui exploite le changement de ligne : en inversant l'appui, on génère un fendente depuis l'autre côté.

---

## Exemple 6 — Punta + tramazzone
**Formulation :** « Ou lui pousser une punta et lui tirer un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:427 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « tu lui pousseras une punta [...] tu lui tireras un tramazzone » — punta + tramazzone
- book3.md:104 — « tu lui pousseras une punta de bas en haut [...] et puis un tramazzone » — punta + tramazzone = séquence identique

### Lecture
La punta + tramazzone est documentée dans book1:56 et book3:104. Le tramazzone conclut l'attaque initiée par la punta en frappant en arc de cercle depuis la position haute résultante.

---

## Exemple 7 — Punta + bocle sous épée + mandritto jambe
**Formulation :** « Ou lui pousser une punta, mettre ta bocle sous son épée, et lui donner un mandritto à la jambe. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:429 — Définition de l'exemple

#### Marozzo
- book1.md:56 — « tu tireras ton épée par la droite de la sienne en lui poussant ta bocle dans son poing d'épée [...] tu chasseras une autre punta à sa tempe droite » — bocle sous/dans épée adverse + suite
- book3.md:150 — « en passant ta bocle sous son épée et lui tirant un mandritto à la jambe » — bocle sous épée + mandritto jambe = formulation quasi identique

### Lecture
La bocle sous épée + mandritto jambe est documentée quasi à l'identique dans Marozzo book3:150, déjà vu au chapitre 17. Elle est donc confirmée dans deux chapitres de Manciolino et un passage précis de Marozzo.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Falso + mandritto | opera_nova:417 | book1:32, book3:52, book3:695 |
| Ex2 - Falso + feinte mandritto + roverso | opera_nova:419 | book3:695 |
| Ex3 - Punta + mandritto | opera_nova:421 | book1:56, book3:693 |
| Ex4 - Punta + roverso | opera_nova:423 | book1:56, book3:695 |
| Ex5 - Changement pieds + fendente | opera_nova:425 | book2:198, book2:232 |
| Ex6 - Punta + tramazzone | opera_nova:427 | book1:56, book3:104 |
| Ex7 - Punta + bocle sous épée + mandritto jambe | opera_nova:429 | book1:56, book3:150 |

## Conclusion
Les sept offenses depuis la coda longa e alta de Manciolino sont toutes confirmées dans le corpus, avec une concentration notable dans Marozzo book3:693-695 qui documente ces séquences directement depuis cette garde. Le falso + feinte mandritto + roverso (Ex2) trouve sa correspondance la plus directe dans book3:695. La coda longa e alta, garde basse à gauche avec épée vers la droite, génère naturellement les bottes fondées sur le falso montant et les punte tendues.
