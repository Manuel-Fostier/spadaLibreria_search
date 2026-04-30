# Rapport : Cas d'utilisation des exemples du Chapitre 7 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples d'**offenses contre quelqu'un en guardia di faccia** décrits au Chapitre 7 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Punta en face
**Formulation :** « Contre quelqu'un qui est en guardia di faccia, tu peux lui pousser une punta à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:231 — Définition de l'exemple

#### Marozzo
- book3.md:198 — « tu feras qu'il sera nécessaire que tu la fasses par l'extérieur à son côté droit, c'est-à-dire par-dessus son épée à falso contre falso. Et comme tu auras chassé bien fortement la pointe de ton épée vers son côté gauche, tu lui donneras une entaille dans la face » — punta par l'extérieur dans guardia di faccia ou similaire
- book3.md:232 — « quand il poussera cette punta, du pied droit ou du pied gauche, par l'extérieur à ton côté droit, tu camoufleras ton épée par-dessous la sienne et tu la lui mettras par le côté intérieur » — punta contre guardia similaire documentée comme offensive ET défensive
- book2.md:86 — Séquences de puntas en guardia di faccia comme contre-attaques

### Lecture
La punta directe contre la guardia di faccia est la botte d'entrée la plus naturelle contre cette garde. Marozzo la documente du point de vue défensif (comment la parer) ce qui confirme qu'elle est bien attendue comme attaque principale contre cette garde.

---

## Exemple 2 — Mandritto puissant
**Formulation :** « Ou lui tirer un mandritto puissant. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:233 — Définition de l'exemple

#### Marozzo
- book3.md:420 — « si lui tire un mandritto tondo ou fendente ou redeppio, tu peux lever en guardia alta dans le temps de sa frappe, et dans sa frappe de mandritto [...] tu lui donneras un mandritto à sa tempe gauche » — mandritto puissant référencé du côté patient (il faut lever en guardia alta pour le contrer)
- book2.md:86 — « à chacun de ces mandritti tu jetteras le pied droit un peu vers son côté droit et dans ce pas tu pareras son coup en guardia di faccia » — mandritto contre guardia di faccia = coup standard

### Lecture
Le mandritto direct contre la guardia di faccia est une botte de force. Marozzo la documente toujours du côté du contre (book3:420) ce qui confirme que c'est une attaque attendue : sa puissance réclame une esquive ou une monte en guardia alta.

---

## Exemple 3 — Tramazzone
**Formulation :** « Ou lui tirer un tramazzone. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:235 — Définition de l'exemple

#### Marozzo
- book1.md:32 — Le tramazzone est la botte depuis guardia alta contre toute garde basse, utilisé systématiquement
- book3.md:134 — « tu frapperas du falso de ton épée vers l'extérieur [...] puis tu lui tailleras un mandritto sgualembrato à la face accompagné d'un tramazzone » — tramazzone comme coup final après falso contre garde basse
- book3.md:174 — « tu te couvriras en tirant un tramazzone en fuyant de ta jambe gauche » — tramazzone utilisé en attaque depuis garde quelconque

### Lecture
Le tramazzone est un coup universel contre toute garde dans la tradition bolognaise. Contre la guardia di faccia spécifiquement, il exploite l'angle de dessus de la pointe adverse. Marozzo l'intègre systématiquement comme coup de finition.

---

## Exemple 4 — Falso dans l'épée de l'ennemi + frappe en face
**Formulation :** « Ou bien frapper avec le falso de ton épée dans celle de ton ennemi en tirant à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:237 — Définition de l'exemple

#### Marozzo
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi [...] tu frapperas du falso de ton épée dans la botte qu'il te tire, puis tu lui tailleras un mandritto sgualembrato à la face » — falso dans épée adverse + frappe face en deux temps
- book3.md:188 — « tu lui frappes un falso fortement dans son épée en plaçant dans cette frappe ta jambe gauche derrière la droite. Sans t'arrêter tu lui tireras un mandritto tondo » — falso dans épée + mandritto tondo immédiat
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — falso défensif + suite à la face

### Lecture
Le coup de falso dans l'épée adverse pour l'écarter puis frapper en face est documenté chez Marozzo dans book3:52 et book3:188 de façon quasi identique à Manciolino. C'est un coup d'engagement qui contrôle l'arme adverse tout en frappant.

---

## Exemple 5 — Feinte roverso de bas en haut + mandritto
**Formulation :** « Ou bien feinter d'un roverso de bas en haut et néanmoins lui donner un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:239 — Définition de l'exemple

#### Marozzo
- book1.md:38 — « tu lui tourneras alors un roverso in falso à sa tempe gauche. Si lui veut couvrir ce côté ci-dessus, tu lui tourneras un roverso à sa cuisse droite » — feinte roverso + variation selon réaction adverse
- book3.md:424 — « dans l'aller de sa frappe, tu lèveras en guardia alta, et dans sa frappe de mandritto, tu te chasseras dessous et tu consentiras et lui tireras le roverso redoppio » — feinte → roverso inversé
- book3.md:663 — « tu lèveras en guardia alta en fuyant de la jambe droite et retourneras avec celle-ci et avec le trivillato » — feinte + coup de bas en haut

### Lecture
La feinte roverso montant (de bas en haut) suivie d'un mandritto est une inversion de ligne classique. Chez Marozzo, elle est documentée comme variation de la feinte standard dans plusieurs contextes. Le roverso de bas en haut est identifié comme un roverso redoppio ou trivellato selon les auteurs.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Punta en face | opera_nova:231 | book2:86, book3:198, book3:232 |
| Ex2 - Mandritto puissant | opera_nova:233 | book2:86, book3:420 |
| Ex3 - Tramazzone | opera_nova:235 | book1:32, book3:134, book3:174 |
| Ex4 - Falso dans épée + frappe face | opera_nova:237 | book3:52, book3:188, book1:48 |
| Ex5 - Feinte roverso montant + mandritto | opera_nova:239 | book1:38, book3:424, book3:663 |

## Conclusion
Les cinq exemples d'offenses contre la guardia di faccia de Manciolino correspondent tous à des bottes documentées chez Marozzo. Le falso dans l'épée (Ex4) est particulièrement bien représenté dans book3. La guardia di faccia, par sa position de pointe tendue, appelle naturellement des attaques par déviation (falso) ou par feinte, confirmant la cohérence entre les deux auteurs sur la tactique contre cette garde.
