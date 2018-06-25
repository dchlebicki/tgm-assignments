# 16-17_SEW_10_observer_newspaper_subscription
## Design Patterns: Observer Zeitungsabo

Schreibe ein Programm mit mehreren Anzeigen!

#### Grundanforderungen

- Ein Verlag startet sein Geschäft und veröffentlicht unterschiedliche Zeitungen
- Man abonniert eine bestimmte Zeitung
    - Jedes Mal, wenn eine neue Ausgabe erscheint, wird der Nutzer informiert und kann sich die aktuelle Ausgabe abrufen
- Das Abo kann jederzeit gekündigt werden
    - Man erhält dann auch keine Aktualisierungen mehr.
    - Die Beobachter geben die Inhalte in der Konsole aus

Empfohlene Vorgehensweise:

1. Verlag mit 3 unterschiedlichen Zeitungen
2. Jede Zeitung hat einen anderen Erscheinungstermin (Anfang, Mitte und Ende des Monats)
3. Verlag lässt das Abonnieren durch Kunden zu
4. Jeder Kunde (zumindest 3) kann jeweils eine oder mehrere Zeitungen abonnieren.
5. Beim Erscheinen einer neuen Ausgabe werden alle abonnierten Kunden informiert.
6. Jeder Kunde kann nun die Ausgabe (und den Inhalt) abrufen.
7. Ein Kunde kann eine oder mehrere Abos kündigen und erhält somit keine Informationen mehr.
8. Beim Erscheinen einer neuen Ausgabe ...

#### Erweiterungen

- Die Beobachter zeigen die Inhalte in einer GUI an

#### Abgabe

Abgabe der ausführbaren Source-Files (Java oder Python) 

Hinweis: Achte auf eine gute Dokumentation!  
