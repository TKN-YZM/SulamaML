# Yenilenebilir Enerji ve IoT ile Akıllı Sistem

Bu proje, yenilenebilir enerji kaynakları kullanılarak oluşturulmuş ve IoT ile entegre edilmiş akıllı bir sistemdir. Proje, eş zamanlı hava raporu takibi, toprak nem ve ortam sıcaklık takibi gibi çeşitli sensörler aracılığıyla çevresel verileri toplar ve bu verileri analiz ederek enerji ve sulama verimliliğini optimize eder.

Ayrıca, makine öğrenmesi algoritmaları kullanılarak sistem akıllı hale getirilmiştir. Bu algoritmalar, toplanan verilere dayanarak sistem performansını sürekli olarak iyileştirmek için kullanılır.

## Teknolojiler ve Araçlar:
-Python / Makine Öğrenmesi Algoritmaları / Hava Durumu Raporları (Beatifulsoup kütüphanesi ile)
-Arduino / DHT11 Nem Ve Sıcaklık Sensörü / Röle (5V) / 12V Su Valfi / Toprak nem sensörü
-Veri Tabanı (SQL)

## Projenin çalışma mantığı
Bu projenin çalışma mantığı oldukça basittir. Öncelikle hava durumu, sıcaklık, nem ve toprak nem oranı gibi önemli verileri sürekli olarak toplar. Bu veriler, geçmiş verilere dayanarak eğitilmiş olan makine öğrenmesi algoritmalarıyla işlenir. Bu algoritmalar, geçmiş veri setlerini analiz eder ve optimal sulama zamanını, süresini ve miktarını belirlemek için karmaşık bir model oluşturur. Bu model doğrultusunda sulama işlemleri otomatik hale gelir.

<div align="center">
  <img  src="https://github.com/TKN-YZM/SulamaML/blob/main/czm.jpg" alt="Proje Çizim">
  <img  src="https://github.com/TKN-YZM/SulamaML/blob/main/czm2.jpg" alt="Proje Kod">
</div>

## Kurulum

1. Bu depoyu yerel makinenize klonlayın.
2. Gerekli bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.
3. Sensörlerin doğru şekilde bağlandığından emin olun.
4. Uygulamayı başlatmak için `python main.py` komutunu çalıştırın.
