in dit bestand wordt er teruggkeken op  de kwaliteit van de code.
Wat kon er beter en waar kon het netter? Welke functionaliteit ontbreek er nog en hoe zou dit gemaakt moeten worden?
Eerst wordt de peerreview gegeven door Luitzen de Vries en mijn reacties hierop weergegeven.
Daarna heb ik mijn eigen verbeterpunten opgesomt.

__Peer review Luitzen de Vries__
1. wat gebeurt er wanneer je bij het registreren een heel simpel wachtwoord aanmaakt, bijvoorbeeld van 1 teken. 
martijn: 
dan werkt dit ook nog. Dit is natuurlijk voor een productieversie niet wenselijk en hier had nog veel functionaliteit bijgekunt. Je wilt dat het wachtwoord lang genoeg moet zijn, liefst een cijfer en leesteken bevat en niet (deels) overeenkomt met de gebruikersnaam. Wanneer ik deze functionaliteit zou toevoegen zou ik eerst op internet gaan speuren of een library of bestaand programma dit zou kunnen vergemakkelijken zodat dit niet allemaal gehardcoded hoeft te worden. Voor nu heb ik de functionaliteit vanuit books gekopieerd.

2.  Ik zie nog een aantal print statements, was dit de bedoeling? Martijn: deze ben ik vergeten weg te halen.

3.  Ik zie veel javascript in je paginas staan,  heb je opzettelijk ervoor gekozen om dit hier te zetten? Martijn: ik had hier inderdaad voor gekozen  zodat in de header van het template niet telkens alle scripts van de gehele app hoeven te worden geladen voor een specifieke pagina. na samen is te hebben gekekeken kreeg ik de feedback van Luitzen dat dit wel kon doormidel van een {block script} in de header. dit was wel netter geweest.

__eigen verbeterpunten__
met wat meer tijd had ik de volgende functionaliteit nog willen toevoegen:
1. een sid bij de metingen op eenzelfde manier als bij de controllers. nu kunnen gaan er waarschijnlijk problemen ontstaan als 2 gebruikers meten met dezelfde naam van de meting.
2. het lukte me niet om alle prullebakjes van kleur te laten veranderen wanneer er over gehoverd wordt. de oorzaak van dit probleem heb ik nog niet achterhaald.
3. Door een klein typefoutje in de pagina controller.html worden controllers van type 'execute code' niet weergegeven.  in het if statement van jinja  om deze controller weer te gegeven staat 'execute' ipv 'execute code'.
4. de pagina setup had nog wel wat mooier gekund en vooral de tekst, die had beter met een margin vanaf de zijkant van het scherm kunnen worden weergegeven. 
5. een bug die ik nog niet heb  opgelost is dat wanneer bij de controller pagina eerst een slider en dan een toggle worden neergezet, dat deze twee controllers niet op dezelfde hoogte staan. 

