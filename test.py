# test_scanner.py
from cleaner.file_scanner import scan_folder

# Test klasör yolu
folder_path = "C:/Users/Enes Link/Desktop/test_klasor"

# Tarama parametreleri
extensions = [".txt", ".log", ".tmp"]  # filtreleme yapmak için uzantılar
older_than_days = 0                     # tüm dosyaları al
smaller_than_kb = 10000                 # 10 MB'dan küçük dosyalar

# Fonksiyonu çalıştır
files = scan_folder(folder_path, extensions, older_than_days, smaller_than_kb)

# Sonuçları ekrana yazdır
print("Tarama sonucu bulunan dosyalar:")
for f in files:
    print(f)
