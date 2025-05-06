## Grundlagen
In diesem Kapitel werden die wichtigsten Konzepte und Technologien erläutert, die dem Aufbau unseres Sudoku-Solvers zugrunde liegen. 
Neben den logischen Grundlagen des Spiels Sudoku werden die Funktionsweise gängiger Lösungsalgorithmen dargestellt. 
Zudem beschreiben wir die im Projekt verwendeten Softwaretechnologien wie Python, die grafische Benutzeroberfläche mit Tkinter sowie die eingesetzten Datenformate und die Projektstruktur.

### Allgemeine Spielregeln und Logik von Sudoku
Sudoku ist ein logikbasiertes Zahlenspiel, das auf einem 9×9-Gitter basiert, das wiederum in neun 3×3-Blöcke unterteilt ist. 
Ziel des Spiels ist es, das Gitter so mit den Ziffern 1 bis 9 zu füllen, dass jede Zahl genau einmal in jeder Zeile, jeder Spalte und in jedem der neun Blöcke vorkommt. 
Dabei sind zu Beginn bereits einige Zahlen vorgegeben, die sogenannte Startkonfiguration.

Das Lösen eines Sudokus erfordert logisches Denken und manchmal auch strategisches Raten. 
Für Computerprogramme bedeutet das:  
Die Lösung muss unter Berücksichtigung klarer Konsistenzregeln gefunden werden. 
Ein ungültiger Spielstand entsteht, wenn z. B. eine Zahl doppelt in einer Zeile oder einem Block vorkommt. Das muss frühzeitig erkannt und vermieden werden.

### Lösungsstrategien und Algorithmen
Für das automatisierte Lösen von Sudokus gibt es verschiedene Ansätze. 
Die bekannteste Methode ist Backtracking, ein rekursiver Algorithmus, der systematisch alle möglichen Zahlenkombinationen ausprobiert und bei ungültigen Zuständen zurückspringt. 
Dieser Algorithmus wird auch in unserem Projekt verwendet.

**Vereinfacht gesagt:**
1. Leeres Feld finden
2. Alle möglichen Zahlen (1–9) ausprobieren
3. Für jede Zahl: Prüfen, ob sie gültig ist (nicht doppelt in Zeile, Spalte, Block)
4. Bei gültiger Zahl: Rekursiv mit nächstem leeren Feld fortfahren
5. Wenn keine Zahl gültig ist: zurückspringen (Backtracking)

Obwohl der Algorithmus auf den ersten Blick ineffizient erscheint, funktioniert er bei klassischen Sudokus sehr schnell, da viele ungültige Kombinationen frühzeitig ausgeschlossen werden können.

### Technologischer Aufbau des Projekts
Das Projekt wurde vollständig in Python umgesetzt und ist in mehrere Module unterteilt:
- `main.py`: Einstiegspunkt des Programms, übernimmt den Ablauf
- `io_utils.py`: Ein- und Ausgabe von Sudoku-Daten im JSON-Format inkl. Validierung
- `gui_main.py`: Grafische Darstellung und visuelles Feedback mit Hilfe der Bibliothek Tkinter
- `hints.py`, `difficulty.py`: Zusatzfunktionen für Hinweise und Schwierigkeitsanalyse

Die Sudokus werden in JSON-Dateien gespeichert, die neben dem Spielbrett (board) auch die Lösung (solution) enthalten. 
Diese Dateien dienen sowohl als Eingabe für das Programm als auch als Testbasis zur Überprüfung der korrekten Lösung.

### Verwendung von Tkinter für die grafische Benutzeroberfläche
Zur Darstellung des Spielfelds wurde die in Python integrierte GUI-Bibliothek Tkinter verwendet. 
Damit lassen sich einfache grafische Elemente wie Buttons, Textfelder und Rasterlayouts effizient umsetzen. 
In unserem Projekt wird das Sudoku-Gitter als interaktive Oberfläche dargestellt, die es erlaubt, den Lösungsprozess visuell zu verfolgen.

Die Umsetzung der GUI war ein wesentlicher Teil des Projekts, da sie nicht nur die Nutzbarkeit erhöht, sondern auch beim Debugging und Testen des Algorithmus unterstützt.

### Projektstruktur und Modularität
Das Sudoku-Solver-Projekt ist modular aufgebaut, sodass Einleseroutine, Spiellogik, GUI und Tests klar voneinander getrennt sind. 
Dies erleichtert nicht nur die Wartung und Weiterentwicklung, sondern ermöglicht auch die Wiederverwendung einzelner Module in anderen Kontexten, z. B. zur Integration in eine App oder für größere KI-Vergleiche mit automatischer Bewertung.