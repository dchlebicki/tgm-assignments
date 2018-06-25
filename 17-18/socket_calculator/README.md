# 17-18_SEW_A08_socket_calculator
## A08: Socket Rechner

Server stellen unterschiedliche Funktionalitäten zur Verfügung. Um Overhead von höheren Protokollen einzusparen, wird manchmal ein eigenes Socket-Protokoll implementiert.  
Implementiere einen multithreaded Java-Server, welcher auf einen vorgegebenen Port auf eingehende Verbindungen horcht. Verbindet sich ein neuer Client, wird ein neuer Thread (eigene Klasse) erzeugt, welcher sich um die Kommunikation mit dem neuen Client kümmert. Dadurch kann der Server sofort wieder neue Verbindungen akzeptieren.  
Der Server unterstützt simple Rechenoperationen, welche vom Client an den Server geschickt
werden:

* !exit: Schließt die Verbindung zum Client
* !add \<z1> \<z2>: addiert die zwei Zahlen z1 und z2 und liefert das Ergebnis zurück
* !subtract \<z1> \<z2>: zieht z2 von z1 ab und liefert das Ergebnis zurück
* !buy \<z> (Erweiterung): erhöht die Credits des Clients um z

Jede Rechenoperation kostet jeweils 1 Credit. Der Server verwaltet die Credits in einer geteilten, threadsicheren Collection und initialisiert die Credits mit einem Startwert von 10 pro Client. Hat ein Client nicht genügend Credits, wird ihm dies entsprechend mitgeteilt.

Zusätzlich logt der Server threadsicher mit, wenn ein Client eine Operation ausführt.
