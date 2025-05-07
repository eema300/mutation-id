from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from .side_panel import SidePanel
from .view_area import ViewArea
from .view_caller import init_sequence_view_WT, init_sequence_view_MT

class WelcomeView(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # set name so you can access it later
        self.setObjectName('welcome_view')

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()
        load_wt_button = QPushButton("Load Reference FASTA")
        load_wt_button.setToolTip("Open a FASTA file with the reference sequence")
        load_mutation_button = QPushButton("Load Mutated FASTA")
        load_mutation_button.setToolTip("Open a FASTA file with the mutated sequence")
        load_wt_button.clicked.connect(lambda: init_sequence_view_WT(main_window))
        load_mutation_button.clicked.connect(lambda: init_sequence_view_MT(main_window))
        self.side_panel.wt_widget_layout.addWidget(load_wt_button)
        self.side_panel.mt_widget_layout.addWidget(load_mutation_button)
        self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
        self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)
        self.side_panel.side_panel_layout.addStretch(1)
        self.side_panel.setLayout(self.side_panel.side_panel_layout)

        # view area
        self.view_area = ViewArea()

        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area, stretch=1)
        self.setLayout(self.layout)