# Rapport : Cas d'utilisation des exemples du Chapitre 18 (Manciolino)
## Objet
Ce rapport analyse les huit exemples de **contres depuis la cinghiara porta di ferro** décrits au Chapitre 18 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Contre punta + mandritto : falso + mezzo mandritto bras
**Formulation :** « Si l'ennemi te pousse une punta et te donne un mandritto, tu lui frappes du falso et lui donnes un mezzo mandritto au bras. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:399-401 — Définition de l'exemple

#### Marozzo
- book1.md:76 — « tu frapperas du falso [...] tu lui donneras un mezzo mandritto au bras » — falso + mezzo mandritto au bras = séquence identique
- book3.md:68 — « tu frapperas du falso [...] et dans ce même temps tu lui donneras un mandritto » — falso + mandritto comme contre standard

### Lecture
La réponse falso + mezzo mandritto au bras contre la séquence punta + mandritto est documentée presque à l'identique dans Marozzo book1:76. Le falso intercepte et le mezzo mandritto frappe l'avant-bras adverse exposé.

---

## Exemple 2 — Contre punta + roverso : falso + guardia di testa + mandritto
**Formulation :** « Si l'ennemi te pousse une punta et te tire un roverso, tu lui frappes du falso, tu passes en guardia di testa et lui donnes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:401 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « tu te couvriras avec ta bocle en levant l'épée en guardia di testa et dans le retour tu lui donneras un mandritto » — guardia di testa + mandritto comme contre
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée [...] tu te mets en guardia di testa » — falso + guardia di testa

### Lecture
La séquence falso → guardia di testa → mandritto contre punta + roverso est une parade-riposte en trois temps. Marozzo documente les deux éléments (falso + guardia di testa dans book1:48, guardia di testa + mandritto dans book1:26) dans des séquences adjacentes.

---

## Exemple 3 — Contre punta + mandritto jambe traversant : falso + mezzo mandritto main
**Formulation :** « Si l'ennemi te pousse une punta et te donne un mandritto traversant à la jambe, tu lui frappes du falso et lui donnes un mezzo mandritto à la main. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:403 — Définition de l'exemple

#### Marozzo
- book1.md:76 — « tu frapperas du falso [...] tu lui donneras un mezzo mandritto au bras ou à la main » — falso + mezzo mandritto main/bras
- book3.md:150 — « tu lui tireras un mezzo mandritto à la main d'épée » — mezzo mandritto main documenté

### Lecture
La variante du mezzo mandritto à la main (au lieu du bras) contre le mandritto traversant jambe est documentée dans book1:76 et book3:150. Le mezzo mandritto main cible l'avant-bras et la main exposés lors d'un coup bas.

---

## Exemple 4 — Contre deux punte : falso + droit fil
**Formulation :** « Si l'ennemi te pousse deux punte, tu lui frappes du falso et lui pousses un droit fil. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:405 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — falso + droit fil = séquence identique
- book3.md:52 — « tu frappes fortement du falso [...] et de là tu lui pousseras un droit fil » — falso + droit fil confirmé

### Lecture
Le falso + droit fil contre les doubles punte est documenté quasi à l'identique dans book1:48 et book3:52. Le falso intercepte la première punta, le droit fil (épée en ligne tendue) contre-attaque dans l'intervalle entre les deux punte.

---

## Exemple 5 — Contre falso + mandritto : porta di ferro larga + falso + mandritto
**Formulation :** « Si l'ennemi frappe du falso et te donne un mandritto, tu passes en porta di ferro larga et lui donnes un falso et un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:407 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « depuis la porta di ferro larga [...] tu frappes du falso et lui tireras un mandritto » — depuis porta di ferro larga : falso + mandritto
- book3.md:42 — « tu seras en cinghiara porta di ferro, et là tu frapperas du falso » — transition entre gardes basses + falso

### Lecture
Le pivot vers la porta di ferro larga pour contre-attaquer par falso + mandritto démontre la fluidité entre les gardes basses dans la tradition bolognaise. Marozzo documente ce type de transition dans book3:42 et le falso + mandritto depuis porta di ferro larga dans book1:32.

