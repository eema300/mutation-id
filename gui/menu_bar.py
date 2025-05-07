from PyQt6.QtWidgets import QMenuBar, QMainWindow
from PyQt6.QtGui import QAction, QKeySequence
from .view_caller import init_sequence_view_WT, init_sequence_view_MT

class MenuBar(QMenuBar):
    def __init__(self, main_window: QMainWindow):
        super().__init__()

        file_menu = self.addMenu("Load")
        load_ref = QAction("Load Reference FASTA", self)
        load_mut = QAction("Load Mutated FASTA", self)
        load_ref.triggered.connect(lambda: init_sequence_view_WT(main_window))
        load_mut.triggered.connect(lambda: init_sequence_view_MT(main_window))
        file_menu.addAction(load_ref)
        file_menu.addAction(load_mut)