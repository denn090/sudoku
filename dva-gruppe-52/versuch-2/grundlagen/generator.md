
# Generator


## ⚙️ Funktionen

### `generate(difficulty_level: int) -> dict`
Erzeugt ein Sudoku-Rätsel mit eindeutiger Lösung in der gewünschten Schwierigkeitsstufe.

#### Parameter:
- `difficulty_level` *(int)* – Schwierigkeitsgrad von 0 bis 3:
  - `0` – Easy
  - `1` – Medium
  - `2` – Hard
  - `3` – Expert

#### Rückgabe:
Ein Dictionary mit folgenden Feldern:
```json
{
  "id": "UUID",
  "difficulty": "easy | medium | hard | expert",
  "board": [[...], [...], ...],         // Das Sudoku mit leeren Feldern (0)
  "solution": [[...], [...], ...],      // Die vollständige Lösung
  "createdAt": "ISO 8601 Zeitstempel"
}
```

---

## 🔧 Interne Hilfsfunktionen

### `fill_board(board: list[list[int]]) -> bool`
Füllt ein 9x9 Sudoku-Board rekursiv mit gültigen Zahlen. Verwendet Backtracking.

### `is_safe(board: list[list[int]], row: int, col: int, num: int) -> bool`
Prüft, ob eine Zahl `num` an der Position `(row, col)` gültig gesetzt werden kann.
> Nutzt `valid` aus `solver.py`.

### `remove_cells(board: list[list[int]], holes: int)`
Entfernt kontrolliert Felder aus dem Board, um die gewünschte Anzahl an „Löchern“ (leeren Feldern) zu erreichen.
> Verwendet `count_solutions` aus `solver.py`, um sicherzustellen, dass das Rätsel **nur eine Lösung** hat.

---

## 🧠 Abhängigkeiten

- **Interne Imports:**
  - `solve` und `count_solutions` müssen in der Datei `solver.py` definiert sein.
  - `valid` sollte die Sudoku-Regeln für eine gültige Platzierung prüfen.

- **Standardbibliothek:**
  - `random`, `copy`, `datetime`, `uuid`, `json`

---

## ✅ Beispiel

```python
from sudoku_generator import generate

puzzle = generate(1)  # Medium Level
print("ID:", puzzle["id"])
print("Board:")
for row in puzzle["board"]:
    print(row)
print("Solution:")
for row in puzzle["solution"]:
    print(row)
```

---

## 📌 Hinweise

- **Anzahl der leeren Felder pro Schwierigkeitsgrad:**
  - **Easy (Schwierigkeitsgrad 0):** ~35 leere Felder
  - **Medium (Schwierigkeitsgrad 1):** ~45 leere Felder
  - **Hard (Schwierigkeitsgrad 2):** ~55 leere Felder
  - **Expert (Schwierigkeitsgrad 3):** ~60 leere Felder

- Jedes generierte Rätsel hat **genau eine Lösung**.
- Die Generierung basiert auf zufälliger Permutation + Backtracking.

