# Rapport : Cas d'utilisation des exemples du Chapitre 10 (Manciolino)
## Objet
Ce rapport analyse les dix exemples de **contres depuis la guardia di sopra braccio** décrits au Chapitre 10 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
roverso spinto|sopra braccio|punta roversa|roverso.*fendente.*tramazzone
```

---

## Exemple 1 — Contre deux roversi : couvrir le 1er + roverso spinto face
**Formulation :** « Si l'ennemi te tire deux roversi, tu couvres le premier avec ta bocle et lui donnes un roverso spinto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:275 — Définition de l'exemple

#### Marozzo
- book1.md:42 — « tu te mettras en guardia di testa [...] dans ce temps, tu lui donneras un roverso sgualembrato à sa tempe droite » — couverture en garde + roverso
- book3.md:424 — « étant en guardia di sopra braccio, si quelqu'un vient contre toi avec un roverso [...] tu passeras vers son côté gauche en lui donnant un roverso en même temps » — contre-roverso depuis sopra braccio

### Lecture
La riposte par roverso spinto après avoir couvert un roverso adverse avec la bocle est une parade-riposte classique. Marozzo documente la riposte par roverso depuis sopra braccio dans book3:424 et la couverture par bocle + roverso dans book1:42.

---

## Exemple 2 — Contre deux roversi + mandritto : cinghiara porta di ferro + falso + roverso
**Formulation :** « Si l'ennemi tire deux roversi et un mandritto, tu descends en cinghiara porta di ferro en laissant passer les deux roversi, puis tu frappes du falso et lui tires un roverso. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:277 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu lâches l'épée sur sa jambe [cinghiara porta di ferro] en fuyant du pied gauche derrière le droit [...] tu leveras l'épée en guardia alta [...] tu lui donneras un grand mandritto dans la tête » — descente en garde basse pour laisser passer puis contre
- book3.md:42 — « tu seras en cinghiara porta di ferro, et là tu frapperas du falso de ton épée dans la sienne et de l'autre côté tu lui donneras un roverso » — cinghiara + falso + roverso = séquence identique

### Lecture
La séquence cinghiara porta di ferro → falso → roverso est documentée quasi à l'identique dans Marozzo book3:42. C'est l'un des contres les mieux partagés entre les deux auteurs : la cinghiara absorbe ou évite les coups hauts, le falso écarte l'épée adverse, le roverso conclut.

---

## Exemple 3 — Contre roverso intérieur bocle : mandritto face
**Formulation :** « Si l'ennemi tire un roverso à l'intérieur de ta bocle, tu lui tires un mandritto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:281 — Définition de l'exemple

#### Marozzo
- book1.md:20 — « tu avances du pied droit d'un grand pas en avant et que tu tailles un roverso sgualembrato dans le rebord de ta bocle. Si celui-ci met en défaut ma bocle et m'atteint la jambe [...] mets-toi en guardia di testa et tire-lui un mandritto » — roverso dans bocle + réponse mandritto
- book1.md:42 — « et dans ce déplacement tu frapperas du pied en demi-volte en repassant [...] lui donnant un mandritto à la tempe gauche » — contre-mandritto face comme réponse au roverso

### Lecture
La réponse mandritto face au roverso intérieur bocle est logique : le roverso qui passe à l'intérieur crée une ouverture sur la ligne du mandritto adverse. Marozzo book1:20 et book1:42 documentent cette réponse.

---

## Exemple 4 — Contre feinte roverso + mandritto : guardia di faccia → roverso tempe
**Formulation :** « Si l'ennemi feinte un roverso et te donne un mandritto, tu passes en guardia di faccia et lui frappes un roverso à la tempe droite. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:283 — Définition de l'exemple

#### Marozzo
- book3.md:426 — « s'il te fait une feinte de mandritto pour te donner un roverso, alors tu lèveras en guardia alta dans cette feinte de mandritto, et dans sa frappe de roverso tu lui donneras un mandritto à sa tempe gauche » — contre la feinte par lever en garde haute + frappe en temps adverse
- book3.md:630 — « tu te placeras en guardia di faccia en esquivant son coup » — guardia di faccia comme parade contre frappe

### Lecture
Contre la feinte roverso → mandritto, descendre en guardia di faccia (qui couvre le mandritto par la pointe menaçante) et frapper un roverso à la tempe est un contre-en-temps. Marozzo book3:426 documente le principe général avec des variantes.

---

## Exemple 5 — Contre pied gauche + feinte roverso : guardia di faccia → roverso traversant
**Formulation :** « Si l'ennemi avance avec le pied gauche en feintant un roverso, tu passes en guardia di faccia et lui tires un roverso traversant. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:285 — Définition de l'exemple

#### Marozzo
- book3.md:218 — « tu passeras avec le pied gauche vers son côté droit [...] te couvrant avec un roverso sgualembrato traversant sa tempe droite » — passage + roverso traversant
- book3.md:634 — « et dans ce temps tu lui donneras un roverso sgualembrato à travers la tête ou la face » — roverso traversant comme coup de finition

### Lecture
Le roverso traversant (sgualembrato) contre une attaque de pied gauche + feinte est documenté chez Marozzo dans plusieurs contextes. La guardia di faccia comme position intermédiaire de couverture est implicite dans la séquence book3:218.

---

## Exemple 6 — Contre punta roversa : épée + tramazzoni ; guardia di testa + mandritto
**Formulation :** « Si l'ennemi pousse une punta roversa, tu la pares avec ton épée et lui tires des tramazzoni, ou bien tu te mets en guardia di testa et lui donnes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:285-287 — Définition de l'exemple (deux options)

#### Marozzo
- book2.md:176 — « tu lui donneras un mezzo roverso par-dessus son bras droit avec une punta roversa à la poitrine » — punta roversa documentée avec riposte intégrée
- book2.md:223 — « tu pousseras une punta roversa à la face, et dans le même temps tu sauteras avec les deux pieds » — punta roversa avec saut défensif
- book1.md:48 — « tu te mets en guardia di testa et que tu lui frappes un mandritto » — guardia di testa + mandritto comme réponse standard

### Lecture
La parade de la punta roversa par l'épée + tramazzoni est une réponse dynamique qui utilise le propre mouvement de la punta adverse. La variante par guardia di testa + mandritto est documentée chez Marozzo dans book1:48 comme contre standard.

---

## Exemple 7 — Contre roverso + fendente + tramazzone : trois contres distincts
**Formulation :** « Si l'ennemi tire un roverso, tu mets ta punta dans sa main et ta bocle par-dessus son bras. Si un fendente, tu passes en guardia di testa. Si un tramazzone, tu sautes. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:287-289 — Définition des trois contres

#### Marozzo
- book1.md:26 — « tu te couvriras avec ta bocle en levant l'épée en guardia di testa et dans le retour tu lui donneras un mandritto » — guardia di testa contre fendente
- book3.md:104 — « contre le tramazzone tu passeras le pied gauche vers l'extérieur » — passage de pied contre tramazzone
- book1.md:34 — « contre le roverso tu pousseras ta bocle sur son poing d'épée » — bocle sur poing contre roverso

### Lecture
Ces trois contres distincts selon le type de coup adverse sont des réponses codifiées. Marozzo documente chacun séparément : bocle sur poing contre roverso (book1:34), guardia di testa contre fendente (book1:26), fuite de pied contre tramazzone (book3:104).

---

## Exemple 8 — Contre pied gauche + punta vers bras : roverso cuisse
**Formulation :** « Si l'ennemi passe avec le pied gauche en poussant une punta vers ton bras, tu lui tires un roverso à la cuisse. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:289 — Définition de l'exemple

#### Marozzo
- book1.md:38 — « tu lui tourneras alors un roverso in falso à sa tempe gauche. Si lui veut couvrir ce côté ci-dessus, tu lui tourneras un roverso à sa cuisse droite » — roverso cuisse comme coup de remplacement si défense haute
- book3.md:198 — « tu peux l'atteindre à la cuisse ou à la jambe avec un roverso » — roverso cuisse comme alternative standard

### Lecture
Le roverso à la cuisse en réponse à une punta au bras adverse est un contre en ligne basse. Marozzo documente le roverso cuisse dans book1:38 comme coup de substitution quand la défense haute est couverte.

---

## Exemple 9 — Contre deux tramazzoni : guardia di testa + punta face
**Formulation :** « Si l'ennemi tire deux tramazzoni, tu passes en guardia di testa et lui pousses une punta à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:291 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu te mets en guardia di testa et que tu lui frappes un mandritto ou une punta » — guardia di testa + contre sur le tramazzone
- book3.md:124 — « tu attendras que l'ennemi tire un tramazzone [...] et dans sa frappe de tramazzone tu lui pousseras une punta entre les bras » — punta face dans le temps du tramazzone

### Lecture
Contre le tramazzone, la guardia di testa permet de couvrir le coup et de riposte en punta face dans l'intervalle. Marozzo documente ce contre dans book1:48 et book3:124 de façon quasi identique.

---

## Exemple 10 — Contre roverso spinto : falso tempe + bocle
**Formulation :** « Si l'ennemi tire un roverso spinto, tu lui frappes du falso à la tempe et tu le pousses avec ta bocle. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:293 — Définition de l'exemple

#### Marozzo
- book1.md:34 — « tu lui donneras du falso à ses mains » — falso comme réponse au roverso
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi » — falso offensif comme remise après roverso adverse
- book1.md:56 — « tu lui pousseras ta bocle dans son poing d'épée » — bocle utilisée comme arme contre le poing adverse

### Lecture
Le falso à la tempe + bocle contre le roverso spinto est un contre coordonné épée-bocle. Marozzo documente l'usage du falso contre le roverso (book1:34) et l'usage de la bocle sur le poing adverse (book1:56) dans des séquences distinctes mais complémentaires.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre deux roversi : roverso spinto | opera_nova:275 | book1:42, book3:424 |
| Ex2 - Contre 2 roversi+mandritto : cinghiara+falso+roverso | opera_nova:277 | book1:32, book3:42 |
| Ex3 - Contre roverso bocle : mandritto face | opera_nova:281 | book1:20, book1:42 |
| Ex4 - Contre feinte roverso+mandritto : guardia di faccia+roverso | opera_nova:283 | book3:426, book3:630 |
| Ex5 - Contre pied gauche+feinte roverso : roverso traversant | opera_nova:285 | book3:218, book3:634 |
| Ex6 - Contre punta roversa : tramazzoni ou guardia di testa+mandritto | opera_nova:285-287 | book1:48, book2:176, book2:223 |
| Ex7 - Contre roverso/fendente/tramazzone (3 contres) | opera_nova:287-289 | book1:26, book1:34, book3:104 |
| Ex8 - Contre punta vers bras : roverso cuisse | opera_nova:289 | book1:38, book3:198 |
| Ex9 - Contre deux tramazzoni : guardia di testa+punta | opera_nova:291 | book1:48, book3:124 |
| Ex10 - Contre roverso spinto : falso+bocle | opera_nova:293 | book1:34, book1:56, book3:52 |

## Conclusion
Les dix contres depuis la guardia di sopra braccio de Manciolino sont parmi les mieux documentés dans le corpus. La cinghiara porta di ferro contre la rafale roversi+mandritto (Ex2) trouve un écho quasi identique dans Marozzo book3:42. Le contre aux deux tramazzoni par guardia di testa+punta (Ex9) est également très directement confirmé par book1:48 et book3:124. Ce chapitre illustre comment la sopra braccio est une garde fondamentalement défensive/réactive dans la tradition bolognaise.
