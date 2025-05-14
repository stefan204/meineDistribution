"""
    Autor:      Robert Panzirsch
    Datum:      xx.xx.xxxx
    Version:    1.0

    Modul eines Pakets für import

"""

from datetime import date

def wochentagheute():
    """Liefert den deutschen Wochentag."""
    return ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date.today().weekday()]

#print("Modul exekutiert!")
