import os

# Dosyaların oluşturulacağı klasör
folder_path = r"C:\\Users\\Talha Eren\\Desktop\\Projects\\FileCleanerPro\\FileCleanerPro\\test_klasor"

# Eğer klasör yoksa oluştur
os.makedirs(folder_path, exist_ok=True)

# Farklı türlerde dosya isimleri ve uzantıları
file_types = [".txt", ".log", ".tmp", ".pptx", ".bmp", ".rar"]

# Kaç dosya oluşturmak istediğin
num_files_per_type = 5

for ext in file_types:
    for i in range(1, num_files_per_type + 1):
        file_name = f"test_file_{i}{ext}"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Bu {file_name} dosyası test amaçlıdır.\n")

print(f"{len(file_types) * num_files_per_type} test dosyası oluşturuldu: {folder_path}")
