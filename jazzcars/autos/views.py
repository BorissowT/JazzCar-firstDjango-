from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

cars = [
    {   'id':1,
        'title': 'Mazda Cosmo Sports',
        'year': 1967,
        'category': {"Schnell", "Cool"},
        'Motor': 'Otto-Wankel:1,0 Liter (81 kW, 94 kW)',
        'info': 'Der Mazda 110 S Cosmo Sport wurde von 1967 bis 1972 gebaut. Er war der erste Serienwagen mit einem Zweischeiben-Wankelmotor. Der Wagen wurde 1176-mal gebaut, ausschließlich als Rechtslenker.Es handelte sich um ein zweisitziges Coupé, dessen Karosserie zu großen Teilen und dessen Motor aus Aluminium besteht.Ab 1968 wurde es bei 1 cm geringerer Gesamtlänge mit 15 cm längerem Radstand gebaut.Mazda Cosmo Sport, Heckansicht.Das Cosmo-Projekt wurde im Dezember 1962 von Mazda gestartet. Mazda stellte den ersten Zweischeibenmotorprototyp im Juli 1963 fertig. Der erste fahrbare Prototyp des Cosmo Sport wurde im August 1963 fertiggestellt. Dieser wurde im Oktober 1963 auf der Tokyo Motorshow, unter dem Titel "Projekt L402A", vorgestellt.Der Prototypmotor L8A hatte ein Kammervolumen von 2 × 398 cm³. Beim L8A setzte man noch kombinierte Seiten- und Umfangseinlässe ein. Der L8A wurde zum L10A weiterentwickelt und das Kammervolumen auf 2 × 491 cm³ vergrößert. Die Umfangseinlässe entfielen und wurden durch zwei zusätzliche Seiteneinlässe in dem Vorder- und Endteil des Motors ersetzt. Dies verbesserte das Drehmoment und die Fahrbarkeit bei niedrigen Drehzahlen. Der L10A hatte eine Motorleistung von 110 PS (81 kW). Die Weiterentwicklung L10B verfügte über das gleiche Kammervolumen wie der L10A, durch geänderte Steuerzeiten hatte man die Leistung des Motors auf 128 PS (94 kW) gesteigert. Damit beschleunigte der Cosmo Sport in 8,8 s auf 100 km/h und erreichte 200 km/h.[1][3]Im April 1966 stellte Mazda 80 Vorserien-Cosmo Sport her, davon lieferte man 60 Stück an Händler in Japan zur Felderprobung aus. Von der ersten Serienversion mit dem Motor L10A (30. Mai 1967 bis Juli 1968) wurden 343 Stück hergestellt. Die zweite Serienversion mit dem L10B (13. Juli 1968 bis September 1972) wurde 833-mal gebaut. Somit wurden insgesamt 1176 Serienfahrzeuge (ca. 1256 mit Vorserienfahrzeugen mitgerechnet) des Typs Cosmo Sport hergestellt. Der Cosmo Sport wurde ausschließlich in Japan verkauft. Etwa 36 Fahrzeuge wurden unter der Bezeichnung "110 S" offiziell exportiert, davon 11 Fahrzeuge nach Europa. Ein 1970 Mazda Cosmo Sport Series II L10B Coupe wurde im Januar 2015 für US$ 110.000 inklusive Aufgeld in den USA auf einer Auktion von Bonhams verkauft ',
        'picture': "https://i.pinimg.com/originals/c0/1a/79/c01a79491e034d85484487c7d1c01fd3.jpg"
    },
    {   'id':2,
        'title': 'Mazda Eunos 100',
        'year': 1989,
        'category': {"Schnell","Cool", "Billig"},
        'Motor': '1,5 Liter ',
        'picture':'https://s.auto.drom.ru/i24208/c/photos/fullsize/mazda/eunos_100/mazda_eunos_100_707979.jpg',
        'info':"Eunos (japanisch: ユーノス; gesprochen [ju:nos]) war eine japanische Automobilmarke des Automobilherstellers Mazda. Die Marke bestand von 1989 bis 1996 und war lediglich auf den Märkten Australiens, Japans und den ASEAN-Staaten vertreten. Anwendung fand der Markenname für Modelle und Modellvarianten mit gehobener Ausstattung."
    },
    {   'id':3,
        'title': 'Mazda CX-5',
        'year': 2011,
        'category': {"Gross", "Billig"},
        'Motor': 'Ottomotoren: 2,0–2,5 Liter (118–141 kW) Dieselmotoren: 2,2 Liter (110–129 kW)',
        'picture': 'https://s.auto.drom.ru/i24208/c/photos/fullsize/mazda/cx-5/mazda_cx-5_708027.jpg',
        'info':"""  Der MX-5 ist vom Konzept her eine Evolution der kleinen britischen und italienischen Sportwagen der 1960er wie z. B. der Triumph Spitfire, MG MGB, Fiat 124 Sport Spider, Alfa Romeo Spider und besonders der Lotus Elan. Vor der Vorstellung des MX-5 im Jahre 1989 war die Bauform des klassischen Roadsters aufgrund ständig verschärfter Sicherheitsbestimmungen und erheblicher Probleme mit der Zuverlässigkeit so gut wie ausgestorben. Einige Hersteller produzierten Fahrzeuge mit herausnehmbaren Dachteilen (Targa). Der einzige noch in Großserie gebaute Vertreter der Gattung der klassischen Roadster war der Alfa Romeo Spider, der jedoch aufgrund seiner langen Bauzeit technisch veraltet war.

                    Da die Marktforschungsabteilungen des Automobilkonzerns kein Potenzial für ein solches Fahrzeug sahen, ist es zu großen Teilen der persönlichen Initiative vieler Entwickler, wie dem MX-5 Projektleiter Toshihiko Hirai, zu verdanken, dass der Wagen dennoch in Serie ging. Bei Markteinführung soll eine Produktion von lediglich 5.000 Fahrzeugen im Jahr geplant worden sein, davon 3.000 für die USA und 500 für Europa.[2] Aber schon bis Ende 1990 waren 140.918 Fahrzeuge produziert worden. Die 15.888 Fahrzeuge, die davon auf Europa entfielen, konnten die hiesige Nachfrage jedoch bei weitem nicht decken. Das für Deutschland bestimmte Kontingent war in nur drei Tagen ausverkauft, was zu einer großen Anzahl von Grauimporten aus den USA und Kanada, nicht nur nach Deutschland, führte.

                    Der MX-5 wurde mit besonderem Blick auf den kalifornischen Markt entwickelt. So soll sich der Gedanke zur Entwicklung eines Roadsters ursprünglich in einem Gespräch zwischen dem Mazda-Manager Kenichi Yamamoto und dem amerikanischen Journalisten Bob Hall entwickelt haben, der auf Yamamotos Frage, welches Mazda-Fahrzeug auf dem nordamerikanischen Markt besonders fehlte, geantwortet haben soll: „A lightweight sportscar“. Man erhoffte sich von dem Wagen eine emotionale Besetzung des Markennamens Mazda; eine Strategie, die im Nachhinein wohl als erfolgreich bezeichnet werden kann.

                    Andere Hersteller zogen später mit eigenen Roadster-Modellen nach, so zum Beispiel BMW mit dem Z3, Mercedes mit dem SLK, MG mit dem MG F, Toyota mit der dritten Generation des MR2 und Fiat mit der Barchetta. Während die im Preissegment des MX-5 angesiedelten Konkurrenten praktisch ausnahmslos ohne Nachfolger eingestellt wurden, hat sich der Markt für höherpreisige, meist verhältnismäßig komfortbetonte Roadster seitdem zu einer festen Größe entwickelt."""
    },
    {   'id':4,
        'title': 'BMW E21',
        'year': 1975,
        'category': {"Billig","Cool"},
        'Motor': 'Ottomotoren: 1,6–2,3 Liter(55–105 kW)',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/BMW_E21_%283er%29.jpg/1920px-BMW_E21_%283er%29.jpg',
        'info':"""Das Design des E21 stammt von Paul Bracq, der davor bereits den ersten 5er BMW E12 gezeichnet hatte. Die ersten Modelle des E21 wurden noch ohne die schwarze Kunststoffblende zwischen den Heckleuchten ausgeliefert. Kundenproteste wegen des kargen Hecks (beim Vorgänger war noch das Kennzeichen zwischen den Leuchten montiert) veranlassten BMW, vier Monate nach dem Produktionsanlauf im August 1975 eine geriffelte Heckblende in die Serie einzuführen.

                Die Fahrzeuge mit den „kleinen“ Vierzylinder-Motoren (315, 316, 318 und 318i) unterscheiden sich auch äußerlich von den Varianten 320, 320i und 323i. So haben die kleineren Typen einzelne Rundscheinwerfer von 7" (ca. 178 mm) Durchmesser, die je nach Modellversion und Baujahr teils mit R2-Zweifadenlampen oder H4-Halogenlampen ausgerüstet sind. Die Modelle ab BMW 320 sind mit zwei 5 3/4" (ca. 146 mm) großen Rundscheinwerfern ausgestattet, die Sechszylindermodelle erkennt man am Typenschild im Kühlergrill. Der BMW 323i mit der K-Jetronic-Saugrohreinspritzung ist als einzige Variante mit zwei Auspuffendrohren ausgestattet links und rechts am Fahrzeugheck. Das „i“ hinter der Zahlenkombination stand für „injection“, also Saugrohreinspritzung – Modelle ohne „i“ waren mit Vergaser ausgerüstet.

                Im September 1978 fiel die schwarze Grundfläche unter dem Chrom-Typenschild weg. Die noch aus dem BMW 02 übernommenen Vordersitze wurden durch Neukonstruktionen ersetzt, bei denen unter anderem die Gurtschlösser am Sitzrahmen befestigt sind. Der Auspuff der Modelle 316 bis 320 wurde weiter vom Kennzeichen weg an die Stelle des linken 323i-Auspuffs verlegt. """
    },
    {   'id':5,
        'title': 'BMW E12',
        'year': 1972,
        'category': {"Billig", "Gross"},
        'Motor': 'Ottomotoren: 1,8–3,5 Liter (66–160 kW)',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/BMW_528_%28E12%29_%E2%80%93_Frontansicht%2C_22._August_2013%2C_M%C3%BCnster.jpg/1920px-BMW_528_%28E12%29_%E2%80%93_Frontansicht%2C_22._August_2013%2C_M%C3%BCnster.jpg',
        'info':"""Der BMW mit Werkscodebezeichnung E12 ist der erste BMW der 5er-Reihe, das Nachfolgemodell der „Neuen Klasse“, und wurde von Sommer 1972 bis Mitte 1981 produziert.

            Mit ihm leitete BMW eine Neuordnung der Modellbenennung ein. Die erste 5er-Reihe wurde nur als viertürige Stufenhecklimousine angeboten.

            Die Plattform übernahm BMW im Wesentlichen von der Neuen Klasse: Frontmotor und Hinterradantrieb, einzeln aufgehängte Räder – Vorderräder an MacPherson-Federbeinen und Querlenkern, die hinteren an leicht angestellten Schwingen („Schräglenkerachse“) – Zahnstangenlenkung und hydraulisch betätigte Bremsen (an der Vorderachse Scheibenbremsen, hinten Trommelbremsen)"""
    },
    {   'id':6,
        'title': 'Alfa Romeo 155',
        'year': 1992 ,
        'category': {'Billig'},
        'Motor': 'Ottomotoren: 1,6–2,5 Liter (85–140 kW) Dieselmotoren: 1,9–2,5 Liter (66–92 kW)',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/2/20/Alfa_Romeo_155_%28photo_by_Serge_Zinnsee%29.jpg',
        'info':"""Im Gegensatz zum hinterradangetriebenen Vorgänger Alfa 75 hat der Alfa 155 Frontantrieb mit quer eingebautem Motor. Einzige Ausnahme ist die Q4-Version, die wie das Rennfahrzeug vierradangetrieben ist und einen Vierzylinder-Reihenmotor mit Turboaufladung hat. Der 155 basiert auf der Tipo-Plattform. Fiat verwendete sie in mehreren Modellen, teils im Detail je nach Modell und Motorisierung angepasst: Tipo (Typ 160) („Ursprungsplattform“), Fiat Tempra, Fiat Coupé, Bravo, Brava, Marea, Multipla, Lancia Delta II und Dedra sowie Alfa Romeo 145, 146, Alfa Romeo 155, Spider und GTV und etwas modifiziert auch noch beim 155-Nachfolger Alfa Romeo 156. Für die Motorvarianten V6 und Q4 war der 155 auch mit einem elektronisch geregelten Dämpfersystem mit zwei Einstellungen (automatisch und Sport) erhältlich.

        Die viertürige Stufenheckkarosserie des 155 wurde von dem Turiner Designstudio I.DE.A Institute entworfen; verantwortlicher Designer war Ercole Spada."""
    },
    {   'id':7,
        'title': 'GAZ-24 Wolga',
        'year': 1967,
        'category': {'Gross'},
        'Motor': 'Ottomotoren: 2,45–5,6 Liter (62,5–145 kW)',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/GAZ-24_%284936806269%29.jpg',
        'info':"""Das Fahrzeug ist mit einer selbsttragenden Karosserie aufgebaut. Der Motor sitzt über der Vorderachse auf einem Hilfsrahmen und treibt über eine Kardanwelle die Hinterachse an. Die Vorderachse ist mit Doppelquerlenkern und Schraubenfedern ausgestattet. Die Hinterachse ist als Starrachse mit Blattfedern ausgebildet. Schräg angeordnete Stoßdämpfer unterdrücken die Federschwingungen und dämpfen Querbewegungen der Achse. Die Fußbremse wirkt hydraulisch in einem Zweikreisbremssystem mit Duplextrommelbremsen an der Vorderachse und Simplextrommelbremsen an der Hinterachse. Zur Bremskraftverstärkung ist ein Unterdruck-Bremskraftverstärker vorhanden. Die Handbremse wirkt auf die Hinterachse."""
    },
    {   'id':8,
        'title': 'RX-7 ',
        'year': 1992,
        'category': {'Schnell', "Cool"},
        'Motor': 'Otto-Wankel:1,3 Liter (176–206 kW)',
        'picture': 'https://i2.wp.com/www.jdmbuysell.com/wp-content/uploads/2020/01/1992-mazda-rx-7-10.jpeg?fit=705%2C436&ssl=1',
        'info':"""Der RX-7 (Code: FD) stellte die konsequente Weiterentwicklung zum Vorgänger dar. Mit einem erneut verbesserten und immer noch turbogeladenen 13B-REW-Wankelmotor wurde in der letzten Ausbaustufe eine Leistung von 206 kW (280 PS) bei 6500/min und ein maximales Drehmoment von 314 Nm bei 5000/min erreicht.

        Der FD war das leistungsstärkste Modell aus der RX-7-Reihe und überzeugte mit besonderen Details wie einer üppig dimensionierten Bremsanlage und Schalensitzen.

        In Deutschland wurde dieser RX-7 nur von Frühjahr 1992 bis Anfang 1996 angeboten, ehe neue Abgasvorschriften den Verkauf von Neuwagen dieses Typs unmöglich machten. Unter anderem führte der damals relativ hohe Neupreis ab 85.000 DM dazu, dass nur wenige Fahrzeuge in Deutschland verkauft wurden."""
    },
    {   'id':9,
        'title': 'Mercedes-Benz G-Klasse ',
        'year': 2012,
        'category': {'Gross'},
        'Motor': '5,5-Liter-V8-Biturbo',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Mercedes-Benz_G_300_CDI_Professional_%28W_461%29_%E2%80%93_Frontansicht%2C_7._August_2012%2C_Stuttgart.jpg/1920px-Mercedes-Benz_G_300_CDI_Professional_%28W_461%29_%E2%80%93_Frontansicht%2C_7._August_2012%2C_Stuttgart.jpg',
        'info':"""Am 30. Juni 2012 erfolgte eine weitere Modellpflege, die insbesondere einen stark überarbeiteten Innenraum mit sich brachte. Während am Exterieur nun alle W 463-Modelle über LED-Tagfahrlicht, das unterhalb der Scheinwerfer angebracht ist, verfügen und neu gestaltete Seitenspiegel erhielten, gab es im Interieur eine gänzlich neu gestaltete Mittelkonsole und Instrumententafel. Letztere stammt aus dem ML (W 166). Als Antrieb dienten auf der einen Seite die bekannten Triebwerke im G 350 BlueTEC und G 500, auf der anderen Seite kamen zwei neue AMG-Modelle hinzu, womit der G 55 AMG abgelöst wurde. Der 5,5-Liter-V8-Biturbo im G 63 AMG leistet 400 kW (544 PS), der G 65 AMG mit einem sechs Liter großen V12-Biturbo-Ottomotor 450 kW (612 PS). Ebendiese AMG-Modelle unterscheiden sich von den herkömmlichen Modellen durch einen Zweilamellen-Grill und durch Stoßfänger mit größeren Lufteinlässen. Auch auf technischer Seite wurde die G-Klasse überarbeitet, so dass die 7G-Tronic Plus, beim G 63 AMG mit Start-Stopp-Automatik, und das Infotainmentsystem Comand Online mit Navigationssystem und Internetzugang serienmäßig ist sowie außerdem zahlreiche Assistenzsysteme erhältlich sind.

        Zur Produktionseinstellung des Cabriolets Ende 2013 wurde Mitte 2013 die auf 200 Exemplare limitierte Final Edition 200 eingeführt, die obligatorisch mit einem beigefarbenen Verdeck ausgestattet ist. Vor der Premiere auf der IAA 2013 waren bereits alle Einheiten verkauft. Als Motor war ausschließlich der G 500 verfügbar."""
    },
    {   'id':10,
        'title': 'Streetscooter GmbH',
        'year': 2017,
        'category': {"Umweltfreundlich", "Gross"},
        'Motor': '68 kW (92 PS)',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Streetscooter_Seitenansicht.jpg/1280px-Streetscooter_Seitenansicht.jpg',
        'info':"""Maximale Flexibilität für maximale Individualität; ­
                    das ist das Prinzip, auf dem die maßgeschneiderten
                    Aufbaulösungen des WORK L Pure basieren.
                    Gemeinsam mit unseren Partnern haben wir eine Vielzahl unterschiedlicher Aufbauvarianten für verschiedene Einsatzzwecke entwickelt. Die Fahrerkabine des WORK L Pure bietet ausreichend Platz für 2 Personen und die pragmatische Ergonomie aller StreetScooter-­Modelle."""
    },
    {   'id':11,
        'title': 'Rimac Concept_One',
        'year': 2013,
        'category': {"Schnell", "Umweltfreundlich", "Gross"},
        'Motor': '900 kW',
        'picture': 'https://cdn.autocentre.ua/wp-content/uploads/2017/03/concept_one_dyncamic_env_02.jpg',
        'info':"""Das Concept_One wurde erstmals auf der Internationalen Automobil-Ausstellung 2011 in Frankfurt am Main und auf der Pariser Autosalon 2012 in Paris präsentiert. Ein Auto wurde bereits im Januar 2013 an einen spanischen Kunden ausgeliefert. Bis Oktober 2014 wurden acht Fahrzeuge verkauft. Das Concept_One soll 980.000 US-Dollar kosten,es sollen nur 88 Fahrzeuge hergestellt werden.

        Der Concept_One war das offizielle Nullemissionsfahrzeug des Renndirektors der FIA-Formel-E-Meisterschaft 2014/15. Der Renndirektor prüfte damit unter anderem vor Rennbeginn die Rennstrecke.

        Im Jahr 2015 nahm Rimac mit einem 1 Megawatt starken Elektrofahrzeug am Pikes-Peak-Rennen teil. Das Fahrzeug belegte den zweiten Platz über alle Klassen. Fahrer war der mehrfache Pikes-Peak-Gewinner Nobuhiro Tajima. Auf den ersten Platz im Gesamtklassement fuhr ebenfalls ein Elektroauto.[10]

        Das Auto wurde beständig weiterentwickelt. Auf dem Genfer Auto-Salon 2016 wurde die finale Versionund bereits die Nachfolgeversion Rimac Concept_S präsentiert.

        Im Rahmen der Dreharbeiten zur Amazon-Prime-Show The Grand Tour wurde ein Prototyp am 10. Juni 2017 von Richard Hammond, einem der drei Moderatoren, zerstört. Dieser verlor am Ende eines Demonstrationslaufs beim Hemberger Bergrennen aus noch ungeklärter Ursache die Kontrolle über das Fahrzeug und überschlug sich. Hammond konnte sich aus dem Wagen selbstständig befreien und erlitt eine Verletzung am Knie; kurz darauf ging das Fahrzeug in Flammen auf."""
    },
    {   'id':12,
        'title': 'Twike',
        'year': 1996 ,
        'category': {"Cool", "Umweltfreundlich"},
        'Motor': 'Elektromotor: 5,0 kW',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Twike.jpg',
        'info':"""Das Twike (Eigenschreibweise „TWIKE“) ist ein dreirädriges Leichtelektromobil für zwei Personen. Es war nach dem CityEL eines der meistverkauften Elektrofahrzeuge in Europa und wurde ab 2013 von Renault ZOE überholt.

                Das Twike ging aus einer Studie von Studenten unter anderem der ETH Zürich hervor. Ursprünglich war es als reines vollverkleidetes Fahrrad (Muskelkraftfahrzeug) konzipiert. 1986 gewann es während der Weltausstellung in Vancouver anlässlich der Innovative Vehicle Design Competition (IVDC) einen Preis für Ergonomie sowie während der Human Powered Vehicle World Championships den ersten Preis in der Kategorie Alltagsfahrzeuge."""
    },
    ]

class MainView(View):
    def get(self, request, cars=cars, *args, **kwargs):
        return render(
            request, 'autos/main.html', context={
                'cars': cars
            }
        )
class CategoryView(View):
    def get(self, request, cars=cars, category="Schnell", *args, **kwargs):
        return render(
            request, 'autos/category.html', context={
                'cars': cars, 'pagename': category
            }
        )

class CarView(View):
    def get(self, request, cars=cars, id=1, *args, **kwargs):
        for carr in cars:
            if carr["id"] == id:
                car=carr
                break
        return render(
            request, 'autos/car.html', context={
                'car': car, 'pagename': car['title']
            }
        )