# FileCleanerPro

FileCleanerPro, bilgisayarınızdaki gereksiz dosyaları hızlıca bulmanızı, silmenizi veya arşivlemenizi sağlayan **PyQt6 tabanlı bir masaüstü uygulamasıdır**.  
Amaç, disk alanını temizlemek ve dosya yönetimini kolaylaştırmaktır.

---

## Özellikler
- Klasör seçip belirli uzantılara göre dosya tarama
- Filtreleme seçenekleri:
  - Boyut (KB)
  - Gün (eski dosyalar)
  - Dosya adı (keyword)
- Seçilen dosyaları silme
- Seçilen dosyaları arşivleme (ZIP)
- Progress bar ile işlem takibi
- Log kaydı ve log geçmişini görüntüleme
- Kullanıcı dostu arayüz (PyQt6)

---

## Kurulum

### 1. Depoyu Klonla
```bash
git clone https://github.com/kullanici/FileCleanerPro.git
cd FileCleanerPro
2. Sanal Ortam (Opsiyonel)
bash
Kodu kopyala
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Gereksinimleri Yükle
bash
Kodu kopyala
pip install -r requirements.txt
Çalıştırma
bash
Kodu kopyala
python main.py
Proje Yapısı
bash
Kodu kopyala
FileCleanerPro/
│
├── cleaner/
│   ├── file_scanner.py   # Dosya tarama ve filtreleme
│   ├── file_manager.py   # Dosya silme, arşivleme
│   ├── file_logger.py    # Log okuma ve yazma
│
├── main.py               # PyQt6 GUI uygulaması
├── requirements.txt      # Gerekli kütüphaneler
└── README.md             # Proje açıklaması
Yol Haritası
Dosyaları geri dönüşüm kutusuna taşıma

Otomatik zamanlanmış temizlik

Disk alanı analizi

Log arama ve filtreleme

Çoklu klasör desteği

