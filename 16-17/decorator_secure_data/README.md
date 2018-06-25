# 16-17_SEW_11_decorator_secure_data

## Design Patterns: Decorator Sichere Daten

Schreiben Sie in einem Programm, dass Daten mittels Passwort und Verschlüsselung
gegen unerwünschten Zugriff schützt.

[siehe e-learning für UML-Diagramm]

Der angehängte Code dient zum Ausführen und Verifizieren der Funktionalität!

Die Klasse TextReader ist die Basis für die Decorator-Klasse und die Worker-Klasse

Ausgabe:

main: let's start! <br>
PASSWORD: 123456 <br>
INPUT:    Mein total sicherer Text! <br>
encrypt: <br>
main:     H\`diojo\gnd^c\`m\`mO\`so <br>
PASSWORD: 123456 <br>
decrypt: <br>
Output:   Mein total sicherer Text! <br>



Empfohlene Vorgehensweise:

1. Eingabe eines Passwortes
2. Eingabe des Textes
3. Verschlüsselung des Textes
4. Ausgabe des verschlüsselten Textes
5. Erneute Eingabe des Passworts
6. Falls das Passwort korrekt war:
    1. Entschlüsselung des Textes
    2. Ausgabe des entschlüsselten Textes
7. Falls das Passwort nicht korrekt war:
    1. Hinweis zur fehlerhaften Eingabe des Passwortes
8. Beendigung des Programmes

Erweiterung:

Verwenden Sie anstatt der Klasse TextReader ein Interface TextReader!

Abgabe:

Abgabe der ausführbahren Source-Files (Java) laut Abgaberichtlinie! 

Hinweis: Achten Sie auf ein gute Dokumentation!  
