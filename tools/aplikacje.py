"""Treści podstron aplikacji LeoKodum (generator: tools/strony_aplikacji.py).
status: test (test zamknięty, grupa testerów), sprawdzanie (u Google), wewnetrzny (testy
wewnętrzne, lista e-mail), przygotowanie. pakiet: identyfikator w Google Play (strona /testuj/). Zrzuty: ścieżki od katalogu repo, 9:16."""

GRUPA = "https://groups.google.com/g/testerzy-leokodum"
MAIL = "leokodum@mail.com"
TEL = "+48 884 322 324"
TEL_LINK = "+48884322324"


def zrzuty(katalog, pliki):
    return [(f"{katalog}/{p}", o) for p, o in pliki]


APLIKACJE = [
    {
        "slug": "opp-assist", "pakiet": "com.robsoft.oppassist", "nazwa": "OPP Assist", "tag": "Dla kierowców", "ikona": "ikona-opp.png?v=2",
        "status": "wewnetrzny",
        "krotko": "Pilnuje średniej prędkości na odcinkowym pomiarze prędkości.",
        "zrzuty": zrzuty("opp-assist/sklep", [
            ("1-ready.png", "Gotowy do jazdy, wybrany limit"), ("2-approach.png", "Sygnał przed odcinkiem"),
            ("3-auto.png", "Pomiar: średnia i ile wolno jechać do końca"), ("4-over.png", "Średnia powyżej limitu"),
            ("5-done.png", "Wynik po przejeździe"),
        ]),
        "wstep": "Pilnuje Twojej średniej prędkości na odcinkowym pomiarze prędkości (OPP). Sam rozpoznaje znane odcinki, daje sygnał przed wjazdem i podpowiada, z jaką prędkością możesz jechać do końca odcinka.",
        "sekcje": [
            ("Uczy się Twoich odcinków", [
                "Pierwszy przejazd zaznaczasz przyciskami START i STOP.",
                "Przy kolejnych aplikacja sama rozpoznaje odcinek, także kierunek jazdy, i mierzy średnią od wjazdu do wyjazdu.",
            ]),
            ("Sygnał przed odcinkiem", [
                "Około 10 sekund przed wjazdem na zapamiętany odcinek słyszysz sygnał, a przy wyjeździe inny.",
                "Dźwięki grają kanałem nawigacji, więc w samochodzie lecą przez głośniki.",
            ]),
            ("Limit z wyboru", [
                "Dopuszczalną prędkość wybierasz jednym dotknięciem, od 30 do 140 km/h.",
                "Średnia świeci na zielono albo na czerwono, a aplikacja podpowiada, ile możesz jechać do końca odcinka.",
            ]),
            ("Android Auto", [
                "Stan pomiaru, średnia i podpowiedź na ekranie samochodu.",
                "Po połączeniu z autem aplikacja pyta, czy ją uruchomić.",
            ]),
            ("Wspólna baza i kilka telefonów", [
                "Nowe odcinki są anonimowo udostępniane innym kierowcom (można to wyłączyć), a odcinki z okolicy możesz pobrać.",
                "Pokazywane są tylko odcinki potwierdzone przez co najmniej dwóch kierowców.",
                "Odcinki synchronizują się między Twoimi telefonami po wpisaniu wspólnego kodu.",
            ]),
        ],
        "uwaga": "Bez reklam, bez kont i logowania. Średnia jest liczona z prędkości GPS, więc nie skacze przy słabym sygnale. Aplikacja nie zastępuje uwagi kierowcy: zawsze przestrzegaj przepisów i znaków drogowych.",
    },
    {
        "slug": "mecz", "pakiet": "pl.leokodum.mecz", "nazwa": "Mecz", "tag": "Dla rodziców i trenerów", "ikona": "ikona-mecz.png?v=2",
        "status": "test", "poziome": True,
        "zrzuty": zrzuty("mecz/sklep", [
            ("1-nagrywanie.png", "Nagrywanie z przyciskami GOL i zegarem"), ("2-gol.png", "Po bramce: wynik miga, można cofnąć"),
            ("3-przerwa.png", "Zatrzymany zegar w przerwie"), ("4-gotowy-film.png", "Gotowy film z tablicą"),
        ]),
        "krotko": "Nagrywanie meczów telefonem z tablicą wyniku i czasem gry od razu w filmie.",
        "wstep": "Nagrywasz mecz telefonem, a nazwy drużyn, wynik i czas gry są wypalane w filmie na żywo. Po meczu nie trzeba nic montować.",
        "sekcje": [
            ("Tablica wyniku w filmie", [
                "Wpisujesz drużyny i wybierasz ich kolory, a nazwy zostają zapamiętane na kolejne mecze.",
                "Szeroki pasek u góry kadru: nazwy, wynik pośrodku i zegar meczu w rogu.",
                "Po bramce wynik przez chwilę miga, żeby było ją widać na nagraniu.",
            ]),
            ("Proste przyciski", [
                "GOL po lewej i po prawej dodaje bramkę gospodarzom albo gościom.",
                "Cofnij zdejmuje ostatnią bramkę, jeśli kliknąłeś za wcześnie.",
                "Zegar meczu włączasz i zatrzymujesz jednym dotknięciem, a przytrzymanie go zeruje, np. przed drugą połową.",
                "Nagrywanie ma osobny przycisk, niezależny od zegara.",
            ]),
            ("Tablica do nagranego wcześniej filmu", [
                "Wybierasz z galerii mecz nagrany bez tablicy i klikasz gole oraz zegar w chwilach, w których dzieją się na filmie.",
                "Aplikacja zapisuje nowy film z tablicą w każdej klatce, a oryginał zostaje.",
            ]),
            ("Gotowe pliki", [
                "Filmy trafiają do galerii, do folderu Mecze, z datą i nazwami drużyn w nazwie pliku.",
                "Działa bez internetu.",
            ]),
        ],
        "uwaga": "Najlepiej nagrywać w poziomie, z telefonem na statywie lub uchwycie.",
    },
    {
        "slug": "kafelki", "pakiet": "pl.leokodum.kafelki", "nazwa": "Kafelki", "tag": "Dla przedszkolaków", "ikona": "ikona-kafelki.png?v=2",
        "status": "test",
        "krotko": "Spokojna, wesoła gra dla dzieci w wieku 3–6 lat: kolory, kształty, liczenie i balony.",
        "wstep": "Spokojna, wesoła gra dla dzieci w wieku 3–6 lat. Pięć trybów zabawy, a w każdym kafelki z buziami, które kołyszą się i mrugają. Za postępy dziecko dostaje naklejki, rangi i awatary. Tu nie da się przegrać.",
        "zrzuty": zrzuty("kafelki/sklep", [
            ("1-menu-916.png", "Menu z pięcioma trybami"), ("2-lap-916.png", "Łap kafelki"),
            ("3-kolory-916.png", "Kolory"), ("4-liczenie-916.png", "Liczenie"),
            ("5-ksztalty-916.png", "Kształty"), ("6-balony-916.png", "Balony"),
        ]),
        "sekcje": [
            ("Pięć trybów zabawy", [
                "<strong>Łap kafelki:</strong> dotknięcie daje konfetti, gwiazdkę i dźwięk jak na cymbałkach, a szybkie łapanie gra melodię.",
                "<strong>Kolory:</strong> głos prosi „Znajdź niebieski!”, a pomyłka uczy nazwy koloru.",
                "<strong>Liczenie:</strong> cyfry dotykane po kolei, głos liczy razem z dzieckiem, od 3 do 10.",
                "<strong>Kształty:</strong> kółko, kwadrat, trójkąt, gwiazdka i serduszko.",
                "<strong>Balony:</strong> kolorowe balony z buziami do przebijania, zanim odlecą.",
            ]),
            ("Nagrody i postępy", [
                "Za każdy nowy poziom „BRAWO!”, fanfara, fajerwerki, tańczący lew i naklejka do albumu (40 do zebrania).",
                "10 rang do zdobycia, a za awans nowe awatary.",
                "Rekord poziomu w każdym trybie zabawy.",
            ]),
            ("Coraz ciekawiej", [
                "Trzy poziomy trudności na start: 🐢, 🐇 i 🚀.",
                "Z kolejnymi poziomami dochodzą nowe kolory i kształty, pływające kafelki, złote kafelki za 3 gwiazdki, odliczanie, a w Balonach wiatr.",
                "Gra sama dopasowuje tempo do dziecka.",
            ]),
            ("Dla rodzica", [
                "Bez reklam, bez zakupów w aplikacji, bez internetu.",
                "Nie zbiera żadnych danych.",
                "Wyjście z gry: przytrzymaj ✕, więc maluch nie wyjdzie przypadkiem.",
                "Pełny ekran, dotyk wieloma palcami (można grać we dwoje), działa na telefonach składanych.",
            ]),
        ],
        "uwaga": "Polecenia głosowe korzystają z polskiego syntezatora mowy w telefonie.",
    },
    {
        "slug": "test-iq", "pakiet": "pl.leokodum.testiq", "nazwa": "Test IQ na wesoło", "tag": "Dla dzieci i dorosłych", "ikona": "ikona-testiq.png?v=1",
        "status": "test",
        "krotko": "Łamigłówki ułożone jak w prawdziwym teście inteligencji, w trzech zeszytach wiekowych.",
        "wstep": "Łamigłówki ułożone jak w prawdziwym teście inteligencji. Każda dobra odpowiedź podnosi poziom trudności, a na końcu dostajesz wynik w skali IQ, krzywą wyników i profil zdolności.",
        "zrzuty": zrzuty("test-iq/sklep", [
            ("1-start.png", "Wybór zeszytu"), ("2-przedszkole.png", "Zeszyt Przedszkole"),
            ("3-szkola.png", "Zeszyt Szkoła"), ("4-dorosli.png", "Zeszyt Dorośli"),
            ("5-wynik.png", "Wynik i profil zdolności"), ("6-ciemny.png", "Ciemny motyw"),
        ]),
        "sekcje": [
            ("Trzy zeszyty", [
                "<strong>Przedszkole (4–6 lat):</strong> 10 zadań z obrazkami, bez limitu czasu, czytane na głos.",
                "<strong>Szkoła (7–15 lat):</strong> 15 zadań, 60 sekund na każde.",
                "<strong>Dorośli:</strong> 20 zadań, 45 sekund na każde.",
                "Szkoła i Dorośli mają osobne pytania, więc nic się między nimi nie powtarza.",
            ]),
            ("Rośnie razem z graczem", [
                "Każdy zeszyt ma stopnie trudności: dobry wynik przenosi wyżej, dwie słabsze gry z rzędu obniżają stopień.",
                "Aplikacja pamięta ostatnie pytania, więc w kolejnych grach rzadko się powtarzają.",
                "Rangi za czas spędzony na łamigłówkach.",
            ]),
            ("Rodzaje zadań", [
                "Ciągi liczb, matryce figur, analogie słowne i „co nie pasuje”.",
                "Obracanie figur w wyobraźni, liczenie, zagadki logiczne i wnioskowanie.",
                "Zadania na pamięć: zapamiętaj obrazki albo cyfry.",
            ]),
            ("Wynik", [
                "Wynik w skali IQ i miejsce na krzywej wyników.",
                "Profil zdolności: liczby, logika, język, pamięć, wyobraźnia, spostrzegawczość.",
                "Przegląd zadań z wyjaśnieniem poprawnej odpowiedzi i najlepszy wynik w każdym zeszycie.",
            ]),
            ("Dla rodzica", [
                "Bez reklam, bez zakupów w aplikacji, bez internetu.",
                "Nie zbiera żadnych danych i nie wymaga uprawnień.",
                "Za każdym razem inne zadania, jasny i ciemny motyw.",
            ]),
        ],
        "uwaga": "To zabawa inspirowana testami inteligencji. Wynik nie jest diagnozą ani prawdziwym pomiarem IQ.",
    },
    {
        "slug": "niko-19", "pakiet": "pl.leokodum.niko19", "nazwa": "Niko 19", "tag": "Dla młodych sportowców", "ikona": "ikona-torpedo.png?v=3",
        "status": "test", "kwadratowe": True,
        "krotko": "Codzienny trening dla dzieci z diamencikami, rangami, testem sprawności i radami o jedzeniu sportowca.",
        "wstep": "Codzienny trening dla młodych sportowców. Krótkie ćwiczenia jedno po drugim, pokazane przez trójwymiarową postać Niko. Za każdy trening dziecko zbiera diamenciki, rangi i nowe awatary, a co dwa tygodnie sprawdza w teście sprawności, ile już potrafi.",
        "zrzuty": zrzuty("niko-19/zrzuty", [
            ("1-start.png", "Ekran główny: ranga, seria dni i cel tygodnia"),
            ("2-test-sprawnosci.png", "Test sprawności z wykresem postępu"),
            ("3-nowy-rekord.png", "Nowy rekord w przysiadach"),
            ("4-jedzenie.png", "Jedzenie sportowca"),
        ]),
        "sekcje": [
            ("Trening krok po kroku", [
                "Aplikacja prowadzi przez kolejne ćwiczenia: przysiady, pompki, deski, wykroki, skoki, mostki i biegi bokiem.",
                "Każde ćwiczenie pokazuje postać Niko w trójwymiarowej grafice, więc od razu widać, jak je zrobić.",
                "Przy każdym ćwiczeniu odliczanie czasu i podpowiedź, co będzie dalej.",
                "Dodatkowy trening tego samego dnia też się liczy, za połowę diamencików.",
            ]),
            ("Motywacja", [
                "Diamenciki za każdy zaliczony trening i mnożnik za serię dni.",
                "Rangi do zdobycia i cel tygodnia.",
                "Awatary do odblokowania za zebrane diamenciki.",
            ]),
            ("Test sprawności", [
                "Co 14 dni krótki test: przysiady i pompki na kolanach w 30 sekund oraz deska na czas.",
                "Rekordy i wykres ostatnich wyników pokazują postęp.",
                "Dziecko porównuje się tylko ze sobą, bez rankingów i porównań z innymi.",
            ]),
            ("Jedzenie sportowca", [
                "Proste zasady: zdrowy talerz, regularne posiłki, woda, co zjeść przed treningiem i po nim.",
                "Ogólne zalecenia oparte na rekomendacjach żywieniowych dla dzieci, bez liczenia kalorii, odchudzania i suplementów.",
                "Osobna karta z informacjami dla rodzica.",
            ]),
            ("Dla rodzica", [
                "Kilku zawodników na jednym telefonie, każdy ze swoimi wynikami.",
                "Kopia postępu do pliku, którą można wczytać na innym telefonie. Wczytanie wymaga PIN-u rodzica.",
                "Działa w całości na telefonie, bez internetu i bez kont. Bez reklam.",
            ]),
        ],
        "uwaga": "Ćwicz w bezpiecznym miejscu, z wolną przestrzenią wokół. Przy bólu lub urazie przerwij trening.",
    },
    {
        "slug": "kids-locknet", "pakiet": "pl.leokodum.kidslocknet", "nazwa": "Kids LockNet", "tag": "Dla rodziców", "ikona": "ikona-kidslocknet.png?v=1",
        "status": "test", "film": "GIfikOUxhIA",
        "krotko": "Blokada internetu i hotspotu na telefonie dziecka, odblokowanie tylko PIN-em rodzica.",
        "wstep": "Ochrona rodzicielska, która blokuje cały internet na telefonie dziecka, także udostępnianie go przez hotspot. Odblokować może tylko rodzic, wpisując PIN na tym telefonie.",
        "zrzuty": zrzuty("kids-locknet/sklep", [
            ("1-zablokowany.png", "Internet zablokowany"), ("2-kod-pin.png", "Wpisywanie PIN-u"),
            ("3-czas.png", "Wybór czasu odblokowania"), ("4-otwarta-play.png", "Internet odblokowany"),
        ]),
        "sekcje": [
            ("Jak to działa", [
                "Jeden duży przycisk: czerwony, gdy internet jest zablokowany, zielony, gdy odblokowany.",
                "Po podaniu PIN-u wybierasz czas: 15 minut, godzinę albo do ręcznego włączenia blokady.",
                "Po upływie czasu blokada wraca sama, także po restarcie telefonu.",
                "Po kilku błędnych próbach PIN-u wpisywanie jest czasowo blokowane.",
            ]),
            ("Hotspot pod kontrolą", [
                "Hotspot można zablokować razem z internetem albo osobno, gdy internet ma działać.",
                "Próba włączenia hotspotu kończy się jego wyłączeniem i powiadomieniem, a ekran ustawień hotspotu prosi o PIN.",
            ]),
            ("Harmonogram", [
                "Blokada w wybranych godzinach, np. na noc albo na czas lekcji.",
                "Do wyboru: blokada internetu i hotspotu albo tylko hotspotu.",
                "Zmiana daty i godziny w telefonie jest chroniona, więc nie da się w ten sposób przesunąć harmonogramu.",
            ]),
            ("Ochrona ustawień", [
                "Ustawienia aplikacji są chronione PIN-em rodzica, także gdy internet jest odblokowany.",
                "Po podaniu PIN-u ustawienia są dostępne przez 10 minut.",
            ]),
            ("Prywatność", [
                "Bez chmury, kont i zdalnego sterowania.",
                "Aplikacja nie ma dostępu do internetu i nie zbiera żadnych danych.",
                "Blokada działa przez lokalny VPN, który odrzuca ruch na tym telefonie i z niczym się nie łączy.",
            ]),
        ],
        "uwaga": "Blokadę da się obejść, np. przez tryb awaryjny lub reset telefonu. Zapomnianego PIN-u nie da się przywrócić. Podczas rozmów ekran pozostaje odsłonięty, a na nakładce jest przycisk połączenia alarmowego.",
    },
    {
        "slug": "styl-jazdy", "pakiet": "pl.leokodum.styljazdy", "nazwa": "Styl Jazdy", "tag": "Dla kierowców", "ikona": "ikona-styljazdy.png?v=1",
        "status": "wewnetrzny",
        "krotko": "Ocena stylu jazdy kierowców w rodzinie lub firmie w skali 0–100.",
        "wstep": "Wybierz, kto jedzie, i ruszaj. Styl Jazdy ocenia przyspieszanie, hamowanie, zakręty, płynność i tempo, a potem porównuje kierowców w rodzinie lub firmie.",
        "sekcje": [
            ("Ocena każdej jazdy", [
                "Wynik w skali 0–100 i wskazówka, co poprawić.",
                "Osobne wyniki i ranking dla wielu kierowców.",
                "Auta rozpoznawane po Bluetooth, więc wyniki są też osobno dla każdego auta.",
            ]),
            ("Pomiary", [
                "Przeciążenia na żywo i rekordy.",
                "Pomiar 0–100 km/h z międzyczasami, tylko na zamkniętym terenie.",
                "Odcinkowe pomiary prędkości: komunikat głosowy przed odcinkiem, duże cyfry średniej i ile wolno jechać do końca.",
                "Po odcinku wynik zostaje na ekranie, a limit na odcinku można poprawić, jeśli się zmienił.",
            ]),
            ("Android Auto", [
                "Ekran jazdy i odcinkowe pomiary prędkości na ekranie samochodu.",
            ]),
            ("Prywatność", [
                "Wyniki zostają w telefonie.",
                "Trasy nie zapisujemy.",
                "Wystarczy telefon w uchwycie.",
            ]),
        ],
        "uwaga": "Wyniki pomiarów z telefonu są orientacyjne. Aplikacja będzie płatna w subskrypcji, z 7 dniami za darmo na start.",
    },
    {
        "slug": "skaner-sieci", "pakiet": "pl.leokodum.skanersieci", "nazwa": "Skaner Sieci", "tag": "Dla domu i instalatorów", "ikona": "ikona-skanersieci.png?v=1",
        "status": "wewnetrzny",
        "krotko": "Urządzenia w sieci, stan Wi-Fi, możliwe zagrożenia i raport PDF.",
        "zrzuty": zrzuty("skaner-sieci/sklep", [
            ("1-siec.png", "Urządzenia w sieci"), ("2-ryzyka.png", "Zagrożenia i zalecenia"),
            ("3-wifi.png", "Sieci Wi-Fi i kanały"), ("4-zdrowie.png", "Zdrowie sieci"), ("5-czuwanie.png", "Czuwanie"),
        ]),
        "wstep": "Pokazuje, co jest w Twojej sieci: urządzenia, ich nazwy i otwarte usługi. Sprawdza Wi-Fi, wskazuje możliwe zagrożenia i przygotowuje raport PDF.",
        "sekcje": [
            ("Urządzenia w sieci", [
                "Skan całej sieci lokalnej w kilkadziesiąt sekund.",
                "Nazwy i rodzaje urządzeń: drukarki, kamery, telewizory, routery i inne.",
                "Historia skanów i porównanie, co doszło, a co zniknęło.",
            ]),
            ("Wi-Fi", [
                "Sieci w okolicy, ich siła sygnału i kanały.",
                "Wykres kanałów, który pomaga wybrać mniej zatłoczony kanał.",
            ]),
            ("Bezpieczeństwo i zdrowie sieci", [
                "Wskazuje możliwe zagrożenia, np. usługi dostępne bez hasła.",
                "Sprawdza połączenie z internetem i trasę do niego.",
            ]),
            ("Czuwanie i raporty", [
                "Czuwanie w tle daje znać, gdy w sieci pojawi się nowe urządzenie.",
                "Raport PDF i eksport do CSV, np. dla klienta po montażu.",
            ]),
        ],
        "uwaga": "Skanuj tylko sieci, którymi zarządzasz lub na które masz zgodę właściciela.",
    },
]
