import serial
import time

class SulamaSistemi:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.arduino = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Arduino'nun başlatılması için biraz bekleme

    def oku(self):
        while True:
            self.arduino.write(b'1')  # Arduino'ya veri göndererek veri okunmasını başlat
            veri = self.arduino.readline().decode().strip()  # Arduino'dan gelen veriyi oku
            nem_tprk, sicaklik_dht, nem_dht = veri.split(',')  # Arduino'dan gelen veriyi al
            print(f"Toprak Nem: {nem_tprk}, Ortam Sıcaklık: {sicaklik_dht}, Ortam Nem: {nem_dht}")
            time.sleep(1)  # Bir saniye bekle

    def kapat(self):
        self.arduino.close()


if __name__ == "__main__":
    arduino_port = "COM3"  # Arduino'nun bağlı olduğu port
    baud_rate = 9600  # Arduino'nun baud hızı

    sulama_sistemi = SulamaSistemi(arduino_port, baud_rate)

