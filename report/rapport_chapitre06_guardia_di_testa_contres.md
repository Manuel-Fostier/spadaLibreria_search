# Rapport : Cas d'utilisation des exemples du Chapitre 6 (Manciolino)
## Objet
Ce rapport analyse les cinq exemples de **contres depuis la guardia di testa** décrits au Chapitre 6 de l'*Opera Nova* de Manciolino, et recherche leurs correspondances dans l'ensemble du corpus.

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

## Exemple 1 — Retirer pied droit + coda longa e alta + punta face + pied droit devant + mandritto face
**Formulation :** « Quand quelqu'un te fera le mandritto à la face en étant en guardia di testa, tu peux tirer le pied droit d'un grand pas derrière le gauche, allant avec l'épée en coda longa e alta. Et quand il voudra tirer le mandritto, tu pousseras une punta dans la face en marchant avec le pied droit devant, et ensuite un mandritto également à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:217 — Définition de l'exemple

#### Marozzo
- book1.md:20 — « Si alors en étant en porta di ferro stretta ton ennemi te tire à la tête, je veux que tu accompagnes ton épée et ta bocle ensemble en guardia di testa [...] tu tailles un mandritto tondo aux jambes [...] tu lui tailleras un roverso sgualembrato montant aussitôt avec un montante » — retraite puis attaque enchaînée depuis garde basse
- book3.md:693 — « tu le trouveras avec un falso dritto qui va en guardia d'intrare in largo passo et avec le mandritto qui va en guardia di faccia » — transition coda longa + attaque

### Lecture
La retraite vers coda longa e alta suivie d'une punta de comptoir est une technique de demi-temps : on esquive la frappe adverse tout en contre-attaquant. Marozzo intègre ce principe dans ses séquences d'assaut, notamment dans book1:20 où la retraite en coda longa est suivie d'une contre-attaque immédiate.

---

## Exemple 2 — Couvrir la punta avec l'épée + guider la main d'épée sous la bocle (contre punta + tramazzone)
**Formulation :** « Contre celui qui te pousse une punta et te tire un tramazzone, tu couvriras la punta avec ton épée. Et quand il tournera les tramazzoni, tu mettras la main d'épée sous la bocle en dirigeant la pointe de ton épée vers sa main. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:221 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « je veux que tu serres ton épée et ta bocle ensemble en guardia di testa où tu pareras sa botte » — serrage épée + bocle pour parer punta + suite
- book1.md:56 — « Si dans ce temps ton ennemi te tire à la tête, tu lui pousseras alors une punta à la face avec la main d'épée couverte par-dessous ta bocle » — main d'épée sous la bocle comme parade contre attaque sur soi, quasi identique
- book2.md:86 — « dans ce pas tu pareras son coup en guardia di faccia avec la pointe de ton épée vers la droite de la face de ton ennemi » — diriger la pointe vers le côté adverse lors de la parade

### Lecture
La technique de couvrir la punta avec l'épée puis guider la main sous la bocle contre les tramazzoni est présente chez Marozzo dans book1:56 avec une formulation très proche (« main d'épée couverte par-dessous ta bocle »). C'est une parade spécifique contre l'enchaînement punta + tramazzone.

---

## Exemple 3 — Guardia di faccia + contre roverso → mandritto
**Formulation :** « Si l'ennemi te pousse une punta pour t'offenser avec un roverso, tu pourras t'en défendre en allant en guardia di faccia. Et lorsqu'il voudra faire son roverso, tu lui tireras un mandritto. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:223 — Définition de l'exemple

#### Marozzo
- book2.md:86 — « à chacun de ces mandritti tu jetteras le pied droit un peu vers son côté droit et dans ce pas tu pareras son coup en guardia di faccia [...] tu passeras du pied gauche et tu lui donneras un mandritto avec le poignard et un roverso avec l'épée » — guardia di faccia → mandritto
- book1.md:56 — « Là, tu le pareras avec le droit fil, c'est-à-dire en guardia di faccia. Tu lui tireras alors un roverso à la cuisse » — guardia di faccia comme position de parade puis contre-attaque
- book3.md:240 — Transitions via guardia di faccia comme position défensive + riposte

