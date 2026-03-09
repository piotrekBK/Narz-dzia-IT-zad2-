## 👥 Podział pracy (celowo powodujący konflikty)

### 👤 Osoba 1 – Critical Hits
Dodaje **szansę na krytyczny atak**.

Zmienia funkcję `attack()`.
### 👤 Osoba 2 – Armor System
Dodaje pancerz.
### 👤 Osoba 3 – Random Damage
Dodaje losowy damage.
Też zmienia funkcję attack().


### zad 2 projekt

Branche główne 
-dev
-release/nazwa
-dev musi być zablokowany jedynie merge ma działać

Projekty:

1. 🎮 Gra Snake z poziomami

Kilka osób pracuje nad tym samym plikiem z logiką gry.

Funkcje:

ruch węża

jedzenie

poziomy trudności

licznik punktów

zapis najlepszych wyników

Dlaczego będą konflikty

wszyscy edytują plik game.py

Struktura projektu

snake-game
│
├─ main.py
├─ game.py
├─ score.py
└─ settings.py

Podział pracy

Osoba 1 – ruch węża

Osoba 2 – jedzenie i punkty

Osoba 3 – poziomy trudności

Każdy zmienia game.py → duża szansa konfliktów.

2. 📋 Rozbudowana To-Do lista

Program z wieloma funkcjami.

Funkcje

dodawanie zadań

usuwanie

edycja

filtrowanie (zrobione / niezrobione)

zapis do JSON

Dlaczego będą konflikty

wspólne menu w main.py

Struktura

todo-app
│
├─ main.py
├─ tasks.py
└─ storage.py

Podział

Osoba 1 – menu

Osoba 2 – operacje na zadaniach

Osoba 3 – zapis danych

Wszyscy edytują main.py.

3. 💬 Terminalowy chat

Projekt z serwerem i klientem.

Funkcje

logowanie nicku

wysyłanie wiadomości

lista użytkowników

komenda /exit

Struktura

chat-app
│
├─ server.py
├─ client.py
└─ utils.py

Konflikty

kilka osób zmienia utils.py lub server.py.