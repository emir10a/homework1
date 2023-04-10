# master-studium repository

Dieses Python-Projekt enthält vier einfache Funktionen zur mathematischen Berechnung: `add`, `subtract`, `multiply` und `divide`. Das Ziel des Projekts ist es, die Funktionsweise von Python-Funktionen und Unit-Tests zu demonstrieren.

## Funktionen

Jede der vier Funktionen akzeptiert zwei numerische Argumente und gibt das Ergebnis der entsprechenden mathematischen Operation zurück.

- `add(x, y)` - gibt die Summe von `x` und `y` zurück.
- `subtract(x, y)` - gibt die Differenz von `x` und `y` zurück.
- `multiply(x, y)` - gibt das Produkt von `x` und `y` zurück.
- `divide(x, y)` - gibt den Quotienten von `x` und `y` zurück. Eine `ValueError`-Ausnahme wird ausgelöst, wenn `y` 0 ist.

## Verwendung

Um diese Funktionen zu verwenden, können sie in ein anderes Python-Skript importiert werden, indem der `functions`-Modul importiert wird:

```python
from functions import add, subtract, multiply, divide

result = add(2, 3) # result is 5

```
Alternativ kann auch die `main.py` Datei ausgeführt werden, um die Funktionen zu testen:

```bash
python main.py
```
## Tests

Diese Funktionen sind mit Unit-Tests ausgestattet, die in `test_functions.py` definiert sind. Diese Tests können ausgeführt werden, um sicherzustellen, dass die Funktionen wie erwartet funktionieren:
```bash
python functions.py
```
Wenn alle Tests erfolgreich sind, sollten Sie eine Ausgabe sehen, die angibt, dass alle Tests bestanden wurden. Wenn ein Test fehlschlägt, wird eine Fehlermeldung ausgegeben, die den fehlgeschlagenen Test und die tatsächlich erhaltene Ausgabe beschreibt.
## Autoren

Dieses Projekt wurde von Emir Avdic erstellt. 

## Lizenz

Copyright 2023 Emir Avdic

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
