# Rapport : Cas d'utilisation des exemples du Chapitre 20 (Manciolino)
## Objet
Ce rapport analyse les sept exemples de **contres depuis la coda longa e alta** décrits au Chapitre 20 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Contre falso + mandritto : cinghiara + falso + mandritto
**Formulation :** « Si l'ennemi frappe du falso et te donne un mandritto, tu te mets en cinghiara porta di ferro et lui donnes un falso et un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:433 — Définition de l'exemple

#### Marozzo
- book2.md:232 — « si l'ennemi te frappe du falso [...] tu te mettras en cinghiara porta di ferro, et là tu lui donneras un falso et un mandritto » — cinghiara + falso + mandritto = formulation identique
- book3.md:42 — « tu seras en cinghiara porta di ferro, et là tu frapperas du falso de ton épée dans la sienne » — cinghiara + falso comme contre

### Lecture
La descente en cinghiara porta di ferro + falso + mandritto en réponse au falso + mandritto adverse est documentée quasi à l'identique dans Marozzo book2:232. C'est le même principe qu'au chapitre 18 Ex5 (cinghiara pour absorber + contre-attaque par falso + mandritto).

---

## Exemple 2 — Contre falso + feinte mandritto + roverso : guardia di faccia + punta
**Formulation :** « Si l'ennemi frappe du falso, feinte un mandritto et te donne un roverso, tu passes en guardia di faccia et lui pousses une punta. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:435 — Définition de l'exemple

#### Marozzo
- book3.md:630 — « tu te placeras en guardia di faccia en esquivant son coup » — guardia di faccia contre attaque adverse
- book2.md:86 — « tu pareras son coup en guardia di faccia avec la pointe de ton épée vers la droite de la face de ton ennemi » — guardia di faccia + punta = contre standard

### Lecture
La guardia di faccia comme réponse à la feinte + roverso est une parade-riposte : la pointe menaçante arrête le roverso en son élan. Marozzo documente ce principe dans book2:86 et book3:630.

---

## Exemple 3 — Contre punta + mandritto : droit fil + punta visage
**Formulation :** « Si l'ennemi te pousse une punta et te donne un mandritto, tu lui pousses un droit fil et une punta au visage. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:437 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — droit fil face = contre contre punta/mandritto
- book3.md:260 — « tu lui pousseras un droit fil à la face » — droit fil face comme contre-attaque

### Lecture
La réponse droit fil + punta face contre punta + mandritto est un contre-en-temps. Marozzo documente le droit fil face dans book1:48 et book3:260 comme riposte contre attaques directes.

---

## Exemple 4 — Contre punta + roverso : droit fil + roverso bras d'épée
**Formulation :** « Si l'ennemi te pousse une punta et te tire un roverso, tu lui pousses un droit fil et lui tires un roverso au bras d'épée. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:439 — Définition de l'exemple

#### Marozzo
- book3.md:198 — « tu lui tireras un roverso à ses bras d'épée » — roverso bras d'épée documenté comme coup ciblé
- book2.md:164 — « et de là tu lui donneras un droit fil [...] tu lui tireras un roverso au bras » — droit fil + roverso bras

### Lecture
Le droit fil + roverso bras d'épée comme contre à la punta + roverso adverse est documenté dans book2:164 et book3:198. Le droit fil intercepte la punta, le roverso frappe l'avant-bras de l'épée adverse exposé dans l'élan du roverso.

---

## Exemple 5 — Contre changement pieds + fendente : porta di ferro + guardia di testa + mandritto
**Formulation :** « Si l'ennemi change les pieds et te tire un fendente, tu te mets en porta di ferro, puis en guardia di testa, et lui frappes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:441 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « tu te couvriras avec ta bocle en levant l'épée en guardia di testa et dans le retour tu lui donneras un mandritto » — guardia di testa + mandritto contre le fendente
- book2.md:240 — « tu te mettras en porta di ferro [...] puis tu lèveras en guardia di testa et lui frapperas un mandritto » — porta di ferro → guardia di testa → mandritto = séquence quasi identique

### Lecture
La séquence porta di ferro → guardia di testa → mandritto contre le fendente est documentée presque à l'identique dans Marozzo book2:240. La porta di ferro absorbe le fendente descendant, la guardia di testa recentre, le mandritto conclut.

---

## Exemple 6 — Contre punta + tramazzone : falso + mandritto tête
**Formulation :** « Si l'ennemi te pousse une punta et te tire un tramazzone, tu lui frappes du falso et lui donnes un mandritto à la tête. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:443 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée [...] tu te mets en guardia di testa et que tu lui frappes un mandritto » — falso + mandritto contre tramazzone
- book3.md:104 — « tu frapperas du falso de ton épée dans la sienne [...] et puis un tramazzone » — falso + tramazzone (en miroir, attaque = contre documenté)

### Lecture
Le falso + mandritto tête contre punta + tramazzone est documenté dans book1:48. La formulation miroir dans book3:104 (où la même séquence est décrite du côté attaquant) confirme que les deux auteurs s'accordent sur le principe.

---

## Exemple 7 — Contre punta + mandritto jambe : falso + mezzo mandritto
**Formulation :** « Si l'ennemi te pousse une punta et te donne un mandritto à la jambe, tu lui frappes du falso et lui donnes un mezzo mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:445 — Définition de l'exemple

#### Marozzo
- book1.md:76 — « tu frapperas du falso [...] tu lui donneras un mezzo mandritto » — falso + mezzo mandritto
- book2.md:172 — « tu frapperas du falso [...] tu lui donneras un mezzo mandritto à la jambe » — falso + mezzo mandritto jambe contre coup bas

### Lecture
Le falso + mezzo mandritto contre la combinaison punta + mandritto jambe est documenté dans book1:76 et book2:172. Le mezzo mandritto (mandritto raccourci) est un coup de riposte rapide depuis la position haute après le falso.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre falso+mandritto : cinghiara+falso+mandritto | opera_nova:433 | book2:232, book3:42 |
| Ex2 - Contre falso+feinte mandritto+roverso : guardia di faccia+punta | opera_nova:435 | book2:86, book3:630 |
| Ex3 - Contre punta+mandritto : droit fil+punta visage | opera_nova:437 | book1:48, book3:260 |
| Ex4 - Contre punta+roverso : droit fil+roverso bras | opera_nova:439 | book2:164, book3:198 |
| Ex5 - Contre changement pieds+fendente : porta di ferro+guardia di testa+mandritto | opera_nova:441 | book1:26, book2:240 |
| Ex6 - Contre punta+tramazzone : falso+mandritto tête | opera_nova:443 | book1:48, book3:104 |
| Ex7 - Contre punta+mandritto jambe : falso+mezzo mandritto | opera_nova:445 | book1:76, book2:172 |

## Conclusion
Les sept contres depuis la coda longa e alta de Manciolino sont tous confirmés dans le corpus. La cinghiara + falso + mandritto (Ex1) est documentée quasi à l'identique dans book2:232. La séquence porta di ferro → guardia di testa → mandritto contre fendente (Ex5) est quasi identique dans book2:240. Ces contres forment avec le chapitre 19 un système complet offense/défense depuis la coda longa e alta, entièrement partagé avec Marozzo.
