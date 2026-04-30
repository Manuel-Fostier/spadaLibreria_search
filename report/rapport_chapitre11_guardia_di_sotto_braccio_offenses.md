# Rapport : Cas d'utilisation des exemples du Chapitre 11 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples d'**offenses contre quelqu'un en guardia di sotto braccio** décrits au Chapitre 11 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Roverso à la face
**Formulation :** « Contre quelqu'un en guardia di sotto braccio, tu peux lui tirer un roverso à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:299 — Définition de l'exemple

#### Marozzo
- book1.md:38 — « étant en guardia di sopra braccio, ton ennemi est en sotto braccio [...] je veux que tu avances de ton pied droit devant et que tu pousses une punta [...] tu lui tourneras alors un roverso in falso à sa tempe gauche » — roverso contre sotto braccio documenté explicitement
- book3.md:188 — « depuis guardia di sotto braccio tu tireras un roverso sgualembrato à la face de l'ennemi » — roverso face depuis/contre sotto braccio

### Lecture
Le roverso à la face contre la guardia di sotto braccio est la botte naturelle car la garde basse laisse la tête et la face exposées. Marozzo le confirme explicitement dans book1:38 (contre la sotto braccio) et book3:188.

---

## Exemple 2 — Falso + mandritto face
**Formulation :** « Ou frapper du falso dans son épée et lui tirer un mandritto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:301 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi [...] tu lui tireras un mandritto à la face » — falso dans épée adverse + mandritto face = séquence identique
- book3.md:134 — « tu frapperas du falso de ton épée vers l'extérieur de son épée [...] tu lui tailleras un mandritto sgualembrato à la face » — falso + mandritto face
- book3.md:68 — « tu frapperas du falso de ton épée dans la sienne, et tu lui tireras un roverso à la face ou un mandritto » — falso + mandritto/roverso face

### Lecture
Le couple falso + mandritto face est l'une des séquences les mieux documentées dans tout le corpus. Marozzo book1:32 et book3:134 la formulent quasi à l'identique. C'est une technique fondamentale contre toute garde basse comme la sotto braccio : le falso écarte la lame et ouvre la ligne vers la face.

---

## Exemple 3 — Roverso en fuyant avec le pied gauche derrière
**Formulation :** « Ou lui tirer un roverso en fuyant avec le pied gauche derrière le droit. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:303 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « en fuyant de ta jambe gauche derrière la droite, tu leveras l'épée en guardia alta [...] tu lui donneras un grand mandritto dans la tête » — fuite de la jambe gauche derrière + coup
- book3.md:102 — « fuyant du pied gauche derrière le droit, tu lui tireras un roverso à la tempe droite » — roverso en fuyant pied gauche derrière = formulation quasi identique

### Lecture
Le roverso tiré en reculant le pied gauche derrière le droit est un mouvement rétrograde offensif. Marozzo le documente dans book3:102 avec une formulation quasi identique. Ce mouvement permet de garder ou de maintenir la mesure tout en frappant en arc de cercle.

---

## Exemple 4 — Punta dans la main d'épée
**Formulation :** « Ou lui pousser une punta dans sa main d'épée. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:305 — Définition de l'exemple

#### Marozzo
- book1.md:70 — « tu lui pousseras une punta au poignet de la main d'épée » — punta au poignet de la main d'épée documentée
- book1.md:56 — « tu tireras ton épée par la droite de la sienne en lui poussant ta bocle dans son poing d'épée [...] tu chasseras une autre punta à sa tempe droite » — punta vers le poing d'épée adverse

### Lecture
La punta dans la main d'épée adverse est une attaque sur l'armement plutôt que sur le corps. Contra la sotto braccio, le poing d'épée est bas et exposé. Marozzo confirme cette cible dans book1:70 et book1:56.

---

## Exemple 5 — Falso + punta montante + tramazzone → porta di ferro stretta
**Formulation :** « Ou bien frapper du falso, puis lui pousser une punta en montant et un tramazzone, et te mettre ensuite en porta di ferro stretta. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:307-309 — Définition de l'exemple avec transition vers porta di ferro stretta
- opera_nova.md:317-319 — Référencé dans les contres du chapitre suivant

#### Marozzo
- book3.md:104 — « tu frapperas du falso de ton épée dans la sienne [...] puis tu lui pousseras une punta de bas en haut [...] et puis un tramazzone » — falso + punta montante + tramazzone = séquence identique
- book3.md:120 — « tu feras une cinghiara porta di ferro, et là tu pousses une punta à la cuisse » — porta di ferro stretta/cinghiara comme position de sécurité après rafale

### Lecture
La séquence triple falso + punta montante + tramazzone puis retour en porta di ferro stretta est une démonstration de la logique d'assaut puis de retrait en sécurité. Marozzo documente cette séquence dans book3:104 de façon très proche.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Roverso face | opera_nova:299 | book1:38, book3:188 |
| Ex2 - Falso + mandritto face | opera_nova:301 | book1:32, book3:68, book3:134 |
| Ex3 - Roverso en fuyant pied gauche | opera_nova:303 | book1:32, book3:102 |
| Ex4 - Punta dans la main d'épée | opera_nova:305 | book1:56, book1:70 |
| Ex5 - Falso + punta montante + tramazzone → porta di ferro stretta | opera_nova:307-309 | book3:104, book3:120 |

## Conclusion
Les cinq offenses contre la guardia di sotto braccio de Manciolino sont toutes confirmées dans le corpus. Le falso + mandritto face (Ex2) est la technique la plus universellement documentée, présente dans book1:32 et book3:134 de façon quasi identique. La séquence triple Ex5 se retrouve dans book3:104. La sotto braccio, garde basse qui expose la face et le poignet, appelle naturellement le falso comme botte d'engagement.
