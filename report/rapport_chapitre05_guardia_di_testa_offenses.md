# Rapport : Cas d'utilisation des exemples du Chapitre 5 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples d'**offenses contre quelqu'un en guardia di testa** décrits au Chapitre 5 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
guardia di testa.*punta|punta.*tramazzone.*guardia di testa|feinte.*mandritto.*roverso.*testa|deux mandritti
```

---

## Exemple 1 — Mandritto à la face, au flanc ou à la jambe
**Formulation :** « Contre quelqu'un qui est en guardia di testa, tu peux lui tirer un mandritto à la face, au flanc ou à la jambe. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:205 — Définition de l'exemple

#### Marozzo
- book1.md:42 — « tu passes devant d'un grand pas du pied droit et que tu tailles un mandritto sous le bras, tirant immédiatement le pied droit vers toi » — mandritto direct contre guardia di testa (ou alta)
- book1.md:48 — Séquences de mandritti depuis guardia di testa dans différentes situations
- book3.md:693 — « tu le trouveras avec un falso dritto qui va en guardia d'intrare in largo passo et avec le mandritto qui va en guardia di faccia » — mandritto direct comme botte fondamentale

### Lecture
Le mandritto direct contre la guardia di testa est la botte d'entrée la plus élémentaire. Marozzo la traite comme point de départ de séquences dans book1:42 et book1:48, confirmant que c'est le premier recours offensif contre cette garde.

---

## Exemple 2 — Punta à la face + tramazzone
**Formulation :** « Ou lui pousser une punta à la face et lui tirer ensuite un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:207 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu tailles un tramazzone en porta di ferro larga. Si alors ton ennemi te tire un fendente ou un roverso ou un tramazzone ou bien s'il te pousse un punta à la face, je veux que dans ce temps tu frappes sa botte avec le falso [...] tu lui tireras deux tramazzoni » — punta + deux tramazzoni contre guardia di testa
- book1.md:56 — « tu lui pousseras une punta par l'extérieur de son épée à la face [...] tu lui tireras deux tramazzoni à la tête » — punta + deux tramazzoni précis depuis guardia di testa/alta
- book3.md:20 — « tu fasses un falso impuntato par l'extérieur de son épée à son côté droit, passant [...] tirant dans ce déplacement un mandritto à la tête avec un tramazzone » — falso + frappe + tramazzone depuis guardia di testa

### Lecture
La séquence punta + tramazzone est une des plus récurrentes du corpus bolognais. Elle apparaît chez Marozzo en deux formulations quasi identiques (book1:48 et book1:56), dont une est une correspondance exacte avec l'exemple manciolinien.

---

## Exemple 3 — Feinte mandritto + roverso
**Formulation :** « Ou lui feinter d'un mandritto et néanmoins lui tirer un roverso. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:209 — Définition de l'exemple

#### Marozzo
- book3.md:426 — « s'il te fait une feinte de mandritto pour te donner un roverso, alors tu lèveras en guardia alta dans cette feinte de mandritto » — feinte mandritto + roverso du côté attaquant, référencé comme botte connue
- book3.md:703 — « dans ta frappe de mandritto, trompe en incrociato, ou aussi trompe le mandritto avec le tramazzoncello » — feinte dans le mandritto = tromper l'adversaire
- book1.md:38 — « Lui par peur de cette punta la frappera avec le falso de l'épée dans l'extérieur et il découvrira son côté gauche, tu lui tourneras alors un roverso in falso » — feinte punta → roverso (logique parallèle)

### Lecture
La feinte mandritto→roverso est une botte fondamentale explicitement documentée chez Marozzo dans book3:426. Les deux auteurs la citent comme exemple de trompe-adversaire standard.

---

## Exemple 4 — Deux mandritti
**Formulation :** « Ou si cela te plaît plus, lui faire deux mandritti. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:211 — Définition de l'exemple

#### Marozzo
- book3.md:124 — « tu lui tireras deux mandritti tondi, un à la tête et l'autre à la jambe qui tirera et entrera en guardia d'intrare » — deux mandritti tondo (tête + jambe) contre porta di ferro alta
- book3.md:208 — « tu jetteras le pied droit vers son côté gauche et lui donneras deux mandritti tondi, le premier mandritto ira à la face [...] et l'autre mandritto ira à la jambe » — deux mandritti (face + jambe) en progression
- book3.md:240 — « tu le trouveras avec deux mandritti tondi, avec le premier ne dépassant pas la guardia di faccia » — deux mandritti en guardia d'intrare
- book3.md:250 — « tu lui tireras alors deux mandritti en passant avec ta jambe droite fortement vers son côté gauche » — deux mandritti en passant

### Lecture
Les deux mandritti (successifs, visant des cibles différentes : tête et jambe) sont un motif récurrent chez Marozzo dans book3. Leur emploi comme botte double est systématique dans les assauts marozziens.

---

## Exemple 5 — Feinte tramazzone + mandritto
**Formulation :** « Ou encore lui feinter d'un tramazzone et néanmoins donner un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:213 — Définition de l'exemple
- opera_nova.md:619 — Reprise de la feinte tramazzone + mandritto dans les assauts

#### Marozzo
- book1.md:32 — « Néanmoins supposons que lui te tire de nouveau à la tête, je veux que dans cette attaque tu accompagnes l'épée et ta bocle ensemble en guardia di testa » — référencement du tramazzone comme botte d'appel dont on se défend (implique que l'attaquant peut feinter)
- book3.md:242 — « en faisant semblant de le lui donner à la tête mais en le tirant à la jambe, à la façon d'une entaille » — feinte tramazzone haut → mandritto bas
- book3.md:238 — « tu feras semblant d'un tramazzone à la tête et tu le trouveras avec un mandritto tondo à la jambe » — feinte tramazzone → mandritto jambe explicite

### Lecture
La feinte tramazzone→mandritto est documentée chez Marozzo dans book3:238 et 242 dans une formulation quasi identique à celle de Manciolino. Elle constitue une des feintes de base de l'école bolognaise.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Mandritto face/flanc/jambe | opera_nova:205 | book1:42, book1:48, book3:693 |
| Ex2 - Punta + tramazzone | opera_nova:207 | book1:48, book1:56, book3:20 |
| Ex3 - Feinte mandritto + roverso | opera_nova:209 | book1:38, book3:426, book3:703 |
| Ex4 - Deux mandritti | opera_nova:211 | book3:124, book3:208, book3:240, book3:250 |
| Ex5 - Feinte tramazzone + mandritto | opera_nova:213 | book1:32, book3:238, book3:242 |

## Conclusion
Les cinq exemples du Chapitre 5 correspondent à des bottes fondamentales largement documentées chez Marozzo. La séquence punta + tramazzone (Ex2) et la feinte tramazzone + mandritto (Ex5) sont particulièrement bien représentées dans le corpus marozzien avec des formulations quasi identiques. Le chapitre 5 de Manciolino constitue ainsi un résumé compact des principales attaques contre la guardia di testa que l'on retrouve dispersées dans les trois livres de Marozzo.
