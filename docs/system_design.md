# 🛸 TerraSense: Detaylı Sistem Tasarım Raporu (v1.1)

## 1. Giriş ve Amaç
Bu rapor, TerraSense 3U Küp Uydu projesinin mimari detaylarını, çalışma prensiplerini ve Milli Uzay Hamlesi vizyonu doğrultusunda geliştirilen inovatif yaklaşımları içermektedir.

## 2. Problem ve İhtiyaç Analizi
Mevcut Küp Uydu sistemlerinde karşılaşılan iki ana sorun:
1.  **Isıl Birikim:** Görev yükü ve işlemci arasındaki ısıl etkileşimin yönetilememesi.
2.  **Veri Tıkanıklığı:** Bilimsel verilerin (Payload data) ana sistem hattını meşgul ederek kritik telemetri akışını engellemesi.

## 3. Mimari Çözümler
### 3.1. Termal ve Kütle Yönetimi
- **Ayrıştırılmış Katmanlar:** OBC (Ana Bilgisayar), ısıl açıdan en korunaklı bölge olan orta modülde konumlandırılmıştır.
- **Kütle Dengesi:** Batarya blokları (en ağır bileşen) en alt birimde toplanarak yerçekimi gradienti stabilizasyonu sağlanmıştır.

### 3.2. Haberleşme Topolojisi
- **Hibrit Bus:** Sistem, kritik olmayan veriler için I2C, kritik telemetri için CAN ve görev yükü için SpaceWire kullanarak veri çarpışmalarını (collision) %0'a indirir.

## 4. Kullanılan Kaynaklar & Açık Veri
Bu proje, küresel uzay ekosistemindeki standartları takip eder:
- **TUA (Türkiye Uzay Ajansı)** vizyon dökümanları.
- **NASA Small Spacecraft Systems** rehberleri.
- **OpenSatStack** mimari referansları.

## 5. Sonuç
TerraSense, modüler yapısı ve optimize edilmiş veri yolu ile yüksek çözünürlüklü görüntüleme görevleri için düşük maliyetli ve yüksek performanslı bir temel mimari sunar.
