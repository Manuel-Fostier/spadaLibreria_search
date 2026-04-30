# Rapport : Cas d'utilisation des exemples du Chapitre 16 (Manciolino)
## Objet
Ce rapport analyse les huit exemples de **contres depuis la porta di ferro larga** décrits au Chapitre 16 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

**Corpus exploré :**
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
porta di ferro larga.*falso|falso.*roverso.*porta di ferro larga|punta trivellata|deux punte
```

---

## Exemple 1 — Contre falso + roverso : même falso + mandritto tempe gauche
**Formulation :** « Si l'ennemi frappe du falso et te donne un roverso, tu frappes de ton même falso et lui donnes un mandritto à la tempe gauche. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:363 — Définition de l'exemple

#### Marozzo
- book1.md:32 — « tu frappes du falso contre son falso [...] tu lui tireras un mandritto » — contre-falso + mandritto
- book3.md:52 — « tu frappes fortement vers ton côté droit du falso de ton épée dans celle de l'ennemi » — falso contre falso adverse

### Lecture
Répondre à un falso + roverso par un contre-falso + mandritto est un contre-en-temps sur la même ligne. Marozzo documente le principe du contre-falso dans book1:32 et book3:52 dans des contextes d'engagement des lames.

---

## Exemple 2 — Contre falso + mandritto : feinte falso + punta face + roverso tête
**Formulation :** « Si l'ennemi frappe du falso et te donne un mandritto, tu feintes du falso et lui pousses une punta à la face, et lui tires un roverso à la tête. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:365 — Définition de l'exemple

#### Marozzo
- book3.md:188 — « tu lui frappes un falso fortement dans son épée [...] tu lui tireras un mandritto tondo [...] tu lui tireras un roverso sgualembrato » — feinte falso + mandritto + roverso séquence
- book2.md:86 — « tu lui donneras une punta à la face [...] puis tu lui tireras un roverso sgualembrato à la tête » — punta face + roverso tête

### Lecture
La feinte falso → punta face → roverso tête est une séquence en trois temps qui exploite la réaction adverse à la feinte. Marozzo documente les éléments de cette chaîne dans book3:188 et book2:86.

---

## Exemple 3 — Contre deux punte : falso + droit fil + fendente → guardia di faccia + roverso cuisse
**Formulation :** « Si l'ennemi pousse deux punte, tu frappes du falso, puis du droit fil, puis un fendente ; et si l'ennemi repasse en guardia di faccia, tu lui tires un roverso à la cuisse. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:367 — Définition de l'exemple

#### Marozzo
- book3.md:52 — « tu frappes fortement du falso [...] puis tu lui pousseras une punta [...] puis un fendente » — falso + punta + fendente = structure similaire
- book3.md:188 — « tu lui tailleras [...] un roverso sgualembrato [...] tu te mettras en guardia di faccia » — transition vers guardia di faccia + roverso cuisse
- book1.md:56 — « tu lui pousseras une punta [...] tu avançant de ton pied droit [...] tu lui chasseras une autre punta » — contre les doubles punte

### Lecture
Ce contre élaboré en cinq temps documente l'adaptabilité de la porte di ferro larga. Marozzo documente les éléments composants dans plusieurs passages de book3 et book1:56.

---

## Exemple 4 — Contre falso en face : falso
**Formulation :** « Si l'ennemi frappe du falso en face, tu frappes aussi du tien. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:369 — Définition de l'exemple

#### Marozzo
- book3.md:102 — « tu pareras avec un falso de ton épée de bas en haut » — falso contre falso adverse
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée » — contra-falso comme réponse

### Lecture
Le contre-falso direct (répondre au falso par le même falso) est le contre le plus économique. Marozzo documente ce principe dans book3:102 et book1:48 comme parade naturelle.

---

## Exemple 5 — Contre roverso : guardia di testa + mandritto
**Formulation :** « Si l'ennemi te tire un roverso, tu passes en guardia di testa et lui frappes un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:371 — Définition de l'exemple

#### Marozzo
- book1.md:26 — « tu te couvriras avec ta bocle en levant l'épée en guardia di testa et dans le retour tu lui donneras un mandritto » — guardia di testa + mandritto = contre canonique au roverso
- book3.md:240 — « tu te mettras en guardia di testa, et dans cette guardia tu lui frapperas un mandritto » — même contre

### Lecture
La guardia di testa + mandritto contre le roverso est le contre le plus standard de la tradition bolognaise. Marozzo le documente dans book1:26 et book3:240 dans un cadre quasi identique.

---

## Exemple 6 — Contre falso en face ; tramazzoni : guardia di faccia (deux cas)
**Formulation :** « Si l'ennemi frappe du falso en face, tu te mets en guardia di faccia. Si l'ennemi tire des tramazzoni, tu passes aussi en guardia di faccia. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:373 — Définition des deux sous-contres

#### Marozzo
- book3.md:630 — « tu te placeras en guardia di faccia en esquivant son coup » — guardia di faccia comme parade contre plusieurs bottes
- book3.md:134 — « et en montant en guardia di faccia tu le pares » — guardia di faccia contre tramazzone
- book3.md:242 — « tu te mettras en guardia di faccia » — transition en guardia di faccia comme réponse défensive

### Lecture
L'utilisation de la guardia di faccia comme parade universelle contre le falso et les tramazzoni est documentée dans plusieurs passages de Marozzo book3. La pointe tendue de la guardia di faccia menace l'adversaire et arrête naturellement les attaques en ligne.

---

## Exemple 7 — Contre falso vers guardia alta : laisser aller
**Formulation :** « Si l'ennemi frappe du falso en montant vers guardia alta, tu laisses aller. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:375 — Définition de l'exemple

#### Marozzo
- book3.md:262 — « en se levant en guardia alta, il frappe du falso de bas en haut [...] et toi tu laisses aller le pied gauche derrière » — laisser aller / retraite contre le falso montant
- book3.md:420 — « tu peux lever en guardia alta dans le temps de sa frappe » — réponse à la montée en guardia alta

### Lecture
"Laisser aller" (se retirer, ne pas forcer la parade) contre le falso montant vers guardia alta est un principe d'économie : ne pas chercher à contrer mais recréer la mesure. Marozzo documente ce principe dans book3:262 comme alternative à la parade.

---

## Exemple 8 — Contre stoccata ; contre tramazzone : pied gauche + tramazzone bras d'épée
**Formulation :** « Si l'ennemi pousse une stoccata, tu frappes du falso. Si un tramazzone, tu passes avec le pied gauche et lui tires un tramazzone au bras d'épée. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:377 — Définition des deux sous-contres

#### Marozzo
- book1.md:48 — « tu frappes sa botte avec le falso de ton épée » — falso contre stoccata/punta
- book3.md:174 — « tu te couvriras en tirant un tramazzone en fuyant de ta jambe gauche » — tramazzone + fuite jambe gauche
- book3.md:198 — « et là tu lui tailleras un tramazzone à ses bras d'épée » — tramazzone au bras d'épée adverse

### Lecture
Le double contre (falso contre stoccata, tramazzone bras avec pied gauche contre tramazzone) montre la réversibilité des techniques. Marozzo documente le tramazzone au bras d'épée dans book3:198 et le falso contre punta dans book1:48.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Contre falso+roverso : contre-falso+mandritto | opera_nova:363 | book1:32, book3:52 |
| Ex2 - Contre falso+mandritto : feinte falso+punta+roverso | opera_nova:365 | book2:86, book3:188 |
| Ex3 - Contre deux punte : falso+droit fil+fendente ; guardia di faccia+roverso cuisse | opera_nova:367 | book1:56, book3:52, book3:188 |
| Ex4 - Contre falso en face : contre-falso | opera_nova:369 | book1:48, book3:102 |
| Ex5 - Contre roverso : guardia di testa+mandritto | opera_nova:371 | book1:26, book3:240 |
| Ex6 - Contre falso/tramazzoni : guardia di faccia | opera_nova:373 | book3:134, book3:242, book3:630 |
| Ex7 - Contre falso guardia alta : laisser aller | opera_nova:375 | book3:262, book3:420 |
| Ex8 - Contre stoccata : falso ; contre tramazzone : pied gauche+tramazzone bras | opera_nova:377 | book1:48, book3:174, book3:198 |

## Conclusion
Les huit contres depuis la porta di ferro larga de Manciolino forment un système défensif cohérent confirmé par Marozzo. Le contre au roverso par guardia di testa + mandritto (Ex5) est particulièrement bien documenté. La guardia di faccia comme parade universelle contre falso et tramazzoni (Ex6) est confirmée dans trois passages de Marozzo book3. Ce chapitre démontre que la porta di ferro larga est une garde adaptée à la défense contre toute attaque de la ligne haute.
