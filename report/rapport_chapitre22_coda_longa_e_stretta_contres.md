# Rapport : Cas d'utilisation des exemples du Chapitre 22 (Manciolino)
## Objet
Ce rapport analyse les quatre exemples de **contres depuis la coda longa e stretta** décrits au Chapitre 22 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Contre punta + mandritto : falso + mezzo mandritto main
**Formulation :** « Si l'ennemi te pousse une punta et te donne un mandritto, tu lui frappes du falso et lui donnes un mezzo mandritto à la main. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:459 — Définition de l'exemple

#### Marozzo
- book2.md:212 — « si l'ennemi te pousse une punta et te donne un mandritto depuis la coda longa e stretta, tu lui frapperas du falso et lui donneras un mezzo mandritto à la main » — falso + mezzo mandritto main = formulation identique dans le contexte de la même garde
- book1.md:76 — « tu frapperas du falso [...] tu lui donneras un mezzo mandritto au bras ou à la main » — falso + mezzo mandritto main/bras

### Lecture
Ce contre est documenté quasi à l'identique dans Marozzo book2:212 dans le contexte de la coda longa e stretta. Le mezzo mandritto à la main (raccourci par rapport au mandritto plein) est le coup de riposte rapide après l'interception par le falso.

---

## Exemple 2 — Contre punta + tramazzone : droit fil + guardia di faccia
**Formulation :** « Si l'ennemi te pousse une punta et te tire un tramazzone, tu lui pousses un droit fil et te mets en guardia di faccia. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:461 — Définition de l'exemple

#### Marozzo
- book2.md:212 — « si l'ennemi te pousse une punta puis un tramazzone [...] tu lui pousseras un droit fil et te mettras en guardia di faccia » — droit fil + guardia di faccia = formulation identique dans le contexte de la coda longa e stretta
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée et que tu le suives d'un droit fil traversato à sa face » — droit fil comme riposte

### Lecture
Ce contre est documenté quasi à l'identique dans Marozzo book2:212. Le droit fil contre la punta, puis la guardia di faccia pour arrêter le tramazzone en présentant la pointe, forment une réponse systématique en deux temps.

---

## Exemple 3 — Contre punta + feinte mandritto + roverso : droit fil + guardia di faccia + demi-volte + mandritto
**Formulation :** « Si l'ennemi te pousse une punta, feinte un mandritto et te donne un roverso, tu lui pousses un droit fil, tu te mets en guardia di faccia, tu fais une demi-volte et lui donnes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:463 — Définition de l'exemple

#### Marozzo
- book2.md:216 — « si l'ennemi te pousse une punta, feinte un mandritto et te donne un roverso, tu lui pousseras un droit fil [...] tu te mettras en guardia di faccia, et dans la demi-volte tu lui frapperas un mandritto » — droit fil + guardia di faccia + demi-volte + mandritto = formulation identique
- book3.md:242 — « tu feras une demi-volte du poing ramenant l'épée [...] et tu lui frapperas un mandritto » — demi-volte + mandritto documenté

### Lecture
Ce contre est documenté quasi à l'identique dans Marozzo book2:216. C'est le contre le plus élaboré du chapitre : quatre temps contre trois temps adverses. La demi-volte du poing (rotation de la main d'épée) lors de la guardia di faccia permet de recadrer le mandritto final.

---

## Exemple 4 — Contre punta + fendente : mezzo mandritto + guardia di testa + mandritto
**Formulation :** « Si l'ennemi te pousse une punta et te tire un fendente, tu lui donnes un mezzo mandritto, tu passes en guardia di testa et lui frappes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:465 — Définition de l'exemple

#### Marozzo
- book2.md:212 — « contre la punta + fendente : mezzo mandritto [...] guardia di testa [...] mandritto » — mezzo mandritto + guardia di testa + mandritto = formulation identique dans le contexte de la coda longa e stretta
- book1.md:26 — « tu te couvriras avec ta bocle en levant l'épée en guardia di testa et dans le retour tu lui donneras un mandritto » — guardia di testa + mandritto comme contre au fendente

### Lecture
Ce contre est documenté quasi à l'identique dans Marozzo book2:212. Le mezzo mandritto intercepte la punta, la guardia di testa couvre le fendente descendant, le mandritto final riposte. C'est la même logique que le chapitre 20 Ex5 (contre le fendente par guardia di testa) appliquée à la coda longa e stretta.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre punta+mandritto : falso+mezzo mandritto main | opera_nova:459 | book1:76, book2:212 |
| Ex2 - Contre punta+tramazzone : droit fil+guardia di faccia | opera_nova:461 | book1:48, book2:212 |
| Ex3 - Contre punta+feinte mandritto+roverso : droit fil+guardia di faccia+demi-volte+mandritto | opera_nova:463 | book2:216, book3:242 |
| Ex4 - Contre punta+fendente : mezzo mandritto+guardia di testa+mandritto | opera_nova:465 | book1:26, book2:212 |

## Conclusion
Les quatre contres depuis la coda longa e stretta de Manciolino sont tous confirmés dans le corpus, avec une correspondance remarquable dans Marozzo book2:212 qui documente trois des quatre contres quasi à l'identique. Ce chapitre est, avec le chapitre 21, celui qui présente la correspondance la plus directe entre les deux auteurs. La coda longa e stretta, garde basse à droite avec pied droit devant, génère un système offense/défense cohérent entièrement partagé entre Manciolino et Marozzo, témoignant de leur appartenance commune à l'école bolognaise.

---

## Note conclusive sur l'ensemble des chapitres 3-22

L'analyse systématique des 20 chapitres de Manciolino (Ch3-Ch22) révèle plusieurs constantes :

1. **Techniques universelles** : Le falso + mandritto face, la guardia di testa + mandritto, et la guardia di faccia comme parade sont présents dans pratiquement tous les chapitres chez Marozzo.

2. **Correspondances directes** : Les chapitres 21-22 (coda longa e stretta) présentent la correspondance la plus directe, avec Marozzo book2:212 documentant quasi à l'identique plusieurs séquences.

3. **Cohérence de l'école bolognaise** : Manciolino (Opera Nova, ~1531) et Marozzo (Opera Nova de l'arte de l'armi, ~1536) enseignent le même système pour l'épée et la bocle, avec les mêmes gardes, les mêmes séquences et les mêmes principes tactiques.
