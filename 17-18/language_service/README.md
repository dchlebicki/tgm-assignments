# 17-18_SEW_A10_language_service

Webservices bieten unterschiedliche Funktionalitäten an, die von Clients genutzt werden können. Eine einfache Variante hierfür sind RESTful Webservices. Schreiben Sie ein einfaches RESTful-Webservice inkl. GUI-Client, welches anhand eines eingegebenen Textes erkennt, um welche Sprache es sich handelt!

##### Grundanforderungen (70%):

Webservice

- Das Webservice kann als Skript gestartet werden und horcht anschließend auf eingehende Requests
- Die Ressource des Webservices ist unter einer URL erreichbar, welche den zu überprüfenden Text als GET-Parameter übernimmt
- Das Webservice retourniert ein JSON-Objekt nach folgendem Aufbau:

```
{ 
  reliable (boolean): reliability
  language (string): found language full name
  short (string): found language short name
  prob (integer): probability in percent
}
```

Beispiel: ```{"reliable": true, "language": "GERMAN", "short": "de", "prob": 96}```

- Das Webservice verwendet eine Library zur Detektion der Sprache

Client

- Der Client ist eine grafische Oberfläche in **PyQt**
- Der Client erlaubt die Eingabe eines (mehrzeiligen) Texts
- Der Client gibt das Resultat des Webservices in einem (mehrzeiligen) Textfeld aus, wobei die Resultate fett markiert werden (vgl. Abbildung)
- Der Client bietet drei Buttons an
  - verify: Schickt den Text an das Webservice und zeigt das Ergebnis im Textfeld an
  - reset: Setzt beide Textfelder zurück
  - close: Schließt die Anwendung
- Die Größe des Clients kann sinnvoll skaliert werden
- Webservice und Client sind über Sphinx dokumentiert

Erweiterungen (30%):

- IP und Port des Webservices können über Kommandozeilenparameter konfiguriert werden
- IP und Port können in der Client-GUI konfiguriert werden

Hinweise:

- Es muss keine eigene Spracherkennung implementiert werden! Verwende eine sinnvolle Library
  - Vorschlag: **pycld2** (die Binaries können unter https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycld2 heruntergeladen werden)
- Verwende für den Client **PySide bzw. PyQt** und die **requests**-API
