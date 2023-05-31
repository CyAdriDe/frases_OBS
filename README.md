# FRASES OBS
L’arxiu agafa el google sheets donat, on aquest només té una columna i va guardant cada frase en un arxiu **llista.txt** que va rotant.
## Codi
Primer és recomenable utilitzar un entorn virtual. 
```
python3 -m venv venv && \
source venv/bin/activate
```
Aixó crearà i activarà l’entron virtual (si ja està creat només utilitzar la segona línia).
Posteriorment instalem les depencencies:
```
pip3 install pandas
```
Finalment podem activar el programa amb:
```
python3 google_sheets.py
```
### Modificant el codi
És possible que s’hagin de canviar paràmetres.
Posem que la nostra URL és la següent:
[](https://docs.google.com/spreadsheets/d/1F7Q3YZZ8vzKq5ifFmp04NrrXKJDMzTDrXNmp-WcVsQ4/edit#gid=0)
D’aquí canviem la línia de SHEET_ID per el que hi ha després de la d/ i fins la següent /.
```
SHEET_ID = ‘1F7Q3YZZ8vzKq5ifFmp04NrrXKJDMzTDrXNmp-WcVsQ4’
```
També haurem de posar el nom del full que volem:
```
SHEET_NAME = ‘Sheet1’
```
Finalment tenim una variable TEMPS_ESPERA que son els segons que volem que hi hagi entre cada frase.
El programa actualitzarà el document quan hagi mostrat totes les frases.
## Configuració OBS
Afegeixes una font de text, i marques la casella _llegir desde arxiu_. Agafes l’arxiu **llista.txt** i el coloques segons convingui.  **NOTA: HA D’ESTAR EL PYTHON EXECUTANTSE PER POGUER CONFIGURAR I LLEGIR L’ARXIU**