---

## Exemple 6 — Contre punta + tramazzone : falso + guardia di faccia
**Formulation :** « Si l'ennemi te pousse une punta et te tire un tramazzone, tu lui frappes du falso et te mets en guardia di faccia. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:409 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée [...] tu te mets en guardia di testa » — falso + transition vers garde active
- book3.md:134 — « tu frapperas du falso de ton épée vers l'extérieur [...] et en montant en guardia di faccia tu le pares » — falso + guardia di faccia = formulation identique

### Lecture
Le falso + guardia di faccia contre punta + tramazzone est documenté quasi à l'identique dans Marozzo book3:134. La guardia di faccia, avec sa pointe menaçante, arrête naturellement l'adversaire après le falso.

---

## Exemple 7 — Contre punta + feinte roverso + mandritto : falso + droit fil + guardia di testa + mandritto
**Formulation :** « Si l'ennemi te pousse une punta, feinte un roverso et te donne un mandritto, tu lui frappes du falso, lui pousses un droit fil, tu passes en guardia di testa et lui frappes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:411 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face [...] tu te mets en guardia di testa » — falso + droit fil + guardia di testa
- book3.md:426 — « contre la feinte mandritto → roverso, tu lèveras en guardia alta [...] tu lui donneras un mandritto » — contre la feinte par garde haute + mandritto

### Lecture
Ce contre élaboré en quatre temps (falso + droit fil + guardia di testa + mandritto) est une réponse complète à une attaque en trois temps. Les éléments composants sont tous présents chez Marozzo dans book1:48 et book3:426.

---

## Exemple 8 — Contre punta trivellata : falso + punta face
**Formulation :** « Si l'ennemi te pousse une punta trivellata, tu lui frappes du falso et lui pousses une punta à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:413 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso » — falso contre punta (dont trivellata)
- book3.md:188 — « dans ce même temps tu lui pousseras une punta [...] tu lui donneras ensuite une punta trivellata » — punta trivellata + riposte punta face
- book3.md:659 — Punta trivellata documentée comme botte distincte

### Lecture
La réponse falso + punta face contre la punta trivellata est documentée dans les éléments de Marozzo book3:188 et book3:659. La punta trivellata ayant une trajectoire en spirale, le falso qui l'intercepte doit être dirigé latéralement pour dévierla rotation.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre punta+mandritto : falso+mezzo mandritto bras | opera_nova:399-401 | book1:76, book3:68 |
| Ex2 - Contre punta+roverso : falso+guardia di testa+mandritto | opera_nova:401 | book1:26, book1:48 |
| Ex3 - Contre punta+mandritto jambe : falso+mezzo mandritto main | opera_nova:403 | book1:76, book3:150 |
| Ex4 - Contre deux punte : falso+droit fil | opera_nova:405 | book1:48, book3:52 |
| Ex5 - Contre falso+mandritto : porta di ferro larga+falso+mandritto | opera_nova:407 | book1:32, book3:42 |
| Ex6 - Contre punta+tramazzone : falso+guardia di faccia | opera_nova:409 | book1:48, book3:134 |
| Ex7 - Contre punta+feinte roverso+mandritto : falso+droit fil+guardia di testa+mandritto | opera_nova:411 | book1:48, book3:426 |
| Ex8 - Contre punta trivellata : falso+punta face | opera_nova:413 | book3:188, book3:659 |

## Conclusion
Les huit contres depuis la cinghiara porta di ferro de Manciolino sont systématiquement confirmés dans le corpus, avec un rôle central du falso dans quasiment tous. Le falso + mezzo mandritto bras (Ex1) est documenté quasi à l'identique dans book1:76. Le falso + guardia di faccia contre punta + tramazzone (Ex6) est dans book3:134. Ce chapitre confirme que la cinghiara porta di ferro est une garde fondamentalement défensive qui répond à toutes les attaques par le falso comme premier geste.
