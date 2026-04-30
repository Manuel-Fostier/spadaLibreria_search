# Rapport : Cas d'utilisation des exemples du Chapitre 13 (Manciolino) dans toute la collection

## Objet

Ce rapport recense les cas d'utilisation, dans toute la collection, des cinq exemples donnes dans :

**Chapitre 13 : Des offenses qui peuvent se faire contre la garde de porta di ferro stretta**

Source principale : `treatises/manciolino/opera_nova.md`.

Corpus explore :
- `treatises/manciolino/opera_nova.md`
- `treatises/marozzo/book1.md`
- `treatises/marozzo/book2.md`
- `treatises/marozzo/book3.md`

**Expressions régulières utilisées (`grep_search`) :**
```
porta di ferro stretta|tramazzone|cinghiara porta di ferro|falso.*mandritto
```

---

## Exemple 1 - Tramazzone simple

Formulation du chapitre 13 :
- "Tu peux tourner un tramazzone."

### Occurrences pertinentes relevees

### Manciolino
- `treatises/manciolino/opera_nova.md:307` : variante avec entree par falso + punta, puis tramazzone tombant en porta di ferro stretta.
- `treatises/manciolino/opera_nova.md:323` : formulation de reference (chapitre 13).
- `treatises/manciolino/opera_nova.md:355` : autre proposition : lever un falso jusqu'en guardia di faccia puis tourner un tramazzone.
- `treatises/manciolino/opera_nova.md:451` : reprise apres punta, puis tramazzone.

### Marozzo
- `treatises/marozzo/book3.md:92` : attaque par tramazzone contre adversaire en porta di ferro stretta/alta.
- `treatises/marozzo/book3.md:120` : falso puis tramazzone, avec chute en cinghiara porta di ferro stretta.
- `treatises/marozzo/book3.md:132` : mandritto traversato avec tramazzone, puis retour en cinghiara porta di ferro stretta.

### Lecture
Le tramazzone comme action offensive directe contre une garde basse est un schema fondamental et transversal chez les deux auteurs.

---

## Exemple 2 - Punta a la face + deux tramazzoni

Formulation du chapitre 13 :
- "... pied gauche devant en poussant une punta a la face, puis pied droit devant en tournant deux tramazzoni."

### Occurrences pertinentes relevees

### Manciolino
- `treatises/manciolino/opera_nova.md:325` : formulation de reference (chapitre 13).
- `treatises/manciolino/opera_nova.md:547` : punta a la face puis tramazzone a la tete, chute en porta di ferro stretta.
- `treatises/manciolino/opera_nova.md:619` : punta a la face puis deux tramazzoni.
- `treatises/manciolino/opera_nova.md:637` : punta a la face puis deux tramazzoni a la tete, dernier en porta di ferro stretta.

### Marozzo
- `treatises/marozzo/book1.md:20` : punta au visage accompagnee de deux tramazzoni, chute en porta di ferro stretta.
- `treatises/marozzo/book1.md:48` : reponse a une attaque puis deux tramazzoni en contre-pas, chute en porta di ferro stretta.
- `treatises/marozzo/book1.md:56` : punta puis enchainement de deux tramazzoni a la tete.

### Lecture
C'est la combinaison la plus stable de la collection : la pointe force la reaction, les tramazzoni exploitent l'ouverture.

---

## Exemple 3 - Feinte de tramazzone -> roverso a la cuisse

Formulation du chapitre 13 :
- "Faire semblant de tirer un tramazzone et toutefois lui donner un roverso a la cuisse."

### Occurrences pertinentes relevees

### Manciolino
- `treatises/manciolino/opera_nova.md:327` : formulation de reference (chapitre 13).
- `treatises/manciolino/opera_nova.md:339` : contre explicite de cette action (chapitre 14).
- `treatises/manciolino/opera_nova.md:633` : en assaut, feinte de tramazzone suivie du roverso a la cuisse.

