# 🗡 spadaLibreria_search

Moteur de recherche hybride **100% local** pour traités d'escrime HEMA (Historical European Martial Arts) numérisés et convertis en Markdown.

Propulsé par [QMD](https://github.com/tobi/qmd) — BM25 full-text + recherche vectorielle sémantique + re-ranking LLM, sans aucune donnée envoyée en dehors de votre machine.

## Fonctionnalités

- **BM25** : recherche plein texte exacte et exhaustive (termes techniques, noms de gardes)
- **Vectoriel** : recherche sémantique par similarité (même concept, formulation différente)
- **Hybride + re-ranking** : fusion RRF + LLM re-ranker pour la meilleure précision
- **MCP server** : intégration native avec Claude Desktop
- Aucune donnée ne quitte votre machine

## Prérequis

- Node.js >= 22
- [QMD](https://github.com/tobi/qmd)

### Installation de Node.js (via fnm, sans sudo)

```bash
curl -fsSL https://fnm.vercel.app/install | bash -s -- --install-dir "$HOME/.local/bin" --skip-shell

# Ajouter à ~/.zshrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.zshrc

source ~/.zshrc
fnm install 22
fnm use 22
```

### Installation de QMD

```bash
npm install -g @tobilu/qmd
```

Les modèles GGUF (embedding, re-ranking, query expansion) sont téléchargés automatiquement depuis HuggingFace au premier usage (~2 Go au total).

## Installation du projet

```bash
git clone https://github.com/Manuel-Fostier/spadaLibreria_search.git
cd spadaLibreria_search
```

## Utilisation

### 1. Indexer les traités

```bash
qmd collection add ./treatises --name hema
qmd embed
```

### 2. Recherche BM25 — termes exacts et exhaustifs

```bash
# Toutes les occurrences exactes d'un terme
qmd search "deux empans"

# Recherche dans la collection hema uniquement
qmd search "falso dritto" -c hema
```

### 3. Recherche hybride — sémantique + BM25 + re-ranking (recommandée)

```bash
# Hybride avec re-ranking LLM (meilleure qualité)
qmd query "deux empans falso dritto"

# Coller un extrait d'un traité pour trouver des passages parallèles
qmd query "tu jetteras le pied droit deux empans derrière le gauche et alors tu tireras un falso dritto de bas en haut aux mains"

# Plusieurs concepts
qmd query "guardia di faccia porta di ferro alta"
```

### 4. Recherche vectorielle seule

```bash
qmd vsearch "retraite suivie d'un coup ascendant aux mains"
```

### 5. Modes de sortie pour les agents / scripts

```bash
# JSON structuré
qmd query --json "falso dritto"

# Chemins seuls (pour piping)
qmd search --files "deux empans"

# Contenu complet des documents matchés
qmd query --full "guardia di testa"
```

## Intégration MCP avec Claude Desktop

QMD expose un serveur MCP. Depuis WSL, utiliser le transport HTTP :

```bash
# Démarrer le serveur MCP en arrière-plan
qmd mcp --http --daemon

# Vérifier qu'il tourne
qmd status
```

Configuration Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json` sur Windows) :

```json
{
  "mcpServers": {
    "qmd": {
      "url": "http://localhost:8181/mcp"
    }
  }
}
```

## Configuration QMD

Le fichier `qmd.yml` à la racine du projet :

```yaml
collections:
  hema:
    path: ./treatises
    pattern: "**/*.md"
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
│   └── manciolino/
│       └── opera_nova.md
├── qmd.yml           # Configuration des collections
└── README.md
```

## Sources incluses

| Auteur | Livre | Fichier |
|---|---|---|
| Marozzo | Opera Nova - Libro Primo | `treatises/marozzo/book1.md` |
| Marozzo | Opera Nova - Libro Secondo | `treatises/marozzo/book2.md` |
| Marozzo | Opera Nova - Libro Terzo | `treatises/marozzo/book3.md` |
| Manciolino | Opera Nova | `treatises/manciolino/opera_nova.md` |

## Scores QMD

| Score | Interprétation |
|---|---|
| 0.8 – 1.0 | Très pertinent |
| 0.5 – 0.8 | Modérément pertinent |
| 0.2 – 0.5 | Peu pertinent |
| < 0.2 | Faible pertinence |
