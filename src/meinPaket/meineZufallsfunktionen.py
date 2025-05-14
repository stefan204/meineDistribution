"""
    Autor:      Robert Panzirsch
    Datum:      xx.xx.xxxx
    Version:    1.0

    Modul eines Pakets für import

"""

from random import randint

untergrenze = 0
obergrenze = 100


def meinezufallszahl():
    """Liefert eine ganze Zufallszahl."""
    return randint(untergrenze, obergrenze)

#print("Modul exekutiert!")
