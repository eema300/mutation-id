# need a state variable that changes every time
# you add a sequence using the file loader
# it needs to go from 0 to 1 to 2 and then decrease
# as such when user deletes a dequence

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, 
                            QHBoxLayout, QPushButton,
                            QWidget)
from PyQt6.QtGui import QAction

from .side_panel import SidePanel
from .view_area import ViewArea

from logic import (align_sequences, load_fasta_file, read_fasta,
                   validate_fasta, update_ambiguous_codes)

from .view_caller import init_sequence_view, init_alignment_view
from .sequence_view import SequenceView

sequence = "AATCTATTCAGTCATAACATTACCCACCCCATGTATGCTTTATTTTTAAATTAACATAGACAATTTTAAA" \
"AAAAATCGACGGTTTAAATTTTATTCCCAGCTACCCAACTTCCTAGCCAGCTTTTGAACACAGATTTTGT" \
"TACCCTTCAAGTTTTAACGCTGCTGTATTTTCTTAACTTGAATGTTAAAATGGATTAAGGTTTAGCTCAT" \
"GGGATACACACATTTTATATATGACTGCTTCCTGTGTAGTAGGGGACATGTCATTCGGTGTTAAATTGTC" \
"TTAAATAAAGTTCAGTTTTTCCCC"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window and layout
        self.setWindowTitle("mutation id")
        self.setMinimumSize(1150, 650)
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()
        load_wt_button = QPushButton("Load Wild Type FASTA")
        load_mutation_button = QPushButton("Load Mutated FASTA")
        load_wt_button.clicked.connect(lambda: init_sequence_view(self))
        load_mutation_button.clicked.connect(lambda: init_sequence_view(self))
        self.side_panel.side_panel_layout.addWidget(load_wt_button)
        self.side_panel.side_panel_layout.addWidget(load_mutation_button)
        self.side_panel.side_panel_layout.addStretch(1)
        self.side_panel.setLayout(self.side_panel.side_panel_layout)

        # view area
        view_area = ViewArea()

        # stacked widget for switching between views
        #self.stacked_widget = QStackedWidget()

        # set main layout
        self.main_layout.addWidget(self.side_panel)
        self.main_layout.addWidget(view_area, stretch=1)
        self.main_widget.setLayout(self.main_layout)

        # menu bar
        # menu_bar = self.menuBar()
        # file_menu = menu_bar.addMenu("File")
        # run_menu = menu_bar.addMenu("Run")
        # load_wt_action = QAction("Load WT FASTA", self)
        # load_wt_action.triggered.connect(load_fasta_file)
        # load_mutation_action = QAction("Load Mutated FASTA", self)
        # load_mutation_action.triggered.connect(load_fasta_file)
        # alignment_action = QAction("Run Alignment", self)
        # alignment_action.triggered.connect(self.run_alignment)
        # file_menu.addAction(load_wt_action)
        # file_menu.addAction(load_mutation_action)
        # run_menu.addAction(alignment_action)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()