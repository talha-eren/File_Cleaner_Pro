import sys
import os
import shutil
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QFileDialog,
    QLineEdit, QProgressBar, QMessageBox, QDialog, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt
from cleaner.file_scanner import scan_folder
from cleaner.file_manager import delete_files, archive_files
from cleaner.file_logger import write_logs, read_logs

# ---------------- Log Viewer ---------------- #
class LogViewer(QDialog):
    def __init__(self, logs, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Log Kayıtları")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.log_list = QListWidget()
        self.log_list.addItems(logs if logs else ["Henüz log yok."])
        layout.addWidget(self.log_list)

        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

# ---------------- Main GUI ---------------- #
class FileCleanerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere başlığı ve boyutu
        self.setWindowTitle("File Cleaner Pro")
        self.setGeometry(100, 100, 600, 500)

        # Central widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        # Bilgilendirme labeli
        self.label = QLabel("Klasörü seçip dosyaları tarayabilirsiniz!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        # Dosya listesi
        self.file_list_widget = QListWidget()
        self.file_list_widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.file_list_widget.itemSelectionChanged.connect(self._update_action_buttons)
        self.layout.addWidget(self.file_list_widget)

        # Klasör seçme ve gösterme
        self.folder_button = QPushButton("Klasör Seç")
        self.folder_button.clicked.connect(self.choose_folder)
        self.layout.addWidget(self.folder_button)

        self.folder_display = QLineEdit()
        self.folder_display.setReadOnly(True)
        self.layout.addWidget(self.folder_display)

        # Dosya tarama, silme ve arşivleme butonları
        self.scan_button = QPushButton("Dosyaları Tara")
        self.scan_button.clicked.connect(self.scan_files)
        self.layout.addWidget(self.scan_button)

        self.delete_button = QPushButton("Seçilenleri Sil")
        self.delete_button.clicked.connect(self.deleted_selected)
        self.delete_button.setEnabled(False)
        self.layout.addWidget(self.delete_button)

        self.archive_button = QPushButton("Seçilenleri Arşivle")
        self.archive_button.clicked.connect(self.archived_selected)
        self.archive_button.setEnabled(False)
        self.layout.addWidget(self.archive_button)

        # Filtreler: Boyut, Tarih, İsim
        self.size_input = QLineEdit()
        self.size_input.setPlaceholderText("Boyut KB <= (Örn: 500)")
        self.layout.addWidget(self.size_input)

        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("Eski dosya gün > (Örn: 30)")
        self.layout.addWidget(self.date_input)

        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("İsim filtresi (Örn: rapor)")
        self.layout.addWidget(self.keyword_input)

        # Log gösterme butonu
        self.log_button = QPushButton("Logları Göster")
        self.log_button.clicked.connect(self.show_logs)
        self.layout.addWidget(self.log_button)

        # Seçilen klasör yolu
        self.folder_path = ""

    # ---------------- Fonksiyonlar ---------------- #
    def choose_folder(self):
        selected = QFileDialog.getExistingDirectory(self, "Klasör seç")
        if selected:
            self.folder_path = selected
            self.folder_display.setText(self.folder_path)
            self.label.setText("Klasör seçildi. Dosyaları tarayabilirsiniz!")

    def scan_files(self):
        if not self.folder_path:
            return
        extensions = [".txt", ".log", ".tmp", ".pptx", ".bmp", ".rar"]
        try:
            older_than = int(self.date_input.text()) if self.date_input.text() else None
            smaller_than = int(self.size_input.text()) if self.size_input.text() else None
        except ValueError:
            older_than = None
            smaller_than = None
        keyword = self.keyword_input.text() or None

        files = scan_folder(
            self.folder_path,
            extensions=extensions,
            older_than_days=older_than,
            smaller_than_kb=smaller_than,
            keyword=keyword
        )

        self.file_list_widget.clear()
        self.file_list_widget.addItems(files)
        self.label.setText("Tarama tamamlandı")
        self._update_action_buttons()

    def deleted_selected(self):
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        if not selected:
            return
        total = len(selected)
        self.progress_bar.setValue(0)
        for i, file_path in enumerate(selected, start=1):
            delete_files([file_path])
            self.progress_bar.setValue(int((i / total) * 100))
        self.scan_files()
        self.label.setText(f"{total} dosya silindi!")
        write_logs(f"{len(selected)} dosya silindi : {selected}")

    def archived_selected(self):
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        if not selected:
            return

        archive_folder = os.path.join(self.folder_path, "archive")
        os.makedirs(archive_folder, exist_ok=True)
        temp_folder = os.path.join(archive_folder, "temp_for_zip")
        os.makedirs(temp_folder, exist_ok=True)

        total = len(selected)
        self.progress_bar.setValue(0)

        for i, file_path in enumerate(selected, start=1):
            shutil.copy(file_path, temp_folder)
            self.progress_bar.setValue(int((i / total) * 100))

        zip_name = os.path.join(archive_folder, "archived_files")
        shutil.make_archive(zip_name, "zip", temp_folder)
        shutil.rmtree(temp_folder)

        self.scan_files()
        self.label.setText(f"{total} dosya arşivlendi ve zip oluşturuldu!")
        write_logs(f"{len(selected)} dosya arşivlendi : {selected}")

    def _update_action_buttons(self):
        has_selection = len(self.file_list_widget.selectedItems()) > 0
        self.delete_button.setEnabled(has_selection)
        self.archive_button.setEnabled(has_selection)

    def show_logs(self):
        logs = read_logs(limit=20)
        log_window = LogViewer(logs, self)
        log_window.exec()

# ---------------- Main ---------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileCleanerGUI()
    window.show()
    sys.exit(app.exec())
