# AGENTS.md

## Projet

TP d'introduction à l'IA (2026-2027) — CHAYRIGUES & BRUGERE.
Dépôt Python avec fonctions utilitaires et leurs tests.

## Structure

- `projet/toolbox.py` — fonctions utilitaires (`is_palindrome`, `word_frequency`, `celsius_to_fahrenheit`)
- `projet/test_toolbox.py` — tests pytest
- `requirements.txt` — dépendances (`ipykernel`, `pytest`)
- `install.sh` — création du venv avec `uv` + installation des dépendances
- `TP_IA_INTRO_26_27.pdf` — énoncé du TP

## Environnement

- Python 3.13, gestion des paquets avec **uv** (pas de pip direct)
- Installation : `bash install.sh` (crée `.venv/`, active, installe `requirements.txt`)
- `.venv/` et `opencode.json` sont dans `.gitignore`

## Commandes

```bash
# Lancer les tests TOUJOURS depuis la racine du projet (l'import est "from projet.toolbox ...")
python -m pytest projet/test_toolbox.py -v

# Réinstaller les dépendances
uv pip install -r requirements.txt
```

⚠️ Exécuter pytest depuis l'intérieur de `projet/` fait échouer l'import `from projet.toolbox import ...`.

## Conventions

- Tests en anglais, fonctions en anglais, docstrings en français.
- Chaque fonction de `toolbox.py` doit être couverte par au moins un test dans `test_toolbox.py`.
- La ponctuation/les espaces sont ignorés dans les fonctions texte (ex. `is_palindrome("un roc si biscornu")` → `True`).
- Commentaires de test obsolètes (« échoue à cause du bug ») à retirer quand le bug est corrigé.
