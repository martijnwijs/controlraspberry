__2-12__
ontdekt dat een websocket in arduino vrij beperkt is en dat het ook geen echte websocket is.
daarom besloten het project te veranderen in het aansturen van een raspberry pi. een raspberry pi gekocht en geinstalleerd. aangesloten op monitor
ik wist nog vrij weinig van de PI dus vandaag wat basisdingen geleerd.
__3-12__
eerst geleerd hoe de gpio library werkt in python om een led licht te laten branden op de raspberry. geleerd over de verschillende pins, hoe je ze definieerd in je programma en aanstuurt.
vervolgens gezocht naar hoe ik een websocket verbinding kon krijgen tussen een python programma (op de raspberry pi) en de applicatie. hier kwam ik in eerste instantie moeilijk uit. Op youtube waren geen turtorials te vinden. ik besloot het voor die dag te laten.

Daarnaast was ik er nog niet uit of ik flask of django wilde gebruiken. de volgende afwegingen waren belangrijk:
- socket.io voor flask is een relatief simpele manier om socket connections te creeeren, django channels zijn wat moeilijker
- django heeft al functionaliteiten zoals login , en ook het beheersen van databases lijkt wat makkelijker, alhoewel je in flask ook doormiddel van OOP databases kunt maken, maar dit moet dan nog geleerd worden.
- django beter leren beheersen is voor eventuele latere projecten een mooie leersprong.

uiteindelijk heb ik toch voor flask gekozen. ik ging een turtorial volgen om een chatapplicatie in django te bouwen en zag dat het een stuk complexer in elkaar leek te zitten dan de flack opdracht met flask. 

__4-12__
gevraagd aan Simon over hoe ik dit probleem het best kon aanpakken. hij had al meer ervaring met websockets en vertelde over de libary socket.io for Python. Toen had ik vrij snel een socket verbinding gecreeerd met een flask applicatie en een python programma die naar beide kanten data kon versturen. verder de eerste control button geprogrammeerd (toggle switch), zowel front als backend.

__5-12__
verder gewerkt aan de app. Veel geleerd over javascript, eventlisteners en innerhtml om dynamische content te laten zien. dit was al eerder langsgekomen bij books maar werd nu wat duidelijker. en hoe je functies in functies maakt.
aan het einde van de dag was de alphaversie nog niet vergenoeg, er konden nog geen control buttons worden toegevoegd. 

__6-12__
De alpha versie afgemaakt. er zijn nu twee soorten control buttons: toggle switch en slider , welke kunnen worden toegevoegd, waarbij ook de juiste pin wordt aangegeven. alleen verstuurd de websocket in de json nog niet de juiste data naar de controller, idealiter wordt dit zoveel mogelijk regels code die gelijk kunnen worden uitgevoerd, zodat dat de gebruiker het programma voor de controller niet moet bijwerken wanneer nieuwe opties worden toegevoegd. daarnaast een tabel gemaakt om de controllers op te slaan. er ontstond nog een error: na het bijwerken van de database doormiddel van het bestand create.py deed 'flask run' het niet meer. op stackoverflow kwam ik er uiteindelijk achter dat het kwam doordat ik twee keer een app had gecreeerd, een in application.py en een in create.py. ik heb vervolgens create.py geimporteerd in application.py en vervolgens in application.py de regel "app = Flask(__name__)" verwijdered.
