# Final Project

Arduino is een opensource-computerplatform bedoeld om microcontrollers eenvoudig te maken. Dit platform is bedoeld voor hobbyisten, artiesten, kunstenaars en iedereen die geïnteresseerd is in het maken en ontwerpen van slimme en creatieve objecten.
met een  arduino kun je een oneindige hoeveelheid aan "apparaatjes" maken. Arduino systemen bevatten sensoren, actuatoren en een board, welke C code runt.  Deze software programmeer je zelf en zet je vervolgens op de arduino zodat ie het gewenste gedrag vertoont. het aansturen van een arduino met je smartphone of pc is relatief moeilijk en hier moet je zelf een applicatie ontwikkelen. 

__probleem__
Een aarduino aansturen vanaf je smartphone of pc met een kant en klare interface.

__ONELINER__
de applicatie die ik wil gaan ontwerpen gaat het mogelijk maken om deze arduino's aan te sturen doormiddel van de Webapp waarbij de gebruiker kant en klare controls kan kiezen uit de applicatie en deze kan configureren met de arduino, zonder dat de gebruiker deze knoppen zelf moet  programmeren.

waar mogelijk gaat de app ook stukjes arduino code genereren/tonen gecombineerd met instructies wat de configuratie makkelijker maakt.

__Optioneel__
Daarnaast, wanneer tijd over, gaat de applicatie het mogelijk maken data te  ontvangen van de arduinos en deze op te slaan in sql databases en live te tonen in de app.
Wanneer er nog meer tijd over is, zou een extra functionaliteit zijn om verschillende arduino's met elkaar te verbinden via de webapp, om zo onderlinge communicatie (IOT) mogelijk te makenen te regulieren.  

__proof of concept:__ https://www.youtube.com/watch?v=lteGQrY5Yu4 . in dit filmpje wordt een systeem gebouwd waarin een arduino wordt aangestuurd doormiddel van een Flask applicatie.

__wireframes__
![afbeelding wireframes](https://github.com/uva-webapps/project-martijnwijs/blob/master/wireframesmetuitleg.jpg)

__control buttons__
afhankelijk van de beschikbare tijd kunnen er verschillende control buttons in javascript worden gepogrammeerd. 
voorbeelden zijn in de volgende afbeelding weergegeven.
![afbeelding control buttons](https://github.com/uva-webapps/project-martijnwijs/blob/master/buttons.jpg)

__COMPUTERNETWERK__
de volgende afbeelding laat zien hoe de verschillende elementen in het netwerk met elkaar in verbinding staan.
![afbeelding architectuur](https://github.com/uva-webapps/project-martijnwijs/blob/master/architectuur.jpg)

Doormiddel van een web socket client library  (https://www.arduinolibraries.info/libraries/web-sockets)
staat de arduino in verbinding met de webapp. beiden kunnen door deze  verbinding continu data naar elkaar versturen zonder telkens een nieuwe http request te maken. waarschijnlijk zal de data in JSON's verstuurd worden

De backend  zal in flask of django worden geprogrammeerd met toegang tot sql databases om metingen van de arduino op te slaan.
de frontend zal in html/css worden geprogrammeerd met interactie in javascript.

__libraries__
arduino (C):
socket client library https://www.arduinolibraries.info/libraries/web-sockets voor socket client verbinding met webapp
arduinojson library https://arduinojson.org/

python:
flask of django voor de webapplicatie
json om json files  te kunnen sturen/ontvangen

__vergelijkbare apps__
Arduino IoT Cloud, arduino wordt averbonden met de applicatie via laptop met usb. Dus geen directe verbinding 
https://thingsboard.io/ ,slaat data op en visualiseert maar control opties lijken afwezig. betaald
https://thinger.io/ opensource  Iot platform, betaald.
__struikelblokken__