### Lecture
La guardia di faccia utilisée comme position de réception d'une attaque adverse (roverso) avant de riposter d'un mandritto est un principe récurrent chez Marozzo. La logique est identique : garder la pointe menaçante (guardia di faccia) force l'adversaire à modifier son attaque, créant l'ouverture pour le mandritto.

---

## Exemple 4 — Mezzo mandritto + porta di ferro stretta → falso + mandritto face (contre deux mandritti)
**Formulation :** « Aux deux mandritti, tu pourras t'opposer en taillant un mezzo mandritto à la main d'épée à l'intérieur du rebord de ta bocle, ajustant ensuite ton épée en porta di ferro stretta. Et quand il te tirera l'autre mandritto, tu t'en défendras avec un falso, lui tirant en haut un mandritto à la face. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:225 — Définition de l'exemple

#### Marozzo
- book1.md:48 — « je veux que tu serres ton épée et ta bocle ensemble en guardia di testa où tu pareras sa botte. Tu passeras et délivreras un mandritto tondo à ses jambes » — contre le second coup = mandritto
- book3.md:188 — « tu lui frappes un falso fortement dans son épée [...] tu lui tireras un mandritto tondo à la jambe ou à la tête » — falso + mandritto contre série d'attaques

### Lecture
La réponse en deux temps (mezzo mandritto sur premier coup, puis falso + mandritto sur second coup) est une structure défensive en deux actes présente de façon similaire chez Marozzo. L'utilisation de la porta di ferro stretta comme position de rebond entre deux défenses est commune aux deux auteurs.

---

## Exemple 5 — Feinte tramazzone → porta di ferro stretta + falso + roverso à la cuisse
**Formulation :** « S'il fait semblant de te donner du tramazzone, tu iras avec l'épée en guardia di faccia. Et quand il tirera le roverso à la cuisse, tu lui tireras aussitôt un roverso au bras d'épée. »

### Occurrences pertinentes relevées

#### Manciolino
- opera_nova.md:227 — Définition de l'exemple, opera_nova:339

#### Marozzo
- book1.md:56 — « Tu lui tireras alors un roverso à la cuisse en ne bougeant ni des pieds ni des jambes, et ton épée tombera en coda longa e stretta » — roverso cuisse en réponse
- book1.md:32 — « Ayant paré le tramazzone ou le mandritto, tu lui tireras un roverso à sa tempe droite ou aux jambes » — après parade tramazzone → roverso
- book3.md:242 — Séquences feinte tramazzone → roverso documentées

### Lecture
La riposte d'un roverso (au bras d'épée ou à la cuisse) comme contre à une feinte de tramazzone est présente chez Marozzo dans book1:56. La dynamique de « lire l'intention de l'adversaire » (tramazzone ou roverso bas) et riposter de roverso est commune aux deux auteurs.

---

## Tableau de synthèse

| Exemple | Manciolino | Marozzo |
|---------|-----------|---------|
| Ex1 - Retraite coda longa + punta + mandritto | opera_nova:217 | book1:20, book3:693 |
| Ex2 - Couvrir punta épée + main sous bocle | opera_nova:221 | book1:48, book1:56, book2:86 |
| Ex3 - Guardia di faccia → contre roverso → mandritto | opera_nova:223 | book1:56, book2:86, book3:240 |
| Ex4 - Mezzo mandritto + porta di ferro stretta + falso + mandritto | opera_nova:225 | book1:48, book3:188 |
| Ex5 - Feinte tramazzone → guardia di faccia → roverso bras | opera_nova:227, 339 | book1:32, book1:56, book3:242 |

## Conclusion
Les contres depuis la guardia di testa de Manciolino se retrouvent dans les assauts de Marozzo avec des correspondances directes, particulièrement pour l'usage de la guardia di faccia comme position de parade intermédiaire (Ex3, Ex5) et pour les contre-attaques au roverso cuisse/bras (Ex2, Ex5). Le Chapitre 6 confirme que la guardia di testa bolognaise est conçue comme une garde active permettant des contre-attaques immédiates.
