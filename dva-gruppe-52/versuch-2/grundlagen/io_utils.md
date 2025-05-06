
# 📄 Dokumentation: Sudoku JSON Struktur & I/O Utilities

## 🔢 Sudoku-Datenstruktur

Ein Sudoku-Datensatz wird in JSON-Format gespeichert und enthält folgende Felder:

```json
{
  "id": "001",
  "difficulty": "easy",
  "board": [[...], [...], ...],
  "solution": [[...], [...], ...],
  "createdAt": "2023-08-01T00:00:00Z"
}
```

### Felder im Detail

| Feld         | Typ                | Beschreibung |
|--------------|--------------------|--------------|
| `id`         | `string`           | Eindeutige Kennung des Sudoku-Rätsels. |
| `difficulty` | `string` *(optional)* | Schwierigkeitsgrad, z. B. `"easy"`, `"medium"`, `"hard"`. |
| `board`      | `int[9][9]`        | 9×9 Sudoku-Gitter. Leere Felder = `0`. |
| `solution`   | `int[9][9] \| null`| Lösung des Sudoku (keine Nullen erlaubt) oder `null`, wenn nicht verfügbar. |
| `createdAt`  | `string (ISO 8601)`| Erstellungsdatum des Rätsels. |

---

## 📥 `import_sudoku(filepath: str) -> list`

### Beschreibung
Lädt ein Sudoku aus einer `.json`-Datei, validiert die Daten und gibt das Sudoku-Board zurück.

### Parameter
- `filepath` (`str`): Pfad zur JSON-Datei.

### Rückgabe
- `board` (`list[list[int]]`): Das Sudoku-Board (Werte zwischen 0–9).

### Fehler
- `FileNotFoundError`: Falls die Datei nicht existiert.
- `ValueError`: Bei fehlerhafter Datenstruktur.

---

## 📤 `export_sudoku(filepath: str, sudoku_data: dict)`

### Beschreibung
Speichert Sudoku-Daten im JSON-Format in eine Datei.

### Parameter
- `filepath` (`str`): Ziel-Dateipfad.
- `sudoku_data` (`dict`): Die vollständige Sudoku-Datenstruktur.

---

## ✅ `validate_sudoku_data(data: dict)`

### Beschreibung
Validiert die Struktur und Werte des übergebenen Sudoku-Datensatzes.

### Validierungen
- Muss `id`, `board`, `solution` enthalten.
- `board` muss ein 9×9 Gitter mit Werten von `0`–`9` sein (`0` = leer).
- `solution`, falls vorhanden, muss ein 9×9 Gitter mit Werten von `1`–`9` sein.

### Fehler
- `ValueError`: Bei ungültiger Struktur oder unzulässigen Werten.

---

## 📦 Beispiel: Sudoku laden und validieren

```python
import json
from sudoku_utils import import_sudoku

try:
    board = import_sudoku("sudoku_001.json")
    print("Sudoku erfolgreich geladen!")
except Exception as e:
    print(f"Fehler: {e}")
```

