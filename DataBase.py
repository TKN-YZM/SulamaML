import sqlite3
from datetime import datetime
import HavaDurumu
class SulamaVeritabani:

    def __init__(self, veritabani_adi):
        self.veritabani_adi = veritabani_adi
        self.baglanti = sqlite3.connect(self.veritabani_adi)
        self.imlec = self.baglanti.cursor()

        self.tablo_olustur()
    def tablo_olustur(self):
        self.imlec.execute('''CREATE TABLE IF NOT EXISTS sulama (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nem FLOAT,
                            sicaklik FLOAT,
                            toprak_nem FLOAT,
                            hava_tahmin_sicaklik FLOAT,
                            hava_tahmin_nem FLOAT,
                            zaman DATETIME,
                            hava_tahmin_metin TEXT,
                            su_vanasi INTEGER
                            )''')
        self.baglanti.commit()
    def veri_ekle(self, nem, sicaklik, toprak_nem, su_vanasi):
        zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hava_verileri=HavaDurumu.Hava(1,"Denizli")

        self.imlec.execute("INSERT INTO sulama (nem, sicaklik, toprak_nem, hava_tahmin_sicaklik, hava_tahmin_nem, zaman, hava_tahmin_metin,su_vanasi) VALUES (?, ?, ?, ?, ?, ?,?, ?)",
                           (nem, sicaklik, toprak_nem, hava_verileri[0], hava_verileri[1], zaman, hava_verileri[2],su_vanasi))
        self.baglanti.commit()
    def veri_goster(self):
        self.imlec.execute("SELECT * FROM sulama")
        veriler = self.imlec.fetchall()
        return veriler

    def baglantiyi_kapat(self):
        self.baglanti.close()

