import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mutation id")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_file_action = QAction("Open File", self)
        open_file_action.triggered.connect(self.open_file)

        quit_app_action = QAction("Quit", self)
        quit_app_action.triggered.connect(self.close)

        file_menu.addAction(open_file_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_app_action)

    def open_file(self):
        pathname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "FASTA Files (*.fasta)")
        if not pathname:
            return
        
        try:
            with open(pathname, 'r') as file:
                sequence = file.read()

        except FileNotFoundError:
            QMessageBox.critical(self, "File Error", "The selected file could not be found")
        except IOError as e:
            QMessageBox.critical(self, "File Error", f"An error occured while reading the file {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occured {e}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()