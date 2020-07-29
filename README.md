# Assistant
Python

Opis:

-Prosty asystent, do zarządzania komputerem za pomocą głosu 

Wymagania:

-Python 3.6, ustawiony w zmiennych srodowiskowych, jako domyslny python dla CMD.
Jak sprawdzic? Wpisujesz w cmd 'python', jezeli odpala się python 3.6.X, to znaczy ze wszystko w porzadku.
-Sprawny mikrofon.

Instalacja:

-Odpalasz plik "modules.bat", instaluje on potrzebne biblioteki do działania skryptu.

-W pliku "main.py", zmieniasz scieżkę do dźwięku dingOn.mp3. Sciezka znajduję się w 14 linijce kodu.

Uzycie:

W pliku "settings.ini", ustawiasz słowa kluczowe, dla odpalania programów i folderów. Jedynym wyjątkiem jest "wejdz", jest on niezmmienny dla
stron internetowych.

Po odpaleniu skryptu, wciskasz 'F8', czekasz aż dźwięk się zakonczy, a nastepnie mowisz komendę. Przykład:
"Odpal <nazwa_programu, z pliku settings>"

W "settings.ini", nie uzywac polskich znaków dla poleceń w nawiasach. Skrypt je usuwa, więc poprowadzi to do bugów.