### Marozzo
- `treatises/marozzo/book3.md:112` : feinte de tramazzone a la tete, puis chute en roverso a la jambe.
- `treatises/marozzo/book3.md:238` : schema equivalent de feinte haute -> frappe basse.

### Lecture
La logique feinte haute / attaque basse est commune aux deux traditions textuelles du corpus.

---

## Exemple 4 - Punta + feinte de roverso -> mandritto

Formulation du chapitre 13 :
- "Pousser une punta a la face, faire semblant d'un roverso a la tete, puis donner un mandritto (tete ou jambe)."

### Occurrences pertinentes relevees

### Manciolino
- `treatises/manciolino/opera_nova.md:329` : formulation de reference (chapitre 13).
- `treatises/manciolino/opera_nova.md:341` : contre detaille (chapitre 14) : lecture de la feinte de roverso puis opposition au mandritto.
- `treatises/manciolino/opera_nova.md:393` : reprise formulee presque a l'identique.
- `treatises/manciolino/opera_nova.md:935` : meme structure depuis coda longa e alta.
- `treatises/manciolino/opera_nova.md:1109` : variante en sequence longue (rondache).

### Marozzo
- `treatises/marozzo/book3.md:236` : feinte de roverso puis mandritto tondo a la jambe.
- `treatises/marozzo/book3.md:352` : mention explicite de la feinte de roverso pour donner mandritto.

### Lecture
Ce pattern est tres frequent : la punta provoque, la feinte de roverso fixe la garde, le mandritto conclut.

---

## Exemple 5 - Punta + roverso de bas en haut au bras + mandritto

Formulation du chapitre 13 :
- "Punta (pied gauche), grand pas du droit, roverso de bas en haut au bras, puis mandritto tete/jambe, avec couverture en roverso a la main d'epee en retraite."

### Occurrences pertinentes relevees

### Manciolino
- `treatises/manciolino/opera_nova.md:331` : formulation de reference (chapitre 13).
- `treatises/manciolino/opera_nova.md:343` : contre correspondant (chapitre 14).
- `treatises/manciolino/opera_nova.md:635` : roverso redoppio de bas en haut au bras dans une sequence d'assaut.

### Marozzo
- `treatises/marozzo/book3.md:96` : roverso redoppio de bas en haut aux bras dans la parade-riposte.
- `treatises/marozzo/book3.md:318` : meme coup, precise sur le bras droit.
- `treatises/marozzo/book1.md:62` : enchainement avec mandritto puis roverso redoppio de bas en haut.

### Lecture
Le roverso redoppio montant au bras est clairement une action technique partagee entre Manciolino et Marozzo.

---

## Tableau de synthese

| Exemple Chapitre 13 | Manciolino (hors ligne-source) | Marozzo |
|---|---|---|
| 1. Tramazzone simple | 307, 355, 451 | book3: 92, 120, 132 |
| 2. Punta + 2 tramazzoni | 547, 619, 637 | book1: 20, 48, 56 |
| 3. Feinte tramazzone -> roverso cuisse | 339, 633 | book3: 112, 238 |
| 4. Punta + feinte roverso -> mandritto | 341, 393, 935, 1109 | book3: 236, 352 |
| 5. Punta + roverso montant bras + mandritto | 343, 635 | book3: 96, 318 ; book1: 62 |

---

## Conclusion

Les cinq exemples du chapitre 13 de Manciolino ne sont pas des cas isoles. Ils reparaissent en continu dans l'Opera Nova de Manciolino (chapitres techniques, contres, assauts) et trouvent des correspondances claires chez Marozzo.

Deux points ressortent :
- Le couple **punta + tramazzoni** est un pivot methodologique majeur.
- La logique **feinte haute -> frappe basse** (tramazzone/roverso feinte puis mandritto ou roverso a la cuisse) est un invariant tactique du corpus.

En pratique, le chapitre 13 apparait comme une synthese operationnelle de schemas deja distribues dans tout l'ensemble des traites, plutot qu'une section autonome.
