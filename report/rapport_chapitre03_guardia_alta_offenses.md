# Rapport : Cas d'utilisation des exemples du Chapitre 3 (Manciolino)
## Objet
Ce rapport analyse les neuf exemples d'offenses depuis la **guardia alta** décrits au Chapitre 3 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
guardia alta|mandritto.*main d.épée.*par-dessus|roverso.*cuisse.*guardia alta|feinte.*montante
```

---

## Exemple 1 — Mandritto main d'épée par-dessus bras + roverso + montante en guardia alta
**Formulation :** « Tu peux tirer un mandritto à sa main d'épée qui va au-dessus du bras, et bien retourner d'un roverso à cette même main, et ensuite lui monter un montante en haut qui retourne en guardia alta. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:175 — Définition de l'exemple (chapitre source)

#### Marozzo
- book1.md:26 — « tu passes devant d'un grand pas avec le pied droit et tu tailles un mandritto par-dessus le bras [...] tu passes avec ce pied gauche vers le côté droit de l'ennemi, et dans ce pas tu lui donneras un roverso à sa tempe droite » — séquence mandritto par-dessus bras + roverso, très proche
- book1.md:20 — « tu avances avec le pied droit devant et tu tailles un mandritto sgualembrato qui va par-dessus le bras [...] montante dans la bocle, et ton épée ira en guardia alta » — mandritto sgualembrato + montante guardia alta depuis guardia alta

### Lecture
La séquence mandritto au-dessus du bras + roverso + retour en guardia alta est un pattern fondamental présent chez Marozzo (book1:26) presque à l'identique. La variante sgualembrata de Marozzo (book1:20) confirme la généralisation de ce coup d'entrée.

---

## Exemple 2 — Roverso à la cuisse (si attaque tête avec falso traversato)
**Formulation :** « Tu peux aussi lui tirer un roverso à la cuisse. Et si l'ennemi te lance un falso traversato pour te frapper à la tête, tu n'as qu'à te mettre en guardia di testa. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:177 — Définition de l'exemple

#### Marozzo
- book1.md:38 — « Si lui veut couvrir ce côté ci-dessus, tu lui tourneras un roverso à sa cuisse droite sans bouger les pieds ou les jambes. » — roverso à la cuisse comme réponse à une couverture adverse, contexte guardia di sopra braccio mais même logique tactique
- book1.md:56 — « Tu lui tireras alors un roverso à la cuisse en ne bougeant ni des pieds ni des jambes » — roverso cuisse de pied ferme après parade

### Lecture
Le roverso à la cuisse, coup opportuniste bas après avoir menacé le haut, est récurrent chez Marozzo. Ici le contexte est guardia alta chez Manciolino ; Marozzo l'intègre dans d'autres gardes mais avec la même logique : exploiter la couverture adverse.

---

## Exemple 3 — Feinte montante + pied gauche devant + guardia di testa + mandritto
**Formulation :** « Ou encore lui faire une feinte de montante, avancer le pied gauche devant, et dans cette avancée aller en guardia di testa, et pousser un mandritto passant avec le pied droit et retirant ensuite le gauche derrière. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:179 — Définition de l'exemple

#### Marozzo
- book1.md:42 — « tu passes devant d'un grand pas du pied droit et que tu tailles un mandritto sous le bras, tirant immédiatement le pied droit vers toi » depuis guardia di testa — structure similaire (garde haute + mandritto depuis transition)
- book1.md:18 — Passages répétés guardia di testa → falso → montante en guardia alta + transitions de pieds

### Lecture
La feinte de montante pour entrer en guardia di testa puis frapper est une logique de transition garde haute→frappe que Marozzo décrit sous différentes formes. Le principe de changer la menace en cours d'action est commun aux deux auteurs.

---

## Exemple 4 — Feinte roverso cuisse + mandritto par-dessous bras à main d'épée
**Formulation :** « Tu peux feinter de lui tirer un roverso à la cuisse et ensuite lui donner un mandritto par-dessous le bras à sa main d'épée. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:181 — Définition de l'exemple

#### Marozzo
- book1.md:38 — « [depuis sopra braccio] tu pousses une punta à la face de l'ennemi par l'extérieur de son côté droit. Lui par peur de cette punta la frappera avec le falso [...] tu lui tourneras alors un roverso in falso à sa tempe gauche » — feinte haute + frappe basse inversée chez Marozzo
- book3.md:420-426 — Descriptions de feintes mandritto/roverso depuis diverses gardes hautes

### Lecture
La feinte basse (cuisse) suivie de coup haut (main d'épée/sous bras) est l'inverse de la feinte haute+basse de Marozzo. Les deux auteurs exploitent la même logique de rupture de ligne mais dans des directions opposées.

---

## Exemple 5 — Tramazzone tout découvert → guardia di testa + mandritto/roverso + fuite
**Formulation :** « Ou bien tirer un tramazzone tout découvert pour que si l'ennemi veut profiter de cette occasion, tu aies le temps de te mettre en guardia di testa et de lui tirer un mandritto ou roverso et fuir. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:183 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu tailles un tramazzone en cinghiara porta di ferro [...] tu jettes ton pied droit d'un grand pas devant le gauche, et dans ce pas tu pareras la botte de ton ennemi du falso de ton épée. Tu lui donneras alors un roverso ou un mandritto » — tramazzone découvert comme appel + parade + contre identique
- book1.md:48 — « tu tailles un tramazzone en porta di ferro larga. Si alors ton ennemi te tire [...] tu frappes sa botte avec le falso de ton épée et tu le suives d'un droit fil traversato » — tramazzone odkryty → contre

### Lecture
L'usage du tramazzone comme appel (laisser une ouverture intentionnelle) est documenté chez Marozzo de façon quasi identique dans book1:32. C'est une technique de provocation partagée par les deux auteurs.

---

## Exemple 6 — Tramazzone vers côté droit (pied gauche) + feinte roverso + mandritto
**Formulation :** « Tirer le tramazzone vers son côté droit en avançant le pied gauche, faire semblant d'un roverso et puis frapper de mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:185 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « en jetant en un temps le pied droit vers son côté gauche, tu lui donneras un fendente avec un tramazzone dans la tête » — tramazzone en passant vers le flanc adverse
- book3.md:242 — « tu tireras un tramazzoncello [...] tu te couvriras en lui tirant un falso de bas en haut [...] Puis tu tireras un mandritto » — enchaînement tramazzone + feinte + mandritto

### Lecture
La séquence tramazzone lateral + feinte + mandritto est présente chez Marozzo sous forme de variantes dans plusieurs assauts. Le principe du tramazzone comme préparation de frappe est universel dans les deux traités.

---

## Exemple 7 — Feinte tramazzone + mandritto
**Formulation :** « Faire semblant d'un tramazzone et néanmoins donner un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:187 — Définition de l'exemple
- opera_nova.md:619 — « tu feras semblant de tourner un autre tramazzone et cependant tu lui frapperas la jambe avant d'un mandritto » — reprise exacte dans les assauts

#### Marozzo
- book3.md:242 — « en faisant semblant de le lui donner à la tête mais en le tirant à la jambe, à la façon d'une entaille » — feinte tramazzone tête → mandritto jambe
- book1.md:32 — Feinte tramazzone référencée comme contre dans plusieurs contextes

### Lecture
La feinte tramazzone + mandritto est une des feintes les plus documentées de la tradition. Manciolino la mentionne brièvement ; Marozzo y revient dans plusieurs contextes avec la même mécanique.

---

## Exemple 8 — Punta par-dessus main + un ou deux tramazzoni
**Formulation :** « Pousser une punta par-dessus la main et lui tirer ensuite un ou deux tramazzoni. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:189 — Définition de l'exemple
- opera_nova.md:619, 621, 633, 635 — Séquences punta + tramazzoni répétées dans les assauts

#### Marozzo
- book1.md:20 — « pousses une punta sous ta bocle qui va au visage de ton ennemi, accompagnant cette punta ferme de deux tramazzoni » — punta + deux tramazzoni exactement
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et tu le suives d'un droit fil traversato à sa face [...] tu lui tireras deux tramazzoni » — séquence similaire
- book1.md:56 — « tu lui tireras deux tramazzoni à la tête, ton épée tombera en porta di ferro stretta » — punta + deux tramazzoni

### Lecture
La séquence punta + tramazzoni est l'une des plus récurrentes de tout le corpus. Elle apparaît chez Marozzo dans au moins trois contextes distincts (book1:20, 48, 56) avec une formulation quasi identique à celle de Manciolino.

---

## Exemple 9 — Fendente + tramazzone
**Formulation :** « Lui tirer un fendente suivi d'un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:191 — Définition de l'exemple
- opera_nova.md:633 — « un fendente par-dessus la tête accompagné de deux tramazzoni »

#### Marozzo
- book1.md:26 — « en jetant en un temps le pied droit vers son côté gauche, tu lui donneras un fendente avec un tramazzone dans la tête »
- book3.md:20 — « tirant dans ce déplacement un mandritto à la tête avec un tramazzone de sorte que ton épée tombera en porta di ferro larga »

### Lecture
La combinaison fendente + tramazzone apparaît littéralement chez Marozzo (book1:26). Il s'agit d'une séquence de coups en cascade courante dans la tradition bolognaise.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Mandritto par-dessus bras + roverso + montante | opera_nova:175 | book1:20, book1:26 |
| Ex2 - Roverso à la cuisse | opera_nova:177 | book1:38, book1:56 |
| Ex3 - Feinte montante + guardia di testa + mandritto | opera_nova:179 | book1:18, book1:42 |
| Ex4 - Feinte roverso cuisse + mandritto sous bras | opera_nova:181 | book1:38, book3:420 |
| Ex5 - Tramazzone découvert + contre guardia di testa | opera_nova:183 | book1:32, book1:48 |
| Ex6 - Tramazzone vers côté droit + feinte roverso + mandritto | opera_nova:185 | book1:26, book3:242 |
| Ex7 - Feinte tramazzone + mandritto | opera_nova:187 | book1:32, book3:242 |
| Ex8 - Punta + tramazzoni | opera_nova:189 | book1:20, book1:48, book1:56 |
| Ex9 - Fendente + tramazzone | opera_nova:191 | book1:26, book3:20 |

## Conclusion
Les offenses depuis la guardia alta décrites par Manciolino trouvent des correspondances directes chez Marozzo, principalement dans le Book 1. La séquence punta + tramazzoni (Ex8) est la plus universelle du corpus. La guardia alta est manifestement une position d'attaque fondamentale partagée par toute l'école bolognaise.
