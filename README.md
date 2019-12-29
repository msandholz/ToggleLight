# ToggleLight

## Schaltung testen
>**Schaltungsbelegung (BCM)**: 
>GPIO 25 = LED ein/aus schalten | 
>GPIO 24 = LED Status messen |
>GPIO 18 = Button

Mit dem Befehl `gpio -v` kann man prüfen, ob die WiringPi Bibliothek auf dem Raspi installiert ist. Mit dem Befehl `gpio readall` kann man sich Pinbelegung und Status ausgeben lassen.

Mit dem Befehlen `gpio -g mode 25 out` und `gpio -g write 25 1` kann man die LED ein und mit `gpio -g write 25 0` wieder ausschalten. Mit `gpio -g read 24` kann man den Status der LED messen.

## Python Programm installieren und testen
Als erstes müssen die Programme `SwitchLED.py` und `switchLED.service` in das Verzeichnis `/home/pi/SwitchLED` kopiert werden.
Ob das Programm startet, kann man mit `python SwitchLED/SwitchLED.py` testen. Das Kopieren kann man mit WinSCP durchführen.

## Script als Linux-Service starten
Will man das Python-Programm als Linux-Service starten, muss man die Datei `switchLED.service` in das Verzeichnis `/etc/systemd/system/` kopieren. Hierzu muß man das Kommando `sudo cp switchLED.service /etc/systemd/system/switchLED.service` absetzen.


====


Das Kopieren kann man mit WinSCP durchführen. Vorher benötigt man aber Root-Rechte.
1. Einloggen mit dem Nutzer `pi` und folgendes Kommando absetzen: `sudo passwd root`
2. Mit dem Kommando `nano /etc/ssh/sshd_config` die Konfigurationsdatei öffnen und den Wert `PermitRootLogin yes` setzen.
3. Raspi neu starten mit `sudo shutdown -r 0`


### Lese- & Schreib-Rechte vergeben
Als nächstes weisen wir die benötigten Rechte zu (Lesen & Schreiben): `sudo chmod 755 /etc/init.d/toggle_light`

### Start des Scripts
Wir testen das Skript indem wir es starten:  `sudo systemctl start switchLED.service`

### Stoppen des Scripts
Wir können das Script wieder stoppen mit: `sudo systemctl start switchLED.service`

### Enablen des Scripts
Damit das Skript beim booten auch aufgerufen wird, führen wir folgendes aus: `sudo systemctl enable switchLED.service`

Nun sollte das Programm bei booten auch ausgeführt werden.




### Entfernen des Scripts
Solltest du eines Tages dich umentscheiden und das Programm aus dem Autostart nehmen wollen, kannst du dies mit: `sudo update-rc.d -f  toggle_light remove`

## CustomControls in OctoPrint anlegen
Um in OctoPrint CustomControls anzulegen, muss man in der Datei `/home/pi/.octoprint/config.yaml` folgende Zeilen hinzufügen:

```
system:
  actions:
  - action: LED on
    command: gpio -g write 8 1
    confirm: false
    name: LED on
  - action: LED off
    command: gpio -g write 8 0
    confirm: false
    name: LED off
  - action: Printer on
    command: gpio -g write 7 0
    confirm: Switching Printer on...
    name: Printer on
  - action: Printer off
    command: gpio -g write 7 1
    confirm: Switching printer off...
    name: Printer off
  - action: streamon
    command: sudo service webcamd start
    confirm: false
    name: Start video stream
  - action: streamoff
    command: sudo service webcamd stop
    confirm: false
    name: Stop video stream   
```
