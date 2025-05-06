## Einleitung
Mit der zunehmenden Leistungsfähigkeit moderner KI-Modelle stellt sich nicht nur die Frage, wie kreativ oder vielseitig sie sind, sondern auch, inwieweit sie bei der Lösung klassischer algorithmischer Probleme unterstützen können. 
Eines dieser Probleme ist das Sudoku.
Es ist ein logikbasiertes Zahlenspiel, das sich gut eignet, um Programmierkonzepte wie Backtracking, Validierung und GUI-Integration zu demonstrieren.

In unserem zweiten Experiment entwickeln wir einen vollständigen Sudoku-Solver. 
Ziel ist es, ein Programm zu erstellen, das beliebige Sudoku-Rätsel aus einer JSON-Datei einliest, auf Korrektheit prüft und, sofern lösbar, automatisch auf grafischer Oberfläche darstellt und löst.

**Dabei liegt der Fokus auf mehreren Aspekten:** 
- Dem Einlesen und Validieren der Spieldaten
- Der Implementierung eines Lösungsalgorithmus
- Die Einbindung in eine grafische Benutzeroberfläche. 

Zusätzlich wollen wir untersuchen, wie man Programmteile so strukturiert, dass sie leicht testbar und wiederverwendbar sind.

### Zielsetzung
Ziel dieses Versuchs ist es, ein modulares und robustes System zur Lösung von Sudokus zu entwickeln. 
Dabei sollen sowohl die technische Umsetzung als auch die Benutzerfreundlichkeit berücksichtigt werden. 
Der Aufbau des Projekts erfolgt in mehreren Schritten, von der Datenverarbeitung über die Spiellogik bis hin zur visuellen Darstellung. 
Besonderes Augenmerk legen wir auf die Validierung der Eingabedaten, die Effizienz des Lösungsalgorithmus und die klare Trennung der Funktionsbereiche innerhalb des Programmcodes.