import os
import datetime


def scan_folder(
    folder_path,
    extensions=None,
    older_than_days=None,
    smaller_than_kb=None,
    newer_than_days=None,
    larger_than_kb=None,
    keyword=None,
):
    """Belirtilen klasördeki dosyaları filtreleyip tam yollarını döndürür.

    Filtreler:
    - extensions: ['.txt', '.log'] gibi. Harf duyarsız karşılaştırılır.
    - older_than_days: Bu değerden DAHA yeni olanlar elenir; yalnızca daha yaşlı dosyalar kalır.
    - newer_than_days: Bu değerden DAHA yaşlı olanlar elenir; yalnızca daha yeni dosyalar kalır.
    - smaller_than_kb: Bu boyuttan büyük olanlar elenir.
    - larger_than_kb: Bu boyuttan küçük olanlar elenir.
    - keyword: Dosya adında bu anahtar kelime yoksa elenir.
    """

    if not folder_path or not os.path.isdir(folder_path):
        return []

    now = datetime.datetime.now()
    normalized_exts = None
    if extensions:
        # '.txt' ve 'txt' biçimlerini normalize et, küçük harfe çevir
        normalized_exts = {
            (ext if ext.startswith(".") else f".{ext}").lower() for ext in extensions
        }

    result = []

    for entry in os.scandir(folder_path):
        if not entry.is_file():
            continue

        file_path = entry.path
        filename = entry.name

        # Uzantı filtresi
        if normalized_exts is not None:
            _, ext = os.path.splitext(filename)
            if ext.lower() not in normalized_exts:
                continue

        # Anahtar kelime filtresi
        if keyword:
            if keyword.lower() not in filename.lower():
                continue

        # Zaman filtreleri
        file_mtime = datetime.datetime.fromtimestamp(entry.stat().st_mtime)
        age_days = (now - file_mtime).days
        if older_than_days is not None and age_days < older_than_days:
            continue
        if newer_than_days is not None and age_days > newer_than_days:
            continue

        # Boyut filtreleri
        size_kb = entry.stat().st_size / 1024.0
        if smaller_than_kb is not None and size_kb > smaller_than_kb:
            continue
        if larger_than_kb is not None and size_kb < larger_than_kb:
            continue

        result.append(file_path)

    return result