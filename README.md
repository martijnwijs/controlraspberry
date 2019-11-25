# Final Project

Arduino is een opensource-computerplatform bedoeld om microcontrollers eenvoudig te maken. Dit platform is bedoeld voor hobbyisten, artiesten, kunstenaars en iedereen die geïnteresseerd is in het maken en ontwerpen van slimme en creatieve objecten.
met een  arduino kun je een oneindige hoeveelheid aan "apparaatjes" maken. Arduino systemen bevatten sensoren, actuatoren en een board, welke een soort C software runt.  Deze software programmeer je zelf en zet je vervolgens op de arduino zodat ie het gewenste gedrag vertoont.   

de applicatie die ik wil gaan ontwerpen gaat het mogelijk maken om deze arduino's aan te sturen doormiddel van de Webapp, data te  ontvangen van de arduinos en eventueel (bij genoeg tijd) verschillende arduino's met elkaar gaat verbinden, om zo onderlinge communicatie (IOT) mogelijk te maken.  

__proof of concept:__ https://www.youtube.com/watch?v=lteGQrY5Yu4 . in dit filmpje wordt een systeem gebouwd waarin een arduino wordt aangestuurd doormiddel van een Flask applicatie.

__wireframes__
![afbeelding wireframes](https://github.com/uva-webapps/project-martijnwijs/blob/master/wireframesmetuitleg.jpg)
__COMPUTERNETWERK__
de volgende afbeelding laat zien hoe de verschillende elementen in het netwerk met elkaar in verbinding staan.
![afbeelding architectuur](https://github.com/uva-webapps/project-martijnwijs/blob/master/architectuur.jpg)

Doormiddel van een web socket client library  (https://www.arduinolibraries.info/libraries/web-sockets)
staat de arduino in verbinding met de webapp. beiden kunnen door deze  verbinding continu data naar elkaar versturen zonder telkens een nieuwe http request te maken. waarschijnlijk zal de data in JSON's verstuurd worden

De backend  zal in flask of django worden geprogrammeerd met toegang tot sql databases om metingen van de arduino op te slaan.
de frontend zal in html/css worden geprogrammeerd met interactie in javascript.



