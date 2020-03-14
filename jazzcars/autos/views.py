from django.conf import settings
from django.shortcuts import render
from django.views import View


cars = [
    {
        'title': 'Mazda Cosmo Sports',
        'year': 1967,
        'category': {"Schnell", "Cool"},
        'Motor': 'Otto-Wankel:1,0 Liter (81 kW, 94 kW)',
        'info': 'Der Mazda 110 S Cosmo Sport wurde von 1967 bis 1972 gebaut. Er war der erste Serienwagen mit einem Zweischeiben-Wankelmotor. Der Wagen wurde 1176-mal gebaut, ausschließlich als Rechtslenker.Es handelte sich um ein zweisitziges Coupé, dessen Karosserie zu großen Teilen und dessen Motor aus Aluminium besteht.Ab 1968 wurde es bei 1 cm geringerer Gesamtlänge mit 15 cm längerem Radstand gebaut.Mazda Cosmo Sport, Heckansicht.Das Cosmo-Projekt wurde im Dezember 1962 von Mazda gestartet. Mazda stellte den ersten Zweischeibenmotorprototyp im Juli 1963 fertig. Der erste fahrbare Prototyp des Cosmo Sport wurde im August 1963 fertiggestellt. Dieser wurde im Oktober 1963 auf der Tokyo Motorshow, unter dem Titel "Projekt L402A", vorgestellt.Der Prototypmotor L8A hatte ein Kammervolumen von 2 × 398 cm³. Beim L8A setzte man noch kombinierte Seiten- und Umfangseinlässe ein. Der L8A wurde zum L10A weiterentwickelt und das Kammervolumen auf 2 × 491 cm³ vergrößert. Die Umfangseinlässe entfielen und wurden durch zwei zusätzliche Seiteneinlässe in dem Vorder- und Endteil des Motors ersetzt. Dies verbesserte das Drehmoment und die Fahrbarkeit bei niedrigen Drehzahlen. Der L10A hatte eine Motorleistung von 110 PS (81 kW). Die Weiterentwicklung L10B verfügte über das gleiche Kammervolumen wie der L10A, durch geänderte Steuerzeiten hatte man die Leistung des Motors auf 128 PS (94 kW) gesteigert. Damit beschleunigte der Cosmo Sport in 8,8 s auf 100 km/h und erreichte 200 km/h.[1][3]Im April 1966 stellte Mazda 80 Vorserien-Cosmo Sport her, davon lieferte man 60 Stück an Händler in Japan zur Felderprobung aus. Von der ersten Serienversion mit dem Motor L10A (30. Mai 1967 bis Juli 1968) wurden 343 Stück hergestellt. Die zweite Serienversion mit dem L10B (13. Juli 1968 bis September 1972) wurde 833-mal gebaut. Somit wurden insgesamt 1176 Serienfahrzeuge (ca. 1256 mit Vorserienfahrzeugen mitgerechnet) des Typs Cosmo Sport hergestellt. Der Cosmo Sport wurde ausschließlich in Japan verkauft. Etwa 36 Fahrzeuge wurden unter der Bezeichnung "110 S" offiziell exportiert, davon 11 Fahrzeuge nach Europa. Ein 1970 Mazda Cosmo Sport Series II L10B Coupe wurde im Januar 2015 für US$ 110.000 inklusive Aufgeld in den USA auf einer Auktion von Bonhams verkauft ',
        'picture': "https://i.pinimg.com/originals/c0/1a/79/c01a79491e034d85484487c7d1c01fd3.jpg"
    },
    {
        'title': 'Mazda Eunos 100',
        'year': 1989,
        'category': {"Schnell","Cool", "Billig"},
        'Motor': '1,5 Liter ',
        'picture':'https://s.auto.drom.ru/i24208/c/photos/fullsize/mazda/eunos_100/mazda_eunos_100_707979.jpg',
        'info':"Eunos (japanisch: ユーノス; gesprochen [ju:nos]) war eine japanische Automobilmarke des Automobilherstellers Mazda. Die Marke bestand von 1989 bis 1996 und war lediglich auf den Märkten Australiens, Japans und den ASEAN-Staaten vertreten. Anwendung fand der Markenname für Modelle und Modellvarianten mit gehobener Ausstattung."
    },
    {
        'title': 'Mazda CX-5',
        'year': 2011,
        'category': {"Cool", "Billig"},
        'Motor': '1,5 Liter ',
        'picture': 'https://s.auto.drom.ru/i24208/c/photos/fullsize/mazda/cx-5/mazda_cx-5_708027.jpg',
        'info':"""  Der MX-5 ist vom Konzept her eine Evolution der kleinen britischen und italienischen Sportwagen der 1960er wie z. B. der Triumph Spitfire, MG MGB, Fiat 124 Sport Spider, Alfa Romeo Spider und besonders der Lotus Elan. Vor der Vorstellung des MX-5 im Jahre 1989 war die Bauform des klassischen Roadsters aufgrund ständig verschärfter Sicherheitsbestimmungen und erheblicher Probleme mit der Zuverlässigkeit so gut wie ausgestorben. Einige Hersteller produzierten Fahrzeuge mit herausnehmbaren Dachteilen (Targa). Der einzige noch in Großserie gebaute Vertreter der Gattung der klassischen Roadster war der Alfa Romeo Spider, der jedoch aufgrund seiner langen Bauzeit technisch veraltet war.

                    Da die Marktforschungsabteilungen des Automobilkonzerns kein Potenzial für ein solches Fahrzeug sahen, ist es zu großen Teilen der persönlichen Initiative vieler Entwickler, wie dem MX-5 Projektleiter Toshihiko Hirai, zu verdanken, dass der Wagen dennoch in Serie ging. Bei Markteinführung soll eine Produktion von lediglich 5.000 Fahrzeugen im Jahr geplant worden sein, davon 3.000 für die USA und 500 für Europa.[2] Aber schon bis Ende 1990 waren 140.918 Fahrzeuge produziert worden. Die 15.888 Fahrzeuge, die davon auf Europa entfielen, konnten die hiesige Nachfrage jedoch bei weitem nicht decken. Das für Deutschland bestimmte Kontingent war in nur drei Tagen ausverkauft, was zu einer großen Anzahl von Grauimporten aus den USA und Kanada, nicht nur nach Deutschland, führte.

                    Der MX-5 wurde mit besonderem Blick auf den kalifornischen Markt entwickelt. So soll sich der Gedanke zur Entwicklung eines Roadsters ursprünglich in einem Gespräch zwischen dem Mazda-Manager Kenichi Yamamoto und dem amerikanischen Journalisten Bob Hall entwickelt haben, der auf Yamamotos Frage, welches Mazda-Fahrzeug auf dem nordamerikanischen Markt besonders fehlte, geantwortet haben soll: „A lightweight sportscar“. Man erhoffte sich von dem Wagen eine emotionale Besetzung des Markennamens Mazda; eine Strategie, die im Nachhinein wohl als erfolgreich bezeichnet werden kann.

                    Andere Hersteller zogen später mit eigenen Roadster-Modellen nach, so zum Beispiel BMW mit dem Z3, Mercedes mit dem SLK, MG mit dem MG F, Toyota mit der dritten Generation des MR2 und Fiat mit der Barchetta. Während die im Preissegment des MX-5 angesiedelten Konkurrenten praktisch ausnahmslos ohne Nachfolger eingestellt wurden, hat sich der Markt für höherpreisige, meist verhältnismäßig komfortbetonte Roadster seitdem zu einer festen Größe entwickelt."""
    },

    ]

class MainView(View):
    def get(self, request, cars=cars, *args, **kwargs):
        return render(
            request, 'autos/main.html', context={
                'cars': cars
            }
        )