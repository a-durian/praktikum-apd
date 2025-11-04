"""
helperss.py
Berisi fungsi pembantu kecil yang digunakan di beberapa modul, seperti
`topMessage` untuk menampilkan header/heading yang rapi di terminal.
"""

def topMessage(topMessage):
    """Cetak header/heading dengan garis pembatas di atas dan bawah.

    Parameter `topMessage` adalah string judul yang ingin ditampilkan.
    """
    msgLong = ("="*21 + f" {topMessage} " + "="*21)
    print("="*len(msgLong))
    print(msgLong)
    print("="*len(msgLong))