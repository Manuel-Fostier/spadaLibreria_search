# 🗡 spadaLibreria_search

Outil de recherche sémantique **100% locale** pour traités d'escrime HEMA (Historical European Martial Arts) numérisés et convertis en Markdown.

## Fonctionnalités

- Recherche sémantique par similarité vectorielle dans les traités indexés
- Expansion conditionnelle de la recherche (Phase 1 → Phase 2 si résultats concluants)
- Évaluation des résultats par un LLM local via [Ollama](https://ollama.com)
- Interface CLI avec scores de similarité colorés (Rich)
- Aucune donnée ne quitte votre machine

## Prérequis

- Python 3.10+
- [Ollama](https://ollama.com) installé et en cours d'exécution

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### Cas WSL (Ollama installé sur Windows hôte)

Si vous lancez les scripts depuis WSL mais qu'Ollama tourne sur Windows, l'API doit être accessible depuis WSL.

1. Sur Windows, démarrez Ollama en exposant le service:

```powershell
$env:OLLAMA_HOST = "0.0.0.0:11434"
ollama serve
```

2. Dans WSL, récupérez l'IP de l'hôte Windows (passerelle par défaut) et exportez l'URL:

```bash
WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')
export OLLAMA_BASE_URL="http://$WIN_HOST:11434"
```

Si la passerelle ne répond pas dans votre environnement, essayez le fallback:

```bash
WIN_HOST=$(awk '/nameserver/ {print $2; exit}' /etc/resolv.conf)
export OLLAMA_BASE_URL="http://$WIN_HOST:11434"
```

3. Testez l'accès:

```bash
curl "$OLLAMA_BASE_URL/api/tags"
```

4. Rendez la configuration persistante dans `~/.zshrc`:

```bash
cat <<'EOF' >> ~/.zshrc

# Auto-configure Ollama URL in WSL if not explicitly set.
if grep -qi microsoft /proc/version 2>/dev/null; then
  if [[ -z "$OLLAMA_BASE_URL" && -z "$OLLAMA_HOST" ]]; then
    WIN_HOST=$(ip route 2>/dev/null | awk '/default/ {print $3; exit}')
    if [[ -z "$WIN_HOST" ]]; then
      WIN_HOST=$(awk '/nameserver/ {print $2; exit}' /etc/resolv.conf 2>/dev/null)
    fi
    if [[ -n "$WIN_HOST" ]]; then
      export OLLAMA_BASE_URL="http://$WIN_HOST:11434"
    fi
    unset WIN_HOST
  fi
fi
EOF
```

5. Rechargez votre shell puis vérifiez:

```bash
source ~/.zshrc
echo "$OLLAMA_BASE_URL"
curl "$OLLAMA_BASE_URL/api/tags"
```

Les scripts `ingest.py` et `search.py` utilisent automatiquement `OLLAMA_BASE_URL` (ou `OLLAMA_HOST`).

## Installation

```bash
git clone https://github.com/Manuel-Fostier/spadaLibreria_search.git
cd spadaLibreria_search

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Utilisation

### 1. Indexer les traités

```bash
python ingest.py
```

### 2. Lancer la recherche interactive

```bash
python search.py
```

### 3. Recherche directe en ligne de commande

```bash
python search.py --sources marozzo_book3 anonimo_epee_deux_mains \
  --query "Quando voi fare un colpo di taglia, si deve avanzare il piede destro..."
```

### 4. Recherche multi-query

Chaque requête est exécutée séparément et affichée dans son propre tableau, précédé du texte exact de la requête.

```bash
python search.py --sources marozzo_book3 \
  --query "falso dritto de bas en haut aux mains, porta di ferro alta" \
  --query "Guardia di faccia" \
  --query "Guardia di Croce"
```

## Format des traités

Chaque fichier `.md` doit avoir un frontmatter YAML :

```yaml
---
author: "Marozzo"
title: "Opera Nova - Libro Terzo"
book: "book3"
source_id: "marozzo_book3"
language: "it"
---
```

Le champ `source_id` est l'identifiant utilisé dans les prompts de recherche.

## Exemple de prompt interactif

```
> Votre prompt :
Recherche des paragraphes similaires dans le livre 3 de Marozzo puis dans
la partie sur l'épée à 2 mains de l'Anonimo. Si les résultats sont concluants,
recherche dans les livres 1 et 2 de Marozzo et dans l'Opera nova de Manciolino.
Quando voi fare un colpo di taglia, si deve avanzare il piede destro...

[ligne vide × 2 pour valider]
```

## Structure du projet

```
spadaLibreria_search/
├── treatises/
│   ├── marozzo/
│   │   ├── metadata.json
│   │   ├── book1.md
│   │   ├── book2.md
│   │   └── book3.md
│   ├── anonimo/
│   │   └── epee_deux_mains.md
│   └── manciolino/
│       └── opera_nova.md
├── chroma_db/        # Base vectorielle (générée par ingest.py)
├── ingest.py         # Script d'indexation
├── search.py         # Script de recherche
├── requirements.txt
└── README.md
```

## Sources d'exemple incluses

| `source_id` | Auteur | Livre |
|---|---|---|
| `marozzo_book1` | Marozzo | Opera Nova - Libro Primo |
| `marozzo_book2` | Marozzo | Opera Nova - Libro Secondo |
| `marozzo_book3` | Marozzo | Opera Nova - Libro Terzo |
| `anonimo_epee_deux_mains` | Anonimo | Trattato - Spada a due mani |
| `manciolino_opera_nova` | Manciolino | Opera Nova |

## Scores de similarité

| Couleur | Score | Interprétation |
|---|---|---|
| Vert | ≥ 0.75 | Très similaire — passage probablement lié |
| Jaune | 0.60 – 0.74 | Similaire — à vérifier |
| Rouge | < 0.60 | Faible similarité |
