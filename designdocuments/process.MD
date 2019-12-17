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
verder gewerkt aan de app. Veel geleerd over javascript, eventlisteners en innerhtml om dynamische content te laten zien. dit was al eerder langsgekomen bij books maar werd nu wat duidelijker. en hoe je functies in functies maakt (=>)
aan het einde van de dag was de alphaversie nog niet ver genoeg, er konden nog geen control buttons worden toegevoegd. 

__6-12__
De alpha versie afgemaakt. er zijn nu twee soorten control buttons: toggle switch en slider , welke kunnen worden toegevoegd, waarbij ook de juiste pin wordt aangegeven. alleen verstuurd de websocket in de json nog niet de juiste data naar de controller, idealiter wordt dit zoveel mogelijk regels code die gelijk kunnen worden uitgevoerd, zodat dat de gebruiker het programma voor de controller niet moet bijwerken wanneer nieuwe opties worden toegevoegd. daarnaast een tabel gemaakt om de controllers op te slaan. er ontstond nog een error: na het bijwerken van de database doormiddel van het bestand create.py deed 'flask run' het niet meer. op stackoverflow kwam ik er uiteindelijk achter dat het kwam doordat ik twee keer een app had gecreeerd, een in application.py en een in create.py. ik heb vervolgens create.py geimporteerd in application.py en vervolgens in application.py de regel "app = Flask(__name__)" verwijdered.

__7-12__
Aan de meetpagina begonnen. geleerd hoe de uitbreiding chart.js werkt. Live data gestreamd vanaf een client programma.

__9-12__
verder gegaan aan de measurement pagina en de record functie gemaakt. geleerd hoe je een csv bestand stuurt en hoe je deze vervolgens in  de zelfde functie verwijdert. dit bleek best lastig doordat wanneer je functie stuurt je hem niet kan verwijderen. de  oplossing bleek om het bestand te kopieren in het tijdelijk geheugen en vervolgens te verwijderen. 

__10-12__
voor het eerst de raspberry aangestuurd via de app. alles werkte behoorlijk goed. het lukte om een ledje aan en uit te laten gaan, code te excecuten en een servostand te veranderen.  geleerd hoe je doormiddel van  een  doorgegeven string een variabele aanroept. dit  doe je doormiddel van een dictionary. als je bijvoorbeeld GPIO.OUT wil callen maar je krijgt de string "GPIO.OUT" binnen, dan kun je deze variabele aanroepen doormiddel van de dictionary  dict = {"GPIO.OUT": GPIO.OUT}.
verder geleerd over hoe je een servo aanstuurt met de raspberry pi. dit  gebeurt door een varierend PWM signaal, en dit is precies wat de slider controller gaat doen. de duty cycle , de verhouding tusen pulsduur en de periode. bij servos zit deze vaak tussen de 2% en 15%. het idee is dat de gebruiker de pulsduur aangeeft en dat hierdoor vervolgens het juiste signaal bij de actuator uitkomt. dit is ook gelukt.  

__11-12__
 geleerd hoe je met javascript de class aanpast van een html element, om zo de css dynamisch te maken. dit heb ik gebruikt om een record functie te maken. 

__12-12__
geleerd hoe je div containers in een dynamisch grid plaatst dat ook van dimensies meeveranderd. doormiddel van de css display: flex;
flex-wrap: wrap;. max-width: 100%;. 

__13-12__
 de volgende belangrijkste bugs tegengekomen en opgelost:
- /download/application.py zou de flask applicatie sturen en hem vervolgens verwijderen. daarom heb ik code toegevoegd waardoor het aangevraagde downloadbestand een .csv bestand is. dit kan je door de volgende regel code checken:
__if not fnmatch.fnmatch(filename, '*.csv'):__
- wanneer forms niet volledig worden ingevoerd ontstaat er een error.

__16-12__
code  netjes gemaakt en aan opmaak gewerkt
