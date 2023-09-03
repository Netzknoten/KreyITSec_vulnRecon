# KreyITSec_vulnRecon 
### Automatischer Schwachstellenscanner in Python geschrieben ###


![Krey-ITSec_vulnRecon](https://github.com/Netzknoten/KreyITSec_vulnRecon/assets/114874531/9fd31dc0-0a1b-4be7-82f7-5d6b07eb633f)


## Willkommen ##
Dies ist eine Python Anwendung. Der Krey-iTSec VulnRecon ist ein Tool, zum erfassen von Schwachstellen. Geben sie zB. eine IP-Adresse, oder Port-Nummern ein. In der Ausgabe werden alle gesammelten Informationen angezeigt. Es kann auch per Knopfdruck in eine Textdatei exportiert werden. 

![GanzerBildschirmVSCode](https://github.com/Netzknoten/KreyITSec_vulnRecon/assets/114874531/8413c76d-f18f-4974-bb6c-1829bbed0b03)


## Ausführen ##


- Repository Klonen
- In das Lokale Verzeichnis wechseln
- Rechte Anpassen (Ausführbar markieren)
- Anwendung mit Python ausführen
- Alternativ kann auch beim Programmaufruf das Verzeichnis mitgegeben werden: python </path2Folder/pythondatei.py>

        git clone https://github.com/Netzknoten/KreyITSec_vulnRecon.git
        cd KreyITSec_vulnRecon
        chmod +x KreyITSec_ReconScanner.py
        python3 KreyITSec_ReconScanner.py
        


## Eingaben ##
![Eingabe](https://github.com/Netzknoten/KreyITSec_vulnRecon/assets/114874531/092c76c5-c38b-4a05-840a-9a51aa36b374)

Geben sie eine IPv4 Adresse z.B im CIDR/Format ein:
    
    192.168.0.0/16
  
Geben sie ein, oder mehrere Ports ein!

    1-1000
## Ausgabe ##

![TestBeendet](https://github.com/Netzknoten/KreyITSec_vulnRecon/assets/114874531/67a5ba78-2eff-4920-a29d-3627c42855d9)

Sie können mit dem Export Butten die Ausgabe in das Lokale Verzeichnis exportieren.

![Bildschirmfoto_2023-09-03_19-28-31](https://github.com/Netzknoten/KreyITSec_vulnRecon/assets/114874531/8f3bc130-b3d0-4dc2-b882-ffac5daa9aa6)
