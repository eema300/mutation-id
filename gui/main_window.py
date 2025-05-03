# need a state variable that changes every time
# you add a sequence using the file loader
# it needs to go from 0 to 1 to 2 and then decrease
# as such when user deletes a sequence

from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .welcome_view import WelcomeView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window and layout
        self.setWindowTitle("mutation id")
        self.setMinimumSize(1312, 650)
        # stacked widget for switching between views
        self.main_widget = QStackedWidget()
        self.setCentralWidget(self.main_widget)

        # view on entry of program
        welcome_view = WelcomeView(self)

        # add view to stacked widget
        self.main_widget.addWidget(welcome_view)

        # menu bar
        # menu_bar = self.menuBar()
        # file_menu = menu_bar.addMenu("File")
        # run_menu = menu_bar.addMenu("Run")
        # load_wt_action = QAction("Load WT FASTA", self)
        # load_wt_action.triggered.connect(lambda: init_sequence_view(self))
        # load_mutation_action = QAction("Load Mutated FASTA", self)
        # load_mutation_action.triggered.connect(lambda: init_sequence_view(self))
        # #alignment_action = QAction("Run Alignment", self)
        # # alignment_action.triggered.connect(self.run_alignment)
        # file_menu.addAction(load_wt_action)
        # file_menu.addAction(load_mutation_action)
        # # run_menu.addAction(alignment_action)