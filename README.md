<div align="center">

![Feza-X Banner](assets/feza_x_banner_v3.png)

# 🛰️ Feza-X: Küp Uydu (CubeSat) Sistem Mimarisi Tasarımı
### *Milli Uzay Hamlesi Vizyonuyla Geliştirilen 3U Gezgin Platformu*

[![Mission Status - Active](https://img.shields.io/badge/Mission_Status-Nominal-059669?style=for-the-badge&logo=statuspage)](https://github.com/topics/cubesat)
[![TRL - 5](https://img.shields.io/badge/TRL-5-3B82F6?style=for-the-badge&logo=rocket)](https://www.nasa.gov/directorates/heo/scan/engineering/technology/technology_readiness_level)
[![Energy Budget](https://img.shields.io/badge/Power-15W_Avg-FACC15?style=for-the-badge&logo=battery)](https://github.com/topics/aerospace)
[![Aethel-Class](https://img.shields.io/badge/Class-Aethel_Grand-7C3AED?style=for-the-badge&logo=starship)](https://github.com/topics/engineering)
[![TUA - Astro Hackathon](https://img.shields.io/badge/TUA-Astro_Hackathon-1E3A8A?style=for-the-badge&logo=spaceX)](https://uzay.gov.tr/)

---

### 🎛️ Mission Control Dashboard (Hızlı Erişim)

| [📊 Analiz](#0--rakip-analizi-ve-stratejik-konumlandırma-competitor-analysis) | [🏗️ Donanım](#🏗️-3-donanım-mimarisi-ve-mekanik-yerleşim-hardware-architecture) | [🧠 Yazılım](#-6-teknik-yaklaşım-ileri-seviye-özellikler) | [📡 Haberleşme](#-22-haberleşme-katmanı-ve-yazılım-protokolleri) |
| :---: | :---: | :---: | :---: |
| [⚠️ Riskler](#-7-güvenilirlik-ve-risk-yönetimi-fmea--heatmap) | [🌡️ Termal](#-11-termal-yönetim-ve-kontrol-thermal-engineering) | [🇹🇷 Vizyon](#🇹🇷-14-milli-uzay-vizyonu-ve-stratejik-uyum) | [📁 Dosyalar](#-25-proje-dizini-ve-dosya-mimarisi) |

---

</div>

## 0. 📊 Rakip Analizi ve Stratejik Konumlandırma (Competitor Analysis)
Feza-X, küresel açık kaynaklı küp uydu ekosisteminde "Havacılık Sınıfı" (Aethel-Class) güvenilirlik ve "Kenar Yapay Zeka" kabiliyetini birleştiren nadir mimarilerden biridir.

| Özellik | PyCubed (Open Source) | OreSat (Open Source) | Ticari 3U Platformlar | **Feza-X (Aethel-Class)** |
| :--- | :---: | :---: | :---: | :---: |
| **Uçuş Yazılımı** | CircuitPython (Temel) | C / Linux (Karmaşık) | Kapalı Kaynak | **NASA-cFS (Profesyonel)** |
| **Kenar AI** | Yok | Opsiyonel (Harici) | Özel Donanım (Pahalı) | **Entegre (NPU tabanlı)** |
| **Panel Tipi** | Karmaşık Mekanizmalar | Açılır (Deployable) | Çeşitli | **Gövdeye Entegre (Rijit)** |
| **Veri Yolu** | I2C / SPI | Card Bus | Kapalı Mimari | **SpaceWire / CAN (Hibrit)** |
| **FDIR Seviyesi** | Başlangıç | Orta | İleri | **Tam Entegre (L1-L4)** |

### Neden Feza-X?
1.  **Veri Darboğazı Çözümü:** Rakiplerimiz tüm verileri indirmeye çalışırken, Feza-X bulutlu görüntüleri uzayda eleyerek bant genişliğini %90 verimli kullanır.
2.  **Mekanik Kararlılık:** Açılır panellerin (deployables) neden olduğu mekanik risk ve atmosferik sürüklenmeyi, gövde entegre panellerle ekarte ettik.
3.  **Endüstriyel Olgunluk:** Hobi odaklı projelere kıyasla Feza-X, ICD, FDIR ve STRIDE gibi profesyonel mühendislik dökümanlarıyla "görev hazır" (mission-ready) seviyededir.

### 0.1. 📍 Mimari Felsefesi ve Evrimsel Süreç (Evolution & Benchmarks)
Feza-X, küresel ölçekte rüştünü ispatlamış iki ana ekosistemin "altın standartlarını" bir araya getirerek geliştirilmiştir:

*   **Yazılım İlhamı (NASA Dellingr):** Feza-X'in "kalbi" olan **NASA-cFS (Core Flight System)** mimarisi, Dellingr (6U) gibi kritik derin uzay görevlerinde kullanılan profesyonel uçuş yazılımı felsefesini temel alır. Bu, sistemimizi hobi odaklı (Arduino/Python) yapılardan ayırıp "Havacılık Sınıfı" bir olgunluğa taşır.
*   **Donanım Referansı (EnduroSat 3U):** Form faktörü ve modülerlik açısından piyasadaki en kararlı ticari platformlardan biri olan **EnduroSat 3U** mimarisiyle paralellik gösterir. PC104 bus yapısı ve fiziksel istifleme mantığı, bu endüstri standartlarına sadık kalınarak optimize edilmiştir.

### Neden Bu Mimariyi Geliştirdik?
Feza-X, bu jenerik referansları şu kritik alanlarda evrimleştirmiştir:
*   **Veri Taşıyıcısından "Düşünen" Uyduya:** Mevcut NASA-cFS altyapısı, NPU donanımıyla hibrit çalışacak ve **"Bulut Eleme/ROI"** yapacak şekilde özelleştirilmiştir.
*   **Mekanik Hassasiyet & GSD Hedefi:** 5 metre çözünürlük hedefi için açılır panellerin (deployables) neden olduğu mikroskobik titreşimler (jitter) elenmiş, **Body-Mounted** seçimiyle optik kararlılık maksimize edilmiştir.

---

## 1. 📋 Gerekli Girdiler (Required Inputs)
**Feza-X**, aşağıdaki teknik ve operasyonel isterleri karşılamak üzere optimize edilmiştir:
- **Form Faktörü:** 3U Standard CubeSat (10x10x34 cm).
- **Kütle & Güç:** < 4.0 kg | ~15W Ortalama Üretim.
- **Yörünge:** 500 km LEO (Sun-Synchronous).
- **Sensör Kabiliyeti:** 5.0m GSD Multispektral Görüntüleme.

---

## 2. 🌟 Yüksek Düzey Özet (High-Level Summary)
**Feza-X**, kısıtlı hacim ve enerji bütçesi altında maksimum veri işleme kabiliyeti sunan bir 3U Küp Uydu mimarisidir. Proje; **NASA-cFS** tabanlı uçuş yazılımı, **On-board Edge AI** işleme ve hibrit veri yolu (CAN/SpaceWire) mimarisi ile klasik küp uydu tasarımlarındaki veri darboğazlarını ve ısıl sorunları ortadan kaldırır.

---

## 🏗️ 3. Donanım Mimarisi ve Mekanik Yerleşim (Hardware Architecture)
Feza-X mimarisinin kalbi, modüler ve yedekli donanım katmanlarından oluşur.

### A. Sistem Mimari Şeması (Master Architecture)
Aşağıdaki yüksek çözünürlüklü görsel, Feza-X'in donanım katmanlarını ve teknik arayüzlerini şematize etmektedir:

![Hardware Architecture](assets/hardware_architecture.png)

### B. Mekanik Patlatılmış Görünüm (Exploded View)
Uydunun iç mekanik katmanlarını ve alt sistem yerleşimini gösteren detaylı mühendislik görünümü:

![Exploded View](assets/exploded_view.png)

### C. Master Hidrolik & Elektronik Blok Diyagramı (Full Block Diagram)
Tüm sensör, eyleyici ve işlemcilerin fiziksel bağlantı haritası:

```mermaid
graph TD
    subgraph "Unit 3: Payload & Optics"
        PL["Optical Sensor (RGB/NIR)"]
        MS["Mass Storage (NAND Flash)"]
        EDGE["Edge AI NPU Module"]
    end

    subgraph "Unit 2: Brain & Radio"
        OBC["OBC (ARM Cortex-M7)"]
        GPS["GNSS Receiver"]
        UHF["UHF/VHF Transceiver"]
        SBAND["S-Band High-Speed TX"]
    end

    subgraph "Unit 1: EPS & ADCS"
        EPS["EPS Board (MPPT)"]
        BATT["Li-Ion Battery Pack"]
        ADCS["ADCS MCU"]
        RW["Reaction Wheels (3-Axis)"]
        MTQ["Magnetorquers (3-Axis)"]
        IMU["IMU / Gyro / Mag"]
    end

    %% Internal Data Flow
    PL -->|SpaceWire| MS
    MS <-->|SpaceWire| EDGE
    EDGE -->|Processed Data| OBC
    GPS -->|UART / PPS| OBC
    GPS -->|UART / PPS| ADCS
    
    %% Control Bus
    OBC <-->|CAN-Bus| EPS
    OBC <-->|CAN-Bus| ADCS
    OBC <-->|UART / SPI| UHF
    OBC <-->|SPI / LVDS| SBAND

    %% Power distribution
    EPS <-->|SMBus| BATT
    EPS ---|3.3V / 5V| OBC
    EPS ---|5V / 12V| PL
    EPS ---|12V Peak| SBAND
    
    %% ADCS Control
    ADCS -->|I2C / PWM| RW
    ADCS -->|GPIO| MTQ
    IMU -->|I2C| ADCS
```

---

## 4. ⚡ Detaylı Elektronik Protokoller

### A. Güç Dağıtım Mimarisi (Power Distribution)
Feza-X, çift seviyeli regüle edilmiş bir güç hattı kullanır:

```mermaid
graph TD
    Solar[Solar Paneller - GaAs] --> MPPT[EPS - MPPT Controller]
    MPPT <--> Batt[40Wh Li-Ion Battery]
    MPPT --> Reg33[3.3V Bus - OBC/Sensors]
    MPPT --> Reg5[5V Bus - ADCS/Payload]
    MPPT --> Unreg[12V Unreg - Comms Amp]
```

### B. Donanım Arayüz Protokolleri (Interconnect)
| Protokol | Kullanım Alanı | Hız / Kritiklik |
| :--- | :--- | :--- |
| **SpaceWire** | Payload -> Storage | 200 Mbps |
| **CAN-Bus** | OBC <-> EPS <-> ADCS | 1 Mbps (Kritik Kontrol) |
| **SPI** | OBC -> SD Card / UHF | 20 MHz (Veri Aktarımı) |
| **I2C** | Sensors (IMU/Termal) | 400 kHz (Sistem Sağlığı) |

---

## 🏗️ 5. Stratejik Tasarım Avantajı: Gövde Entegre vs Açılır Paneller
Feza-X, ISISpace gibi sistemlerde kullanılan "açılır-kapanır" (deployable) güneş panelleri yerine **Gövdeye Entegre (Body-Mounted)** panelleri tercih ederek kritik mimari avantajlar sağlar:

| Özellik | Açılır Panel (Deployable) | Feza-X (Body-Mounted) | Avantaj |
| :--- | :--- | :--- | :--- |
| **Atmosferik Sürüklenme** | Yüksek (Geniş Yüzey) | **Düşük (Aerodinamik)** | Daha Uzun Yörünge Ömrü |
| **Yakıt Tüketimi** | Yüksek (Momentum Değişimi) | **Minimum (Stabil Kütle)** | %25+ Yakıt Tasarrufu |
| **Mekanik Risk** | Açılmama Riski Mevcut | **Sıfır Mekanik Risk** | %100 Güvenilirlik |
| **Kontrol Karmaşıklığı** | Esnek Yapı Titreşimi | **Rijit Gövde Yapısı** | Kolay ADCS Kontrolü |

*   **Sonuç:** Feza-X, deployable sistemlerin neden olduğu "sürüklenme ve yüksek yakıt tüketimi" engellerini ekarte ederek 500km yörüngede maksimum verimlilik sunar.

---

## 🧠 6. Teknik Yaklaşım: İleri Seviye Özellikler

### A. Kenar Yapay Zeka (On-board Edge AI)
Feza-X, görüntüleri uzayda işleyerek sadece değerli verileri indirmeyi sağlar:

![Edge AI Processing](assets/edge_ai.png)

```mermaid
graph LR
    Raw[Raw Images] --> Denoise[Noise Reduction]
    Denoise --> Segment[Cloud Segmentation]
    Segment -->|Cloudy > 70%| Drop[Discard / Low Res Store]
    Segment -->|Clear| Model[YOLOv8 Edge Inference]
    Model --> ROI[ROI Detection: Ships/Planes]
    ROI --> Compress[Lossless Compression]
    Compress --> Downlink((S-Band Downlink))
    
    style Drop fill:#f99,stroke:#333
    style Downlink fill:#9f9,stroke:#333
```

- **Bulut Eleme:** %70+ bulutlu görüntülerin elenmesi ile bant genişliği tasarrufu.
- **ROI Tespiti:** Gemi, araç veya arazi değişikliği tespiti (Selective Compression).
- **Donanım:** Integrated NPU (Neural Processing Unit) @ 1.5W Peak.

### B. Uçuş Yazılım Yığını (NASA-cFS)
Uydunun yazılım mimarisi, yüksek modülerlik için **NASA Core Flight System (cFS)** tabanlıdır:
- **Hata Yönetimi:** Reset App -> Reset Processor -> Power Cycle döngüsü.
- **RTOS:** FreeRTOS üzerinden gerçek zamanlı görev yönetimi.

---

## ⚠️ 7. Güvenilirlik ve Risk Yönetimi (FMEA & Heatmap)
- **OBC SEU Koruması:** ECC RAM ve Watchdog Timer.
- **ADCS Redundancy:** Manyetik Tork Çubukları ile yedekli yönelim kontrolü.
- **Yazılım Safe Mode:** Düşük enerji durumunda sadece temel haberleşme hattını açık tutan güvenli mod.

### Görev Risk Isı Haritası (Risk Heatmap)
Kritik risklerin olasılık ve etki bazlı 5x5 matris üzerindeki dağılımı:

| Olasılık \ Etki | Önemsiz | Düşük | Orta | Yüksek | Kritik |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Çok Yüksek** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |
| **Yüksek** | ⚪ | ⚪ | 🟡 [Termal] | ⚪ | 🔴 [Launch] |
| **Orta** | ⚪ | 🟢 [Sensor] | ⚪ | 🟠 [SEU] | ⚪ |
| **Düşük** | ⚪ | ⚪ | 🟢 [De-orbit]| ⚪ | ⚪ |
| **Çok Düşük** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |

*   **[Launch]:** Fırlatma anı yükleri (Kritik/Yüksek).
*   **[SEU]:** İşlemci hatası (Yüksek/Orta).
*   **[Termal]:** Isıl dengesizlik (Orta/Yüksek).

---

---

## 🌍 8. Yer Segmenti ve Operasyonlar (Ground Segment)
- **MCC:** Python tabanlı PDU kod çözücü ve Grafana izleme arayüzü.
- **Haberleşme:**
    - **TT&C:** UHF/VHF (9.6 kbps) - Omni-directional.
    - **Data Downlink:** S-Band (2.0 Mbps) - High-gain Patch.

---

## 🛡️ 9. Regülasyon ve Uyumluluk
- **Uzay Çöpü Azaltma:** 500 km yörünge sayesinde <12 yılda doğal re-entry.
- **ITU Koordinasyonu:** BTK ve IARU üzerinden frekans tescili.

---

## 🛰️ 10. Misyon Yaşam Döngüsü ve Faz Yönetimi (Mission Lifecycle)
Feza-X görevi, fırlatmadan görevin sonlandırılmasına kadar 5 ana faza ayrılmıştır:

1.  **Fırlatma ve İlk Yörünge Fazı (LEOP):**
    - Ayrılma sonrası 30 dk "sessiz mod".
    - Anten ve güneş paneli açılımı (Burn-wire aktivasyonu).
    - İlk "Beacon" sinyalinin yer istasyonuna iletilmesi.
2.  **Devreye Alma (Commissioning):**
    - Alt sistemlerin (EPS, ADCS, OBC) sağlık kontrolleri.
    - Kamera kalibrasyonu ve Edge AI model doğrulama.
3.  **Nominal Operasyonlar:**
    - Günlük 14-16 yörünge turu.
    - Hedef bölge (Türkiye) üzerinden geçerken görüntüleme ve S-Band veri indirme.
4.  **Uzatılmış Görev / Deney:**
    - Yazılım güncellemeleri ile yeni AI modellerinin test edilmesi.
5.  **Görevin Sonlandırılması (Decommissioning):**
    - Batarya pasivasyonu ve yörünge düşürme manevraları hazırlığı.

---

## 🌡️ 11. Termal Yönetim ve Kontrol (Thermal Engineering)
Uzay ortamının ekstrem sıcaklık farklarına (-50°C ile +80°C) karşı uygulanan stratejiler:
- **Pasif Kontrol:** Alüminyum 7075 şasi üzerine siyah eloksal kaplama ve MLI (Multi-Layer Insulation) battaniyeleri.
- **Aktif Kontrol:** Batarya blokları ve optik sensörler için entegre termistör kontrollü ısıtıcılar (Heaters).
- **Isıl Bütçe:** Solar panel yüzeylerindeki ısıyı şasiye ileten yüksek iletkenlikli termal arayüz malzemeleri (TIM).

---

## 🌌 12. Yörünge Dinamiği ve Kapsama (Orbit & Coverage)
- **Yörünge Tipi:** Güneşe Eşzamanlı Yörünge (SSO).
- **İrtifa:** 500 km | Eğim (Inclination): 97.4°.
- **LTAN (Local Time of Ascending Node):** 10:30 (Sabit ışık açısı ile tutarlı görüntüleme için).
- **Türkiye Kapsaması:** Günde ortalama 2-3 tam geçiş. Ortalama geçiş süresi: 8-10 dakika.

---

## 🚀 13. Gelecek Vizyonu: Feza-X Takımyıldızı ve Optik Bağ (Laser Comms)
Feza-X-A (Prototip) başarısının ardından hedeflenen yol haritası:
- **Feza-X-B:** Gelişmiş L Bandı radar (SAR) sensörü entegrasyonu.
- **Feza-X-C (Deep Space):** Lazer haberleşme (Optical Comms) ile 1Gbps+ veri hızı.
- **Takımyıldız:** Toplam 12 uydu ile Türkiye üzerinden "Real-time" (15 dk altı) izleme kabiliyeti.

### Optik Haberleşme (Feza-X-C Insight)
RF darboğazını aşmak için kullanılacak hibrit sistem:
- **Dalga Boyu:** 1550 nm (Near-IR).
- **Avantaj:** Dar hüzme genişliği sayesinde saptanma riskinin düşmesi ve devasa bant genişliği.
- **Zorluk:** 500km mesafede <1μrad hassasiyetle yüksek hassasiyetli işaretleme (Pointing).

---

---

## 🇹🇷 14. Milli Uzay Vizyonu ve Stratejik Uyum
Feza-X, Türkiye'nin **10 Yıllık Milli Uzay Programı** hedefleriyle tam uyumlu olarak tasarlanmıştır:
- **Yerlileştirme:** Kritik bileşenlerde ASELSAN, TÜBİTAK UZAY ve ASPİLSAN çözümlerine öncelik veren [Milli Yol Haritası](docs/national_roadmap.md) benimsenmiştir.
- **Teknolojik Bağımsızlık:** Görüntü işleme ve uçuş yazılımı katmanlarında açık kaynaklı ancak milli modifikasyonlara açık mimariler (NASA-cFS tabanlı) kullanılmıştır.
- **Sürdürülebilirlik:** Uzay çöpünü minimize eden pasif de-orbit stratejileri ile küresel standartlara uyum sağlanmıştır.

---

## 🛠️ 15. Aethel-Class Grand Ecosystem (Somut Çıktılar)

Proje, sadece teorik bir mimari değil, **mission-ready** bir yazılım ve simülasyon ekosistemi sunar:

| Kategori | Bileşen | Açıklama | Dosya |
| :--- | :--- | :--- | :--- |
| **Simülasyon** | 🌡️ Termal Denge | LEO yörünge sıcaklık analiz motoru | [thermal_equilibrium_model.py](docs/thermal_equilibrium_model.py) |
| **Simülasyon** | 🌀 ADCS Control | 3-eksenli PID yönelim simülatörü | [adcs_simulation.py](docs/adcs_simulation.py) |
| **Haberleşme** | 📦 CSP Gen | CubeSat Space Protocol paket üretici | [csp_packet_generator.py](communication-arch/csp_packet_generator.py) |
| **Haberleşme** | 📊 Link Budget | RF hat bütçesi ve S-Band analiz aracı | [link_budget_calculator.py](communication-arch/link_budget_calculator.py) |
| **Veri** | 📑 Telemetri Sözlüğü | Makine tarafından okunabilir PDU haritası | [telemetry_dictionary.json](communication-arch/telemetry_dictionary.json) |
| **Mühendislik** | 🛡️ FDIR Strategy | Otonom hata tespit ve kurtarma mantığı | [fdir_strategy.md](docs/fdir_strategy.md) |
| **Mühendislik** | 📐 Master ICD | Donanım/Yazılım arayüz kontrol dökümanı | [master_icd.md](docs/master_icd.md) |
| **Altyapı** | 🐳 MCC Docker | Görev Kontrol Merkezi IaC dökümanı | [Dockerfile](Dockerfile) |

---

## 🌡️ 16. Detaylı Isıl Analiz ve Bütçe (Thermal Budget)
Feza-X'in bileşen bazlı operasyonel sıcaklık limitleri ve beklenen ısıl değerleri:

| Bileşen | Çalışma Aralığı (°C) | Beklenen (Güneş) | Beklenen (Gölge) | Koruma Stratejisi |
| :--- | :--- | :--- | :--- | :--- |
| **OBC / Brain** | -40 / +85 | +35 | -10 | Pasif (Şasi Bağlantısı) |
| **BATT / Batarya** | 0 / +45 | +25 | +5 | **Aktif Isıtıcı (Heater)** |
| **EPS / Power** | -40 / +85 | +45 | -15 | Pasif (Yüksek Emisivite) |
| **PAYLOAD / Optik** | -10 / +50 | +20 | 0 | MLI İzolasyon / Heaters |
| **RF Transceiver** | -40 / +85 | +55 | -20 | Termal Arayüz Malzemesi |

---

## 🛡️ 17. Siber Güvenlik ve STRIDE Tehdit Modeli
Feza-X'in güvenlik mimarisi, Microsoft STRIDE metodolojisi ile analiz edilmiştir:

| Tehdit Katmanı | Tehdit Tipi | Risk / Etki | Önleyici Tedbir | Durum |
| :--- | :---: | :--- | :--- | :---: |
| **Spoofing** | Yer İstasyonu Taklidi | Komuta Yetkisi Kaybı | **HMAC-SHA256 İmzası** | ✅ |
| **Tampering** | Paket Manipülasyonu | Uydunun Yanlış Davranışı | **CRC-32 + Signature** | ✅ |
| **Repudiation** | İtiraz Edilebilirlik | Log Sahteciliği | Read-only ECC Telemetry Log | ✅ |
| **Information** | Veri Sızıntısı | Görüntülerin Çalınması | **AES-256-GCM Şifreleme** | ✅ |
| **DoS** | Sinyal Karıştırma | İletişim Kopması | Spread Spectrum / FHSS | ⚠️ |
| **Elevation** | Yetki Yükseltme | Kritik Mod Değişimi | PW Korumalı Safe Mode | ✅ |

---

## 🛡️ 18. Komuta Şifrelemesi ve PDU Akışı
- **Uplink Authentication:** Yer istasyonundan gönderilen her komut, **HMAC-SHA256** algoritması ile imzalanır. Uydu, geçerli bir imza taşımayan komutları reddeder.
- **Replay Attack Protection:** Her komut paketinde "Anti-replay Counter" ve "Timestamp" bulunur. Eskimiş veya tekrar eden paketler işlenmez.
- **Downlink Encryption:** Bilimsel veriler ve görüntüler, S-Band üzerinden iletilmeden önce **AES-256-GCM** ile şifrelenir.

---

## 🏗️ 19. Mekanik Arayüz ve ICD (Interface Control Document)
Uydunun fiziksel entegrasyonu için belirlenen standartlar:
- **PC104 Bus Standard:** Alt sistemler arası elektriksel ve mekanik istifleme (Stacking).
- **Malzeme:** Alüminyum 70-75 (Havacılık Sınıfı), korozyona dayanıklı siyah eloksal kaplama.
- **Toleranslar:** ±0.05 mm (Kritik montaj yüzeyleri için).
- **Kill-Switch:** Deployer içinden çıkışta sistemi aktive eden çift yedekli mekanik anahtar.

---

## 🌀 20. Çevresel Test Matrisi (Verification)
Feza-X'in uzay kalifikasyonu için geçmesi gereken test seviyeleri:
- **Vibration (Sine/Random):** 20Hz - 2000Hz aralığında, RMS: 14.1 G.
- **Shock:** 1000 G @ 0.5ms (Ayrılma anı simülasyonu).
- **Thermal Vacuum (TVAC):** 10^-6 Torr basınçta, -40°C ile +85°C arası 8 döngü (Soak test).
- **EMI/EMC:** MIL-STD-461G uyumlu elektromanyetik uyumluluk testi.

---

## 🔬 21. Alt Sistem Teknik Spesifikasyonları (Deep-Dive)
Aşağıdaki tablolar, Feza-X'in kritik bileşenlerinin mühendislik parametrelerini detaylandırır:

### Faydalı Yük (Payload) - Optik Sensör
| Parametre | Değer | Detay |
| :--- | :--- | :--- |
| **GSD (Ground Sample Distance)** | 5.0m @ 500km | Multispektral (R, G, B, NIR) |
| **Swath Width** | 24 km | Tek geçişte kapsama alanı |
| **SNR (Signal-to-Noise Ratio)** | >110 dB | Düşük ışık koşullarında yüksek verim |
| **Data Rate (Raw)** | 480 Mbps | Kamera - Bellek arası SpaceWire hattı |

### Haberleşme (Transceiver) - UHF & S-Band
| Parametre | UHF (TT&C) | S-Band (Mission Data) |
| :--- | :--- | :--- |
| **Frekans** | 437.5 MHz | 2405 MHz |
| **Modülasyon** | GFSK / 9k6 baud | QPSK / 2Mbps |
| **Protokol** | AX.25 / CSP | CCSDS Frame Structure |
| **TX Power** | 30 dBm (1W) | 33 dBm (2W) |

---

## 📝 22. Haberleşme Katmanı ve Yazılım Protokolleri
Feza-X, alt sistemler arası ve yer-uydu haberleşmesi için **CubeSat Space Protocol (CSP)** kullanır:

### CSP Paket Yapısı (Header)
```text
[ Priority (2b) | Source (5b) | Destination (5b) | Destination Port (6b) | Flags (8b) ]
Total: 32-bit Header
```
- **Port 7:** Telemetry Service (PDU format).
- **Port 10:** Command Service (Encrypted HMAC).
- **Port 31:** File Transfer (FP) Service for images.

---

## 🛠️ 23. Yer Destek Ekipmanları ve AIT Altyapısı (GSE)
Uydunun montaj ve test süreçleri için gereken profesyonel laboratuvar mimarisi:

### Elektriksel Yer Destek Ekipmanı (EGSE)
- **Solar Simulator:** Solar panellerin yörünge aydınlanmasını simüle eden AM0 ışık kaynağı.
- **Battery Cycler:** Batarya şarj/deşarj karakteristiği analizi.
- **Hardware-in-the-Loop (HiL):** OBC ve sensörlerin simülasyon ortamında testi.

### Mekanik Yer Destek Ekipmanı (MGSE)
- **ISO 7 Cleanroom:** Partikül arındırılmış montaj alanı.
- **Vibration Jig:** 3-eksenli titreşim tablası adaptörleri.
- **Thermal Vacuum Chamber (TVAC):** -60°C / +90°C vakum ortamı.

---

## 🌡️ 24. İleri Mühendislik ve Simülasyon Araçları
Feza-X, sadece bir tasarım değil, havacılık standartlarında (Aethel-Class) simülasyon altyapısı sunar:
- **Termal Analiz:** `thermal_equilibrium_model.py` ile farklı kaplama malzemelerinin (Alüminyum, Siyah Eloksal, Beyaz Boya) yörünge sıcaklık etkilerini görün.
- **Protokol Testi:** `csp_packet_generator.py` ile yer-uydu haberleşme paketlerini (Hex) oluşturun ve doğrulayın.
- **Güvenilirlik:** `fdir_strategy.md` ile sistem hatalarına karşı geliştirilen otonom kurtarma ağacını inceleyin.

---

## 📂 25. Proje Dizini ve Dosya Mimarisi
Reposu içindeki dosyaların görev ve hiyerarşi rehberi:

```text
📁 Feza-X-CubeSat-Architecture
├── 📁 assets/               # Görsel varlıklar, banner, exploded view ve mockup
├── 📁 communication-arch/    # Telemetri, Görev Sekansı, Link Budget ve Örnek Veri
├── 📁 docs/                 # Teknik derinlik, GS API, ADCS Sim, FMEA, RTM
├── 📁 hardware-layout/      # 3U yerleşim planları ve alt sistem spekleri
├── 📄 Dockerfile            # Görev kontrol merkezi IaC dökümanı
├── 📄 README.md             # Master dökümantasyon (Ana doküman)
├── 📄 requirements.txt      # Yazılım bağımlılıkları rehberi
└── 📄 LICENSE               # MIT Lisansı
```

---

## 🔗 26. Bağlantılar & Demos
*   📽️ **Tanıtım Videosu:** [Drive Linki]
*   📊 **Proje Sunumu:** [Drive Linki]
*   📂 **Tüm Çıktılar Arşivi:** [Drive/GitHub Ana Klasör]

---
<div align="center">
  Developed for <b>TUA Astro Hackathon 2026</b><br/>
  <i>"Gökyüzünün ötesindeki vizyoner fikirler için."</i>
</div>
