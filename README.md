# ToggleLight

# Script als Linux-Service starten
Als erstes muss im Verzeichnis /etc/init.d/ ein Skript erstellt werden, mittels welchem das Programm gestartet wird. Hierzu die Datei toggle_light in das Verzeichnis /etc/init.d/ kopieren.

Das Kopieren kann man mit WinSCP machen. Vorher benötigt man aber Root-Rechte.
1. Einloggen mit dem Nutzer pi und folgendes Kommando absetzen: sudo passwd root
2. Mit dem Kommando nano /etc/ssh/sshd_config die Konfigurationsdatei öffnen und den Wert PermitRootLogin yes setzen.


# Lese- & Schreib-Rechte vergeben
Als nächstes weisen wir die benötigten Rechte zu (Lesen & Schreiben): sudo chmod 755 /etc/init.d/NameDesSkripts

# Start des Scripts
Wir testen das Skript indem wir es starten:  sudo /etc/init.d/toggle_light start

# Stoppen des Scripts
Wir können das Script wieder stoppen mit: sudo /etc/init.d/toggle_light stop

# Booten des Scripts
Damit das Skript beim booten auch aufgerufen wird, führen wir folgendes aus: sudo update-rc.d toggle_light defaults

Nun sollte das Programm bei starten auch ausgeführt werden.

# Entfernen des Scripts
Solltest du eines Tages dich umentscheiden und das Programm aus dem Autostart nehmen wollen, kannst du dies mit: sudo update-rc.d -f  toggle_light remove
