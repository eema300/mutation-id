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
        run_menu = menu_bar.addMenu("Run")

        load_wt_action = QAction("Load WT FASTA", self)
        load_wt_action.triggered.connect(self.open_file)

        load_mutation_action = QAction("Load Mutated FASTA", self)
        load_mutation_action.triggered.connect(self.open_file)

        alignment_action = QAction("Run Alignment", self)
        alignment_action.triggered.connect(self.run_alignment)

        file_menu.addAction(load_wt_action)
        file_menu.addAction(load_mutation_action)
        run_menu.addAction(alignment_action)

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

    def run_alignment(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()