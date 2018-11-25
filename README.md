# ToggleLight

## Schaltung testen
>**Schaltungsbelegung (WiringPi)**: 
>GPIO 10 = LED ein/aus schalten | 
>GPIO 11 = Relais ein/aus schalten | 
>GPIO 13 = LED Status messen |
>GPIO 14 = Button

Mit dem Befehl `gpio -v` kann man prüfen, ob die WiringPi Bibliothek auf dem Raspi installiert ist. Mit dem Befehl `gpio readall` kann man sich Pinbelegung und Status ausgeben lassen.

Mit dem Befehlen `gpio mode 10 out` und `gpio write 10 1` kann man die LED ein und mit `gpio write 10 0` wieder ausschalten. Mit `gpio read 13` kann man den Status der LED messen.

## Python Programm installieren und testen
Als erstes muß das Python-Programm `toggle_light.py` in das Verzeichnis `/home/pi/SwitchLED/toggle` kopiert werden.
Ob das Programm startet, kann man mit `python SwitchLED/toggle/toggle_light.py` testen.

## Script als Linux-Service starten
Will man das Python-Programm als Linux-Service starten, muss im Verzeichnis `/etc/init.d/` ein Skript angelegt werden. Hierzu die Datei `toggle_light` in das Verzeichnis `/etc/init.d/` kopieren.

Das Kopieren kann man mit WinSCP durchführen. Vorher benötigt man aber Root-Rechte.
1. Einloggen mit dem Nutzer `pi` und folgendes Kommando absetzen: `sudo passwd root`
2. Mit dem Kommando `nano /etc/ssh/sshd_config` die Konfigurationsdatei öffnen und den Wert `PermitRootLogin yes` setzen.
3. Raspi neu starten mit `sudo shutdown -r 0`


### Lese- & Schreib-Rechte vergeben
Als nächstes weisen wir die benötigten Rechte zu (Lesen & Schreiben): `sudo chmod 755 /etc/init.d/toggle_light`

### Start des Scripts
Wir testen das Skript indem wir es starten:  `sudo /etc/init.d/toggle_light start`

### Stoppen des Scripts
Wir können das Script wieder stoppen mit: `sudo /etc/init.d/toggle_light stop`

### Booten des Scripts
Damit das Skript beim booten auch aufgerufen wird, führen wir folgendes aus: `sudo update-rc.d toggle_light defaults`

Nun sollte das Programm bei starten auch ausgeführt werden.

### Entfernen des Scripts
Solltest du eines Tages dich umentscheiden und das Programm aus dem Autostart nehmen wollen, kannst du dies mit: `sudo update-rc.d -f  toggle_light remove`

## CustomControls in OctoPrint anlegen
Um in OctoPrint CustomControls anzulegen, muss man in der Datei `/home/pi/.octoprint/config.yaml` folgende Zeilen hinzufügen:

```
system:
  actions:
  - action: LED on
    command: gpio write 10 1
    name: LED on
  - action: LED off
    command: gpio write 10 0
    name: LED off
  - action: Printer on
    command: gpio write 11 1
    confirm: Switching Printer on...
    name: Printer on
  - action: Printer off
    command: gpio write 11 0
    confirm: Switching printer off...
    name: Printer off
```
