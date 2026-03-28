<div align="center">

![Feza-X Banner](assets/feza_x_banner.png)

# 🛰️ Feza-X: Küp Uydu (CubeSat) Sistem Mimarisi Tasarımı
### *Milli Uzay Hamlesi Vizyonuyla Geliştirilen 3U Gezgin Platformu*

[![TUA - Astro Hackathon](https://img.shields.io/badge/TUA-Astro_Hackathon-1E3A8A?style=for-the-badge&logo=spaceX)](https://uzay.gov.tr/)
[![Category - Engineering](https://img.shields.io/badge/Kategori-Mühendislik_ve_Yazılım-F97316?style=for-the-badge)](https://github.com/topics/aerospace)
[![Level - Advanced](https://img.shields.io/badge/Zorluk-İleri_Seviye-DC2626?style=for-the-badge)](https://github.com/topics/cubesat)
[![License - MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

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

### B. Master Hidrolik & Elektronik Blok Diyagramı (Full Block Diagram)
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

## 🧠 5. Teknik Yaklaşım: İleri Seviye Özellikler

### A. Kenar Yapay Zeka (On-board Edge AI)
Feza-X, görüntüleri uzayda işleyerek sadece değerli verileri indirmeyi sağlar:

![Edge AI Processing](assets/edge_ai.png)

- **Bulut Eleme:** %70+ bulutlu görüntülerin elenmesi.
- **ROI Tespiti:** Gemi, araç veya arazi değişikliği tespiti.
- **Donanım:** Integrated NPU (Neural Processing Unit) @ 1.5W Peak.

### B. Uçuş Yazılım Yığını (NASA-cFS)
Uydunun yazılım mimarisi, yüksek modülerlik için **NASA Core Flight System (cFS)** tabanlıdır:
- **Hata Yönetimi:** Reset App -> Reset Processor -> Power Cycle döngüsü.
- **RTOS:** FreeRTOS üzerinden gerçek zamanlı görev yönetimi.

---

## ⚠️ 6. Güvenilirlik ve Risk Yönetimi (FMEA)
- **OBC SEU Koruması:** ECC RAM ve Watchdog Timer.
- **ADCS Redundancy:** Manyetik Tork Çubukları ile yedekli yönelim kontrolü.
- **Yazılım Safe Mode:** Düşük enerji durumunda sadece temel haberleşme hattını açık tutan güvenli mod.

---

## 🌍 7. Yer Segmenti ve Operasyonlar (Ground Segment)
- **MCC:** Python tabanlı PDU kod çözücü ve Grafana izleme arayüzü.
- **Haberleşme:**
    - **TT&C:** UHF/VHF (9.6 kbps) - Omni-directional.
    - **Data Downlink:** S-Band (2.0 Mbps) - High-gain Patch.

---

## 🛡️ 8. Regülasyon ve Uyumluluk
- **Uzay Çöpü Azaltma:** 500 km yörünge sayesinde <12 yılda doğal re-entry.
- **ITU Koordinasyonu:** BTK ve IARU üzerinden frekans tescili.

---

## 🛰️ 9. Misyon Yaşam Döngüsü ve Faz Yönetimi (Mission Lifecycle)
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

## 🌡️ 10. Termal Yönetim ve Kontrol (Thermal Engineering)
Uzay ortamının ekstrem sıcaklık farklarına (-50°C ile +80°C) karşı uygulanan stratejiler:
- **Pasif Kontrol:** Alüminyum 7075 şasi üzerine siyah eloksal kaplama ve MLI (Multi-Layer Insulation) battaniyeleri.
- **Aktif Kontrol:** Batarya blokları ve optik sensörler için entegre termistör kontrollü ısıtıcılar (Heaters).
- **Isıl Bütçe:** Solar panel yüzeylerindeki ısıyı şasiye ileten yüksek iletkenlikli termal arayüz malzemeleri (TIM).

---

## 🌌 11. Yörünge Dinamiği ve Kapsama (Orbit & Coverage)
- **Yörünge Tipi:** Güneşe Eşzamanlı Yörünge (SSO).
- **İrtifa:** 500 km | Eğim (Inclination): 97.4°.
- **LTAN (Local Time of Ascending Node):** 10:30 (Sabit ışık açısı ile tutarlı görüntüleme için).
- **Türkiye Kapsaması:** Günde ortalama 2-3 tam geçiş. Ortalama geçiş süresi: 8-10 dakika.

---

## 🚀 12. Gelecek Vizyonu: Feza-X Takımyıldızı
Feza-X-A (Prototip) başarısının ardından hedeflenen yol haritası:
- **Feza-X-B:** Gelişmiş L Bandı radar (SAR) sensörü entegrasyonu.
- **Feza-X-C:** Lazer haberleşme (Optical Comms) ile 1Gbps+ veri hızı.
- **Takımyıldız:** Toplam 12 uydu ile Türkiye üzerinden "Real-time" (15 dk altı) izleme kabiliyeti.

---

## 🇹🇷 13. Milli Uzay Vizyonu ve Stratejik Uyum
Feza-X, Türkiye'nin **10 Yıllık Milli Uzay Programı** hedefleriyle tam uyumlu olarak tasarlanmıştır:
- **Yerlileştirme:** Kritik bileşenlerde ASELSAN, TÜBİTAK UZAY ve ASPİLSAN çözümlerine öncelik veren [Milli Yol Haritası](docs/national_roadmap.md) benimsenmiştir.
- **Teknolojik Bağımsızlık:** Görüntü işleme ve uçuş yazılımı katmanlarında açık kaynaklı ancak milli modifikasyonlara açık mimariler (NASA-cFS tabanlı) kullanılmıştır.
- **Sürdürülebilirlik:** Uzay çöpünü minimize eden pasif de-orbit stratejileri ile küresel standartlara uyum sağlanmıştır.

---

## 🛠️ 14. Somut Çıktılar ve Yazılım Araçları (Aon-Class Strategic Ecosystem)
Proje, mimari dökümantasyonun ötesinde çalıştırılabilir altyapılar sunar:
- **[Link Budget Hesaplayıcı](communication-arch/link_budget_calculator.py):** S-Band ve UHF hatları için matematiksel doğrulama aracı.
- **[ADCS Kontrol Simülatörü](docs/adcs_simulation.py):** Nadir yönelimi için PID kontrol algoritması simülasyonu.
- **[Görev Sekansı (JSON)](communication-arch/mission_conops_sequence.json):** Makine tarafından okunabilir görev akışı.
- **[Yer İstasyonu API (Python)](docs/ground_station_api.py):** FastAPI tabanlı GS backend iskeleti.
- **[Telemetri Sözlüğü](communication-arch/telemetry_dictionary.json):** Sistem haberleşme protokolü.
- **[Yörünge Hesaplayıcı](docs/pass_calculator.py):** Python tabanlı yer istasyonu planlama aracı.
- **[MCC Docker Ortamı](Dockerfile):** Görev kontrol merkezini tek komutla kuran altyapı (IaC).
- **[Gereksinim Matrisi (RTM)](docs/requirement_traceability.md):** Mühendislik isterlerinin tam izlenebilirliği.

---

## 🌡️ 15. Detaylı Isıl Analiz ve Bütçe (Thermal Budget)
Feza-X'in bileşen bazlı operasyonel sıcaklık limitleri ve beklenen ısıl değerleri:

| Bileşen | Çalışma Aralığı (°C) | Beklenen (Güneş) | Beklenen (Gölge) | Koruma Stratejisi |
| :--- | :--- | :--- | :--- | :--- |
| **OBC / Brain** | -40 / +85 | +35 | -10 | Pasif (Şasi Bağlantısı) |
| **BATT / Batarya** | 0 / +45 | +25 | +5 | **Aktif Isıtıcı (Heater)** |
| **EPS / Power** | -40 / +85 | +45 | -15 | Pasif (Yüksek Emisivite) |
| **PAYLOAD / Optik** | -10 / +50 | +20 | 0 | MLI İzolasyon / Heaters |
| **RF Transceiver** | -40 / +85 | +55 | -20 | Termal Arayüz Malzemesi |

---

## 🛡️ 16. Siber Güvenlik ve STRIDE Tehdit Modeli
Feza-X'in güvenlik mimarisi, Microsoft STRIDE metodolojisi ile analiz edilmiştir:

| Tehdit Katmanı | Tehdit Tipi | Risk / Etki | Önleyici Tedbir |
| :--- | :--- | :--- | :--- |
| **Spoofing** | Yer İstasyonu Taklidi | Komuta Yetkisi Kaybı | **HMAC-SHA256 İmzası** |
| **Tampering** | Paket Manipülasyonu | Uydunun Yanlış Davranışı | **CRC-32 + Signature** |
| **Repudiation** | İtiraz Edilebilirlik | Log Sahteciliği | Read-only ECC Telemetry Log |
| **Information** | Veri Sızıntısı | Görüntülerin Çalınması | **AES-256-GCM Şifreleme** |
| **DoS** | Sinyal Karıştırma | İletişim Kopması | Spread Spectrum / FHSS |
| **Elevation** | Yetki Yükseltme | Kritik Mod Değişimi | PW Korumalı Safe Mode |

---

## 🛡️ 17. Komuta Şifrelemesi ve PDU Akışı
- **Uplink Authentication:** Yer istasyonundan gönderilen her komut, **HMAC-SHA256** algoritması ile imzalanır. Uydu, geçerli bir imza taşımayan komutları reddeder.
- **Replay Attack Protection:** Her komut paketinde "Anti-replay Counter" ve "Timestamp" bulunur. Eskimiş veya tekrar eden paketler işlenmez.
- **Downlink Encryption:** Bilimsel veriler ve görüntüler, S-Band üzerinden iletilmeden önce **AES-256-GCM** ile şifrelenir.

---

## 🏗️ 16. Mekanik Arayüz ve ICD (Interface Control Document)
Uydunun fiziksel entegrasyonu için belirlenen standartlar:
- **PC104 Bus Standard:** Alt sistemler arası elektriksel ve mekanik istifleme (Stacking).
- **Malzeme:** Alüminyum 70-75 (Havacılık Sınıfı), korozyona dayanıklı siyah eloksal kaplama.
- **Toleranslar:** ±0.05 mm (Kritik montaj yüzeyleri için).
- **Kill-Switch:** Deployer içinden çıkışta sistemi aktive eden çift yedekli mekanik anahtar.

---

## 🌀 19. Çevresel Test Matrisi (Verification)
Feza-X'in uzay kalifikasyonu için geçmesi gereken test seviyeleri:
- **Vibration (Sine/Random):** 20Hz - 2000Hz aralığında, RMS: 14.1 G.
- **Shock:** 1000 G @ 0.5ms (Ayrılma anı simülasyonu).
- **Thermal Vacuum (TVAC):** 10^-6 Torr basınçta, -40°C ile +85°C arası 8 döngü (Soak test).
- **EMI/EMC:** MIL-STD-461G uyumlu elektromanyetik uyumluluk testi.

---

## 🔬 20. Alt Sistem Teknik Spesifikasyonları (Deep-Dive)
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

## 📝 16. Haberleşme Katmanı ve Yazılım Protokolleri
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

## 🛠️ 17. Yer Destek Ekipmanları ve AIT Altyapısı (GSE)
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

## 📂 24. Proje Dizini ve Dosya Mimarisi
Reposu içindeki dosyaların görev ve hiyerarşi rehberi:

```text
📁 Feza-X-CubeSat-Architecture
├── 📁 assets/               # Görsel varlıklar, banner ve MCC mockup
├── 📁 communication-arch/    # Telemetri, Görev Sekansı ve Link Budget
├── 📁 docs/                 # Teknik derinlik, GS API, ADCS Sim, FMEA, RTM
├── 📁 hardware-layout/      # 3U yerleşim planları ve alt sistem spekleri
├── 📄 Dockerfile            # Görev kontrol merkezi IaC dökümanı
├── 📄 README.md             # Master dökümantasyon (Ana doküman)
├── 📄 requirements.txt      # Yazılım bağımlılıkları rehberi
└── 📄 LICENSE               # MIT Lisansı
```

---

## 🔗 Bağlantılar & Demos
*   📽️ **Tanıtım Videosu:** [Drive Linki]
*   📊 **Proje Sunumu:** [Drive Linki]
*   📂 **Tüm Çıktılar Arşivi:** [Drive/GitHub Ana Klasör]

---
<div align="center">
  Developed for <b>TUA Astro Hackathon 2026</b><br/>
  <i>"Gökyüzünün ötesindeki vizyoner fikirler için."</i>
</div>
