# Rapport : Cas d'utilisation des exemples du Chapitre 8 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples de **contres depuis la guardia di faccia** décrits au Chapitre 8 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
guardia di faccia.*punta|punta.*guardia di faccia|tramazzone.*guardia di faccia|falso.*épée.*face
```

---

## Exemple 1 — Contre la punta : pied gauche vers côté droit + demi-volte du poing + frappe face
**Formulation :** « Si l'ennemi te pousse une punta, tu peux passer avec le pied gauche devant vers son côté droit, en faisant une demi-volte du poing, en frappant à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:243 — Définition de l'exemple

#### Marozzo
- book2.md:86 — « tu jetteras le pied droit un peu vers son côté droit et dans ce pas tu pareras son coup en guardia di faccia [...] tu passeras du pied gauche et tu lui donneras un mandritto avec le poignard et un roverso avec l'épée » — passer vers côté de l'ennemi + contre-attaque sur la punta
- book1.md:56 — « tu tireras ton épée par la droite de la sienne en lui poussant ta bocle dans son poing d'épée [...] tu chasseras une autre punta à sa tempe droite » — passage vers flanc adverse lors de punta

### Lecture
La contre-manœuvre de pied croisé vers le flanc adverse lors d'une punta est un *mezzo tempo* documenté chez Marozzo. En passant vers le côté de la main d'épée adverse, on sort de la ligne de la punta tout en créant une ouverture. La demi-volte du poing (rotation de la main d'épée) accompagne ce déplacement chez les deux auteurs.

---

## Exemple 2 — Contre le mandritto : offrir la pointe pour abaisser l'attaque adverse
**Formulation :** « Si le mandritto arrive haut, tu peux le forcer à abaisser son bras en lui offrant ta pointe. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:245 — Définition de l'exemple

#### Marozzo
- book3.md:218 — « tu chasseras une punta à celui-ci, laquelle ira de bas en haut [...] Puis dans un temps tu lui donneras un mandritto tondo qui ne dépassera pas la guardia di faccia [...] Là s'il t'attend, tu jetteras ta main gauche au milieu de ton épée » — usage de la punta dirigée pour forcer une réaction adverse
- book3.md:635 — « pendant qu'il lèvera (son épée) pour s'en défendre, tu lui frapperas la cuisse avant d'un roverso » — exploiter le mouvement de levée provoqué par la punta

### Lecture
Le principe d'offrir la pointe pour contraindre l'adversaire à modifier son attaque (baisser ou lever) est fondamental dans l'escrime bolognaise. Marozzo l'applique dans book3:218 et book3:635 : la pointe menaçante force une réaction prévisible que l'on exploite.

---

## Exemple 3 — Contre le tramazzone : falso vers côté gauche + droit fil en face
**Formulation :** « Si l'ennemi tire un tramazzone, tu frapperas celui-là de ton falso vers ton côté gauche, puis lui tireras un droit fil à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:247 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face en passant avec ton pied gauche vers son côté droit » — falso défensif + droit fil traversato face = quasi identique
- book1.md:32 — « depuis n'importe laquelle de ces gardes tu pares du droit fil de l'épée [...] là tu pareras sa botte sur le droit fil » — droit fil comme parade primaire contre tramazzone/mandritto

### Lecture
La réponse falso + droit fil face contre le tramazzone est documentée presque à l'identique chez Marozzo dans book1:48. Le falso écarte le tramazzone puis le droit fil (épée en position de punta tendue) frappe en une ligne continue. C'est l'un des contres les plus explicitement partagés entre les deux auteurs.

---

## Exemple 4 — Contre le falso sur l'épée : demi-volte du poing
**Formulation :** « Si l'ennemi fait le falso sur ton épée, tu feras une demi-volte du poing. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:249 — Définition de l'exemple

#### Marozzo
- book3.md:242 — « En retirant ensuite le pied droit derrière, tu feras une demi-volte du poing ramenant l'épée en coda longa e stretta » — demi-volte du poing suite à engagement des épées
- book2.md:52 — « tu tireras un falso dritto de bas en haut à ses mains en fuyant du pied droit en arrière, de sorte que tu feras une demi-volte du poing de chaque main » — demi-volte du poing utilisée comme retraite défensive
- book2.md:240 — « Et là, tu avanceras aussitôt de ton pied droit devant et tu lui donneras un roverso à la jambe. Et pour te couvrir, tu jetteras le pied droit derrière le pied gauche, et dans ce pas tu tireras un autre roverso sgualembrato de gamba levata. » — demi-volte implicite lors de changement de garde

### Lecture
La demi-volte du poing (rotation de la main d'épée de 180° pour changer le tranchant actif) est un mouvement tactique récurrent chez Marozzo, notamment utilisé pour esquiver un engagement adverse sur l'épée. Elle est souvent associée à une retraite du pied.

---

## Exemple 5 — Contre la feinte roverso montant + mandritto : pied droit derrière + punta
**Formulation :** « Si l'ennemi fait une feinte de roverso de bas en haut pour te donner un mandritto, en faisant une demi-volte de la main et en jetant le pied droit derrière le gauche, tu le pareras, et ensuite tu lui pousseras une punta dans la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:251 — Définition de l'exemple

#### Marozzo
- book2.md:86 — « dans ce pas tu pareras son coup en guardia di faccia avec la pointe de ton épée vers la droite de la face de ton ennemi. Et dans un même temps, tu passeras du pied gauche et tu lui donneras un mandritto avec le poignard et un roverso avec l'épée » — parade guardia di faccia + contre en un temps
- book1.md:42 — « je veux que dans cette attaque tu jettes ton pied gauche un peu de travers vers le côté droit de l'ennemi et que tu lui tailles un roverso » — retrait puis contre suite à attaque adverse

### Lecture
La parade de la feinte + mandritto par retraite du pied + contre-punta est une structure de demi-temps : on laisse l'adversaire développer sa feinte (roverso) et on frappe dans le temps du mandritto qui suit. Chez Marozzo, cette logique est présente dans book2:86 et les séquences de book1.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre punta : pied gauche vers côté droit + frappe | opera_nova:243 | book1:56, book2:86 |
| Ex2 - Contre mandritto : offrir pointe pour abaisser | opera_nova:245 | book3:218, book3:635 |
| Ex3 - Contre tramazzone : falso + droit fil face | opera_nova:247 | book1:32, book1:48 |
| Ex4 - Contre falso sur épée : demi-volte du poing | opera_nova:249 | book2:52, book2:240, book3:242 |
| Ex5 - Contre feinte roverso + mandritto : retraite + punta | opera_nova:251 | book1:42, book2:86 |

## Conclusion
Les contres depuis la guardia di faccia de Manciolino trouvent tous des correspondances chez Marozzo. Le contre au tramazzone par falso + droit fil (Ex3) est particulièrement bien documenté dans book1:48. La demi-volte du poing (Ex4) est un geste technique fondamental présent dans plusieurs contexts marozziens. Ce chapitre confirme que la guardia di faccia est une garde réactive par excellence, conçue pour transformer toute attaque adverse en contre-attaque.
