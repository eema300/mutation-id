import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                            QFileDialog, QHBoxLayout, QPushButton,
                            QWidget, QFrame, QVBoxLayout)
from PyQt6.QtGui import QAction

# from logic import file_loader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window and layout
        self.setWindowTitle("mutation id")
        self.setMinimumSize(1150, 650)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()

        # side panel layout
        side_panel = QFrame()
        side_panel.setFrameShape(QFrame.Shape.StyledPanel)
        side_panel.setFixedWidth(250)
        side_panel_layout = QVBoxLayout()

        load_wt_button = QPushButton("Load Wild Type FASTA")
        load_mutation_button = QPushButton("Load Mutated Sequence FASTA")

        load_wt_button.clicked.connect(self.load_fasta_file)
        load_mutation_button.clicked.connect(self.load_fasta_file)

        side_panel_layout.addWidget(load_wt_button)
        side_panel_layout.addWidget(load_mutation_button)

        side_panel_layout.addStretch(1)
        
        side_panel.setLayout(side_panel_layout)
        main_layout.addWidget(side_panel)

        # central area layout
        central_area = QFrame()
        central_area_layout = QVBoxLayout()

        central_area.setLayout(central_area_layout)
        main_layout.addWidget(central_area, stretch=1)

        # set main layout
        central_widget.setLayout(main_layout)

        # menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        run_menu = menu_bar.addMenu("Run")

        load_wt_action = QAction("Load WT FASTA", self)
        load_wt_action.triggered.connect(self.load_fasta_file)

        load_mutation_action = QAction("Load Mutated FASTA", self)
        load_mutation_action.triggered.connect(self.load_fasta_file)

        alignment_action = QAction("Run Alignment", self)
        alignment_action.triggered.connect(self.run_alignment)

        file_menu.addAction(load_wt_action)
        file_menu.addAction(load_mutation_action)
        run_menu.addAction(alignment_action)

    def load_fasta_file(self):
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