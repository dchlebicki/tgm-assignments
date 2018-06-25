# 17-18_SEW_A05_google_maps_rest_api

Erstellen Sie einen Client, der eine Auto-Navigation mittels Google Drive API ermöglicht.

```
url = "http://maps.googleapis.com/maps/api/directions/json"
```

* Beachten Sie bei der Umsetzung auch das MVC-Pattern.
* Verwenden Sie auch eine Statusinformation für Berechnung bzw. Fehler aufgrund der Start/Ziel-Adressen
* Für die Umsetzung ist Python empfohlen, jedoch sind auch andere Plattformen denkbar, die für die Beurteiler vorhanden sind (JavaScript oder Java) 

#### Beurteilungskriterien

Kriterium 1: MVC-Pattern

* Model, View und Controller sind eigene Klassen, voneinander getrennt und befinden sich in eigenen Modulen
* Das MVC-Pattern wurde nach den bekannten Standards implementiert

Kriterium 2: Grafische Oberfläche

* Es gibt zwei Eingabefelder: Start und Ziel
* Es gibt einen Ausgabebereich, welcher das Ergebnis einerseits in Gesamt und andererseits im Detail darstellt
* Die wesentlichen Informationen werden hervorgehoben
* Es gibt drei Buttons
    * Submit: Schickt die Anfrage mit Start und Ziel an die Google API
    * Reset: Leert alle Eingabe- und Ausgabefelder
    * Close: Mit Close kann die Applikation beendet werden
* In der Statusleiste (unten) wird der Fortschritt der Berechnung bzw. Fehler wiedergegeben

Kriterium 3: REST-Service

* Bei einem Klick auf Submit wird die angegebene URL mit den jeweiligen Parametern angesprochen
* Wird eine andere Plattform als Python verwendet, so ist dies in der Dokumentation zu begründen
* Das Ergebnis-XML wird korrekt geparsed und in dem GUI angezeigt
* Im Fehlerfall wird eine entsprechende Information in der Statusleiste angezeigt und der Fehler wird im Ausgabebereich angezeigt

Kriterium 4: Dokumentation

* Methoden (außer Getter und Setter) sind kommentiert
* Es existiert eine vollständige Sphinx-Dokumentation (inkl. Übersicht des Moduls)
* Der Code ist nachvollziehbar kommentiert

Kriterium 5: Fehlerbehandlung

* Wenn das Service nicht verfügbar ist, wird eine entsprechende Fehlermeldung angezeigt
* Start und Ende sind auffindbar, ansonsten wird eine Fehlermeldung angezeigt
* In der Statusleiste (unten) wird angezeigt, ob der letzte Request erfolgreich war oder nicht

Kriterium 6: XML-Modus (Erweiterung)

* Es existiert die Möglichkeit, die XML-Variante der Google Maps API anzusprechen
* Eine entsprechende Eingabemöglichkeit (z.B. RadioButton) steuert, ob die XML- oder JSON-Variante verwendet wird
