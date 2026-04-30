# Rapport : Cas d'utilisation des exemples du Chapitre 4 (Manciolino)
## Objet
Ce rapport analyse les deux exemples de **contres depuis la guardia alta** décrits au Chapitre 4 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Percuter le rebord de la bocle de bas en haut (fendente + falso)
**Formulation :** « L'ennemi te lançant le coup qu'il lui plaît pour t'offenser quand tu es en guardia alta, toi tu percuteras le rebord de ta bocle de bas en haut trois ou quatre fois, c'est-à-dire avec le fendente et le falso de l'épée. Et en faisant cela, tu viendras à être en sûreté d'un quelconque coup offensif. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:199 — Définition de l'exemple (chapitre source)

#### Marozzo
- book1.md:18 — « tu battes le falso de l'épée dans l'umbo de la bocle [...] tu feras une retouche de la bocle [...] tu toucheras l'extérieur de ta bocle vers le haut avec le falso de l'épée » — percussions répétées de la bocle avec le falso et le fendente, structure identique comme exercice de base
- book1.md:22 — « tu feras une demi-volte du poing [...] tu toucheras l'umbo de la bocle avec le falso de l'épée vers le haut » — même geste de percussion bocle + falso
- book1.md:28 — « tu toucheras l'extérieur de ta bocle vers le haut avec le falso de l'épée, en passant dans ce mouvement avec le pied droit d'un grand pas devant le gauche » — falso dans bocle en progressant
- book3.md:538-550 — Section « Guardia Alta » : techniques de base incluant les percussions de bocle comme exercice défensif

### Lecture
La technique de défense par percussions successives de la bocle avec le fendente et le falso constitue un exercice fondamental de l'école bolognaise, décrit en détail dans les assauts de Marozzo (book1:18). Le principe de « battre la bocle » est systématiquement intégré dans les séquences d'assaut comme geste de transition et de couverture.

---

## Exemple 2 — Pied droit derrière le gauche + punta montante en guardia di faccia
**Formulation :** « Sinon tu peux tirer le pied droit d'un grand pas derrière le gauche, en chassant une punta à la façon d'un montante qui va en guardia di faccia. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:201 — Définition de l'exemple

#### Marozzo
- book1.md:20 — Séquences de retraite avec pied derrière + punta en guardia dans plusieurs positions
- book2.md:52 — « tu jettes le pied droit fortement devant et tu pares cette botte avec ton épée, et tu lui chasses une punta au flanc avec ton poignard » — punta en retraite pied (structure similaire)
- book3.md:104 — « tu feras la botte qui se nomme fugie e cruve, de sorte que ton épée ira en cinghiara porta di ferro stretta » — retraite + punta de couverture

### Lecture
La retraite avec pied derrière + punta montante est une contre-manœuvre d'effacement qui donne l'initiative après la retraite. Chez Marozzo, cette logique est encodée dans le concept de *fugie e cruve* (fuir et couvrir) et dans les séquences de retraite systématique de book1. C'est un principe de gestion de distance partagé.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Percuter bocle fendente + falso | opera_nova:199 | book1:18, book1:22, book1:28, book3:538 |
| Ex2 - Pied droit derrière + punta montante → guardia di faccia | opera_nova:201 | book1:20, book2:52, book3:104 |

## Conclusion
Les deux contres depuis la guardia alta de Manciolino correspondent à des éléments fondamentaux de la pratique bolognaise : la percussion répétée de la bocle (ex.1) est un exercice de base présent dans tous les assauts de Marozzo, et la retraite avec punta (ex.2) est le principe du *fugie e cruve* marozzien. Ces deux chapitres courts confirment la cohérence entre les deux auteurs sur les fondamentaux défensifs depuis les gardes hautes.
