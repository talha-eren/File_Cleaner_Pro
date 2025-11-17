# 🧹 Dosya Temizleyici Pro - Gelişmiş Dosya Yönetimi ve Temizleme Aracı

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.0+-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Gereksiz dosyaları temizlemek, arşivlemek ve disk alanını verimli yönetmek için PyQt6 tabanlı masaüstü uygulaması.

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Detaylı Özellikler](#detaylı-özellikler)
- [Yol Haritası](#yol-haritası)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## ✨ Özellikler

- **📁 Dosya Tarama**: Klasörlerdeki dosyaları tarama ve filtreleme
- **🔍 Gelişmiş Filtreleme**: 
  - Dosya türüne göre filtreleme
  - Boyut (KB) filtreleme
  - Tarih filtreleme (eski dosyalar)
  - Dosya adı (keyword) arama
- **🗑️ Dosya Silme**: Seçilen dosyaları güvenli şekilde silme
- **📦 Arşivleme**: Seçilen dosyaları ZIP formatında arşivleme
- **📊 Progress Bar**: İşlem takibi için ilerleme çubuğu
- **📝 Log Sistemi**: Tüm işlemlerin log kaydı ve geçmiş görüntüleme
- **🎨 Modern UI**: Kullanıcı dostu PyQt6 arayüzü

## 🚀 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip paket yöneticisi
- Qt6 kütüphaneleri (PyQt6 ile otomatik yüklenir)

### Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/talha-eren/File_Cleaner_Pro.git
cd File_Cleaner_Pro
```

### Adım 2: Sanal Ortam Oluşturun (İsteğe Bağlı ama Önerilir)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa, manuel olarak yükleyin:

```bash
pip install PyQt6
```

## 💻 Kullanım

### Uygulamayı Çalıştırma

```bash
python main.py
```

### Temel İş Akışı

1. **Klasör Seçimi**: Ana ekrandan temizlemek istediğiniz klasörü seçin
2. **Filtreleme**: 
   - Dosya türü seçin (örn: .tmp, .log, .bak)
   - Minimum/maksimum boyut belirleyin
   - Eski dosya gün sayısı girin
   - Dosya adında arama yapın
3. **Dosya Seçimi**: Filtrelenmiş dosyalar listesinden silmek/arşivlemek istediğiniz dosyaları seçin
4. **İşlem**: 
   - "Sil" butonuna tıklayarak dosyaları silin
   - "Arşivle" butonuna tıklayarak ZIP oluşturun
5. **Log Kontrolü**: İşlem geçmişini log ekranından görüntüleyin

## 📁 Proje Yapısı

```
FileCleanerPro/
│
├── cleaner/
│   ├── file_scanner.py      # Dosya tarama ve filtreleme modülü
│   ├── file_manager.py      # Dosya silme ve arşivleme modülü
│   ├── file_logger.py       # Log okuma ve yazma modülü
│
├── main.py                  # PyQt6 GUI ana uygulama
├── requirements.txt         # Gerekli Python kütüphaneleri
├── README.md                # Proje dokümantasyonu
└── .gitignore              # Git ignore dosyası
```

## 🔧 Detaylı Özellikler

### Dosya Tarama (File Scanning)

- Özyinelemeli klasör tarama
- Hızlı dosya listeleme
- Büyük klasörler için optimize edilmiş performans

### Filtreleme Seçenekleri

#### Dosya Türü (File Type)
```python
# Örnek: Sadece .tmp ve .log dosyalarını göster
Dosya Türü: .tmp, .log
```

#### Boyut Filtreleme (Size Filter)
```python
# Örnek: 100 KB'dan büyük dosyalar
Min Boyut: 100 KB
Max Boyut: 1000 KB
```

#### Tarih Filtreleme (Date Filter)
```python
# Örnek: 30 günden eski dosyalar
Gün Sayısı: 30
```

#### Dosya Adı Arama (Filename Search)
```python
# Örnek: "temp" içeren dosyalar
Anahtar Kelime: temp
```

### Dosya Silme (File Deletion)

- Güvenli silme işlemi
- Çoklu dosya seçimi desteği
- Silme öncesi onay mekanizması
- Geri dönüşüm kutusu desteği (yakında)

### Arşivleme (Archiving)

- ZIP formatında arşivleme
- Tarih damgalı arşiv dosyaları
- Sıkıştırma seviyesi ayarları
- Çoklu dosya arşivleme

### Log Sistemi (Logging System)

- Tüm işlemlerin otomatik kaydı
- Log geçmişi görüntüleme
- Log arama ve filtreleme
- Log export özelliği

### Progress Tracking

- Gerçek zamanlı ilerleme göstergesi
- İşlem durumu bilgisi
- İptal etme özelliği

## 🛠️ Gelişmiş Kullanım

### Komut Satırı Arayüzü (Gelecek)

```bash
python main.py --scan /path/to/directory --filter "*.tmp" --delete
```

### Yapılandırma Dosyası

`config.json` oluşturun:

```json
{
  "default_filters": {
    "file_types": [".tmp", ".log", ".bak"],
    "min_size_kb": 0,
    "max_size_kb": 1000,
    "days_old": 30
  },
  "archive_settings": {
    "compression_level": 6,
    "include_date": true
  }
}
```

### Ana Arayüz
- Modern ve kullanıcı dostu arayüz
- Kolay navigasyon
- Responsive tasarım

### Filtre Paneli
- Gelişmiş filtreleme seçenekleri
- Anlık sonuç güncellemesi
- Filtre kombinasyonları

### Log Görüntüleyici
- Detaylı işlem geçmişi
- Arama ve filtreleme
- Export özelliği

## 🗺️ Yol Haritası

### Planlanan Özellikler

- [ ] **Geri Dönüşüm Kutusu**: Dosyaları geri dönüşüm kutusuna taşıma
- [ ] **Otomatik Temizlik**: Zamanlanmış otomatik temizlik
- [ ] **Disk Analizi**: Disk alanı kullanım analizi
- [ ] **Gelişmiş Log**: Log arama ve filtreleme
- [ ] **Çoklu Klasör**: Birden fazla klasörü aynı anda tarama
- [ ] **Dosya Önizleme**: Silmeden önce dosya içeriği önizleme
- [ ] **Batch İşlemler**: Toplu işlem desteği
- [ ] **Cloud Entegrasyonu**: Cloud storage desteği

## ⚠️ Önemli Notlar

- **Yedekleme**: Önemli dosyaları silmeden önce mutlaka yedekleyin
- **Test Modu**: İlk kullanımda test modunda çalıştırın
- **İzinler**: Bazı sistem dosyaları için yönetici izni gerekebilir
- **Geri Alınamaz**: Silinen dosyalar geri alınamaz (geri dönüşüm kutusu özelliği gelene kadar)

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir Pull Request göndermekten çekinmeyin.

1. Depoyu fork edin
2. Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınıza push yapın (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## 👤 Yazar

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)

## 🙏 Teşekkürler

- Mükemmel GUI çerçevesi için PyQt6 topluluğuna
- Bu projenin tüm katkıda bulunanlarına ve kullanıcılarına

## 📧 İletişim

Sorular, öneriler veya destek için lütfen GitHub'da bir issue açın.

## 🐛 Bilinen Sorunlar

- Büyük dizin taraması zaman alabilir
- Bazı sistem dosyaları yönetici izni gerektirebilir
- Unicode dosya adları bazı sistemlerde sorun çıkarabilir

## 💡 İpuçları

- Uygulamayı test etmek için küçük dizinlerle başlayın
- Silmeden önce sonuçları daraltmak için filtreleri kullanın
- İşlemleri takip etmek için düzenli olarak logları kontrol edin
- Silmeden önce önemli dosyaları arşivleyin

---

⭐ Bu projeyi faydalı bulduysanız, lütfen yıldız vermeyi düşünün!






# 🧹 File Cleaner Pro - Advanced File Management and Cleanup Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.0+-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Gereksiz dosyaları temizlemek, arşivlemek ve disk alanını verimli yönetmek için PyQt6 tabanlı masaüstü uygulaması.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features in Detail](#features-in-detail)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **📁 Dosya Tarama**: Klasörlerdeki dosyaları tarama ve filtreleme
- **🔍 Gelişmiş Filtreleme**: 
  - Dosya türüne göre filtreleme
  - Boyut (KB) filtreleme
  - Tarih filtreleme (eski dosyalar)
  - Dosya adı (keyword) arama
- **🗑️ Dosya Silme**: Seçilen dosyaları güvenli şekilde silme
- **📦 Arşivleme**: Seçilen dosyaları ZIP formatında arşivleme
- **📊 Progress Bar**: İşlem takibi için ilerleme çubuğu
- **📝 Log Sistemi**: Tüm işlemlerin log kaydı ve geçmiş görüntüleme
- **🎨 Modern UI**: Kullanıcı dostu PyQt6 arayüzü

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Qt6 libraries (automatically installed with PyQt6)

### Step 1: Clone the Repository

```bash
git clone https://github.com/talha-eren/File_Cleaner_Pro.git
cd File_Cleaner_Pro
```

### Step 2: Create Virtual Environment (Optional but Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install PyQt6
```

## 💻 Usage

### Running the Application

```bash
python main.py
```

### Basic Workflow

1. **Klasör Seçimi**: Ana ekrandan temizlemek istediğiniz klasörü seçin
2. **Filtreleme**: 
   - Dosya türü seçin (örn: .tmp, .log, .bak)
   - Minimum/maksimum boyut belirleyin
   - Eski dosya gün sayısı girin
   - Dosya adında arama yapın
3. **Dosya Seçimi**: Filtrelenmiş dosyalar listesinden silmek/arşivlemek istediğiniz dosyaları seçin
4. **İşlem**: 
   - "Sil" butonuna tıklayarak dosyaları silin
   - "Arşivle" butonuna tıklayarak ZIP oluşturun
5. **Log Kontrolü**: İşlem geçmişini log ekranından görüntüleyin

## 📁 Project Structure

```
FileCleanerPro/
│
├── cleaner/
│   ├── file_scanner.py      # Dosya tarama ve filtreleme modülü
│   ├── file_manager.py      # Dosya silme ve arşivleme modülü
│   ├── file_logger.py       # Log okuma ve yazma modülü
│
├── main.py                  # PyQt6 GUI ana uygulama
├── requirements.txt         # Gerekli Python kütüphaneleri
├── README.md                # Proje dokümantasyonu
└── .gitignore              # Git ignore dosyası
```

## 🔧 Features in Detail

### Dosya Tarama (File Scanning)

- Recursive klasör tarama
- Hızlı dosya listeleme
- Büyük klasörler için optimize edilmiş performans

### Filtreleme Seçenekleri

#### Dosya Türü (File Type)
```python
# Örnek: Sadece .tmp ve .log dosyalarını göster
File Type: .tmp, .log
```

#### Boyut Filtreleme (Size Filter)
```python
# Örnek: 100 KB'dan büyük dosyalar
Min Size: 100 KB
Max Size: 1000 KB
```

#### Tarih Filtreleme (Date Filter)
```python
# Örnek: 30 günden eski dosyalar
Days Old: 30
```

#### Dosya Adı Arama (Filename Search)
```python
# Örnek: "temp" içeren dosyalar
Keyword: temp
```

### Dosya Silme (File Deletion)

- Güvenli silme işlemi
- Çoklu dosya seçimi desteği
- Silme öncesi onay mekanizması
- Geri dönüşüm kutusu desteği (yakında)

### Arşivleme (Archiving)

- ZIP formatında arşivleme
- Tarih damgalı arşiv dosyaları
- Sıkıştırma seviyesi ayarları
- Çoklu dosya arşivleme

### Log Sistemi (Logging System)

- Tüm işlemlerin otomatik kaydı
- Log geçmişi görüntüleme
- Log arama ve filtreleme
- Log export özelliği

### Progress Tracking

- Gerçek zamanlı ilerleme göstergesi
- İşlem durumu bilgisi
- İptal etme özelliği

## 🛠️ Advanced Usage

### Command Line Interface (Future)

```bash
python main.py --scan /path/to/directory --filter "*.tmp" --delete
```

### Configuration File

Create `config.json`:

```json
{
  "default_filters": {
    "file_types": [".tmp", ".log", ".bak"],
    "min_size_kb": 0,
    "max_size_kb": 1000,
    "days_old": 30
  },
  "archive_settings": {
    "compression_level": 6,
    "include_date": true
  }
}
```

### Main Interface
- Modern ve kullanıcı dostu arayüz
- Kolay navigasyon
- Responsive tasarım

### Filter Panel
- Gelişmiş filtreleme seçenekleri
- Anlık sonuç güncellemesi
- Filtre kombinasyonları

### Log Viewer
- Detaylı işlem geçmişi
- Arama ve filtreleme
- Export özelliği

## 🗺️ Roadmap

### Planned Features

- [ ] **Geri Dönüşüm Kutusu**: Dosyaları geri dönüşüm kutusuna taşıma
- [ ] **Otomatik Temizlik**: Zamanlanmış otomatik temizlik
- [ ] **Disk Analizi**: Disk alanı kullanım analizi
- [ ] **Gelişmiş Log**: Log arama ve filtreleme
- [ ] **Çoklu Klasör**: Birden fazla klasörü aynı anda tarama
- [ ] **Dosya Önizleme**: Silmeden önce dosya içeriği önizleme
- [ ] **Batch İşlemler**: Toplu işlem desteği
- [ ] **Cloud Entegrasyonu**: Cloud storage desteği

## ⚠️ Important Notes

- **Yedekleme**: Önemli dosyaları silmeden önce mutlaka yedekleyin
- **Test Modu**: İlk kullanımda test modunda çalıştırın
- **İzinler**: Bazı sistem dosyaları için yönetici izni gerekebilir
- **Geri Alınamaz**: Silinen dosyalar geri alınamaz (geri dönüşüm kutusu özelliği gelene kadar)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)

## 🙏 Acknowledgments

- PyQt6 community for excellent GUI framework
- All contributors and users of this project

## 📧 Contact

For questions, suggestions, or support, please open an issue on GitHub.

## 🐛 Known Issues

- Large directory scanning may take time
- Some system files may require administrator privileges
- Unicode file names may cause issues on some systems

## 💡 Tips

- Start with small directories to test the application
- Use filters to narrow down results before deletion
- Regularly check logs to track operations
- Archive important files before deletion

---

⭐ If you find this project helpful, please consider giving it a star!

