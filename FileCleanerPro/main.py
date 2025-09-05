import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QFileDialog
from PyQt6.QtCore import Qt
from cleaner.file_scanner import scan_folder
from cleaner.file_manager import delete_files, archive_files


class FileCleanerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Cleaner Pro")
        self.setGeometry(100, 100, 600, 500)

        # Label
        self.label = QLabel("Klasörü seçip dosyaları tarayabilirsiniz!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(50, 20, 500, 30)

        # Dosyaları gösterme için widget
        self.file_list_widget = QListWidget(self)
        self.file_list_widget.setGeometry(50, 60, 500, 300)

        # Dosya tarama butonu 
        self.scan_button = QPushButton("Dosyaları Tara", self)
        self.scan_button.setGeometry(50, 380, 150, 40)
        self.scan_button.clicked.connect(self.scan_files)

        # Dosyaları silme butonu 
        self.delete_button = QPushButton("Seçilenleri Sil", self)
        self.delete_button.setGeometry(220, 380, 150, 40)
        self.delete_button.clicked.connect(self.deleted_selected)

        # Dosyaları arşivleme butonu 
        self.archive_button = QPushButton("Seçilenleri Arşivle", self)
        self.archive_button.setGeometry(390, 380, 160, 40)
        self.archive_button.clicked.connect(self.archived_selected)

        self.folder_path = ""

    def scan_files(self):
        if not self.folder_path:
            self.folder_path = QFileDialog.getExistingDirectory(self, "Klasör seç")
        if self.folder_path:
            extensions = [".txt", ".log", ".tmp",".pptx",".bmp",".rar"]
            files = scan_folder(self.folder_path, extensions)
            self.file_list_widget.clear()
            self.file_list_widget.addItems(files)
            self.label.setText(f"{len(files)} dosya bulundu!")

    def deleted_selected(self):
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        print("Seçilen dosyalar:", selected)
        if selected:
            delete_files(selected)
            self.scan_files()
            self.label.setText(f"{len(selected)} dosya silindi!")

    def archived_selected(self):
        selected = [item.text() for item in self.file_list_widget.selectedItems()]
        if selected:
            archive_folder = f"{self.folder_path}"
            archive_files(selected, archive_folder)
            self.scan_files()
            self.label.setText(f"{len(selected)} dosya arşivlendi!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileCleanerGUI()
    window.show()
    sys.exit(app.exec())
