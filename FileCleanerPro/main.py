import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QFileDialog, QLineEdit, QProgressBar
from PyQt6.QtCore import Qt
from cleaner.file_scanner import scan_folder
from cleaner.file_manager import delete_files, archive_files
import shutil
import os

class FileCleanerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere başlığı ve boyutu
        self.setWindowTitle("File Cleaner Pro")
        self.setGeometry(100, 100, 600, 500)

        # Progress Bar: Silme veya arşivleme işlemlerinde ilerlemeyi göstermek için
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, 470, 500, 20)
        self.progress_bar.setValue(0)  # Başlangıçta sıfır

        # Bilgilendirme labeli
        self.label = QLabel("Klasörü seçip dosyaları tarayabilirsiniz!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(50, 20, 500, 30)

        # Dosya listesi göstermek için widget
        self.file_list_widget = QListWidget(self)
        self.file_list_widget.setGeometry(50, 70, 500, 260)
        self.file_list_widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.file_list_widget.itemSelectionChanged.connect(self._update_action_buttons)

        # Bulunan dosya sayısı
        self.count_label = QLabel("", self)
        self.count_label.setGeometry(50, 50, 500, 16)

        # Klasör seçme butonu ve seçilen yolu gösteren alan
        self.folder_button = QPushButton("Klasör Seç", self)
        self.folder_button.setGeometry(50, 340, 100, 25)
        self.folder_button.clicked.connect(self.choose_folder)
        self.folder_display = QLineEdit(self)
        self.folder_display.setGeometry(160, 340, 390, 25)
        self.folder_display.setReadOnly(True)

        # Dosya tarama butonu
        self.scan_button = QPushButton("Dosyaları Tara", self)
        self.scan_button.setGeometry(50, 370, 150, 40)
        self.scan_button.clicked.connect(self.scan_files)

        # Dosya silme butonu
        self.delete_button = QPushButton("Seçilenleri Sil", self)
        self.delete_button.setGeometry(220, 370, 150, 40)
        self.delete_button.clicked.connect(self.deleted_selected)
        self.delete_button.setEnabled(False)

        # Dosya arşivleme butonu
        self.archive_button = QPushButton("Seçilenleri Arşivle", self)
        self.archive_button.setGeometry(390, 370, 160, 40)
        self.archive_button.clicked.connect(self.archived_selected)
        self.archive_button.setEnabled(False)

        # Boyut filtresi
        self.size_label = QLabel("Boyut KB <=", self)
        self.size_label.setGeometry(50, 412, 90, 20)
        self.size_input = QLineEdit(self)
        self.size_input.setGeometry(140, 410, 100, 24)
        self.size_input.setPlaceholderText("Örn: 500")

        # Tarih filtresi
        self.date_label = QLabel("Eski dosya gün >", self)
        self.date_label.setGeometry(260, 412, 120, 20)
        self.date_input = QLineEdit(self)
        self.date_input.setGeometry(390, 410, 100, 24)
        self.date_input.setPlaceholderText("Örn: 30")

        # İsim filtresi (keyword)
        self.keyword_label = QLabel("İsim filtresi", self)
        self.keyword_label.setGeometry(50, 442, 90, 20)
        self.keyword_input = QLineEdit(self)
        self.keyword_input.setGeometry(140, 440, 350, 24)
        self.keyword_input.setPlaceholderText("Örn: rapor")

        # Seçilen klasör yolu
        self.folder_path = ""

    def choose_folder(self):
        """Klasör seçim diyalogunu aç ve yolu göster"""
        selected = QFileDialog.getExistingDirectory(self, "Klasör seç")
        if selected:
            self.folder_path = selected
            self.folder_display.setText(self.folder_path)
            self.label.setText("Klasör seçildi. Dosyaları tarayabilirsiniz!")

    def scan_files(self):
        """Seçilen klasördeki dosyaları filtreleyerek listele"""
        if not self.folder_path:
            self.folder_path = QFileDialog.getExistingDirectory(self, "Klasör seç")
        if self.folder_path:
            extensions = [".txt", ".log", ".tmp", ".pptx", ".bmp", ".rar"]

            # Filtreleri oku
            try:
                older_than = int(self.date_input.text()) if self.date_input.text() else None
                smaller_than = int(self.size_input.text()) if self.size_input.text() else None
            except ValueError:
                older_than = None
                smaller_than = None

            keyword = self.keyword_input.text() or None

            # Dosya tarama fonksiyonunu çağır
            files = scan_folder(
                self.folder_path,
                extensions=extensions,
                older_than_days=older_than,
                smaller_than_kb=smaller_than,
                keyword=keyword
            )

            # List widget'ı temizle ve bulunan dosyaları ekle
            self.file_list_widget.clear()
            self.file_list_widget.addItems(files)
            self.label.setText("Tarama tamamlandı")
            self.count_label.setText(f"Bulunan dosya: {len(files)}")
            self._update_action_buttons()

    def deleted_selected(self):
        """Seçilen dosyaları sil ve progress bar ile göster"""
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        if selected:
            total = len(selected)
            self.progress_bar.setValue(0)
            for i, file_path in enumerate(selected, start=1):
                delete_files([file_path])  # Tek tek sil
                self.progress_bar.setValue(int((i / total) * 100))  # Progress bar güncelle

            self.scan_files()
            self.label.setText(f"{total} dosya silindi!")

    def archived_selected(self):
        """Seçilen dosyaları arşivle ve zip dosyası oluştur"""
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        if selected:
            # Arşiv klasörü
            archive_folder = os.path.join(self.folder_path, "archive")
            if not os.path.exists(archive_folder):
                os.makedirs(archive_folder)

            # Geçici klasör oluştur
            temp_folder = os.path.join(archive_folder, "temp_for_zip")
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)

            total = len(selected)
            self.progress_bar.setValue(0)

            # Dosyaları temp klasöre kopyala
            for i, file_path in enumerate(selected, start=1):
                shutil.copy(file_path, temp_folder)
                self.progress_bar.setValue(int((i / total) * 100))

            # Zip dosyasını oluştur
            zip_name = os.path.join(archive_folder, "archived_files")
            shutil.make_archive(zip_name, "zip", temp_folder)

            # Geçici klasörü sil
            shutil.rmtree(temp_folder)

            self.scan_files()
            self.label.setText(f"{total} dosya arşivlendi ve zip oluşturuldu!")
            self._update_action_buttons()

    def _update_action_buttons(self):
        """Seçime göre eylem butonlarını aktif/pasif yap."""
        has_selection = len(self.file_list_widget.selectedItems()) > 0
        self.delete_button.setEnabled(has_selection)
        self.archive_button.setEnabled(has_selection)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileCleanerGUI()
    window.show()
    sys.exit(app.exec())
