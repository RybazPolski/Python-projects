# Panel gracza Minecraft
---
## 1. Instalacja
Do uruchomienia i poprawnego działania aplikacji wymagane jest uruchomienia serwera na którym będziemy korzystać z komend co za tym idzie potrzebujemy również Java Runtime Environment.
Konieczne jest również aby na serwerze znajdował się gracz.

1. W projekcie pod ścieżką `./server/` znajdziemy plik `start.bat`. Po jego uruchomieniu serwer podejmie próbę uruchomienia się. W razie problemów z uruchomieniem pliku, należy użyć komendy
    ```
    cd server
    java -Xms512M -Xmx1024M -jar spigot-1.16.3.jar -o true
    ```

2. By zainstalować wymagania projektu Python należy wykorzystać komendy 
    ```
    python -m pip install API.zip
    python -m pip pip install -r requirements.txt
    ```

3. W celu uruchomienia panelu należy użyć komendy 
    ```
    python form.py
    ```
---
## 2. Korzystanie z aplikacji
![Minecraft oraz uruchomiony panel gracza](https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pqpDuMCyeL9K93UqnMnbALZVrWNr5Tew2MrFPGk9-782PTSFps1-QGbPOkqp4ljX2xANZcMQcJLu3Zh--O-ANHkup2zA=w1879-h931)
A. Kolejno trzy pola na koordynaty X, Y oraz Z. Po wprowadzeniu prawidłowych liczb i kliknięciu przycisku "Teleportuj" gracz zostanie przeniesiony na podane koordynaty.
B. Lista z opcjami wyboru reprezentującymi odpowiednie moby i byty z gry Minecraft. Po wybraniu bytu i kliknięciu przyciskyu "Przywołaj moba/byt" na pozycji gracza pojawi się wybrany byt lub mob.
C. Lista z opcjami wyboru reprezentującymi odpowiednie bloki i obiekty z gry Minecraft. Po wybraniu opcji "Postaw blok" na pozycji gracza pojawi się wybrany blok lub obiekt.
D. 4 pola tekstowe oraz przycisk "Pozostaw wiadomość". Pola tekstowe reprezentują linijki tekstu które pojawią się na tabliczce po jej postawieniu. Po kliknięciu przycisku na pozycji gracza pojawi się tabliczka z podanym tekstem zwrócona w stronę północną.