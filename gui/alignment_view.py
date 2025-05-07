from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt
from .side_panel import SidePanel
from .view_area import ViewArea
from .sequence_design import SequenceDesign
from .view_caller import init_mutation_view, reset, go_back_to_view
from logic import export_png, export_fasta, export_png_all_graphs
from .stat_sum_area import StatSummary

class AlignmentView(QWidget):
    def __init__(self, main_window,
                 seqid_1, sequence_1_aligned, 
                 seqid_2, sequence_2_aligned):
        super().__init__()

        # set name so you can access it later
        self.setObjectName('alignment_view')

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()

        # view area
        self.view_area = ViewArea()

        seqid_1_label = QLabel(seqid_1)
        seqid_1_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.side_panel.wt_widget_layout.addWidget(seqid_1_label)
        self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
        seqid_2_label = QLabel(seqid_2)
        seqid_2_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.side_panel.mt_widget_layout.addWidget(seqid_2_label)
        self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)
        
        back_button = QPushButton('Back')
        back_button.setToolTip("Go back to unaligned sequences")
        back_button.clicked.connect(lambda: go_back_to_view(main_window, view='sequence_view'))
        self.side_panel.side_panel_layout.addWidget(back_button)

        id_mutations_button = QPushButton('Highlight Mutations')
        id_mutations_button.setToolTip("Highlight mutations in sequence")
        id_mutations_button.clicked.connect(lambda: init_mutation_view(main_window))
        self.side_panel.side_panel_layout.addWidget(id_mutations_button)


        self.side_panel.side_panel_layout.addStretch(1)

        export_png_button = QPushButton('Export Alignment As PNG')
        export_png_button.setToolTip("Export aligned sequences as a PNG")
        export_png_button.clicked.connect(lambda: export_png(main_window, self.sequence_design.scene,
                                                             seqid_1, seqid_2))
        self.side_panel.side_panel_layout.addWidget(export_png_button)
        export_fasta_button = QPushButton('Export Alignment As FASTA')
        export_fasta_button.setToolTip("Export alignment as a FASTA file")
        export_fasta_button.clicked.connect(lambda: export_fasta(main_window, 
                                                                 seqid_1, seqid_2,
                                                                 sequence_1_aligned, sequence_2_aligned))
        self.side_panel.side_panel_layout.addWidget(export_fasta_button)

        # export all graphs button
        export_all_graphs_button = QPushButton('Export All Graphs')
        export_all_graphs_button.setToolTip("Export all graphs as PNGs")
        export_all_graphs_button.clicked.connect(lambda: export_png_all_graphs(main_window,
                                                                                stat_summary.graph.graphs,
                                                                                seqid_1, seqid_2))
        self.side_panel.side_panel_layout.addWidget(export_all_graphs_button)

        reset_button = QPushButton('Reset')
        reset_button.setToolTip("Delete all sequences and clear summaries")
        reset_button.clicked.connect(lambda: reset(main_window))
        self.side_panel.side_panel_layout.addWidget(reset_button)
        # combine side panel together
        self.side_panel.setLayout(self.side_panel.side_panel_layout)
        
        # display sequences in a nice format
        self.sequence_design = SequenceDesign(sequence_1=sequence_1_aligned,
                                         sequence_2=sequence_2_aligned,
                                         mutation=False)
        self.view_area.inner_widget_layout.addWidget(self.sequence_design)

        # stats summary table (and graphs....?)
        stat_summary = StatSummary(main_window, sequence_1_aligned, sequence_2_aligned, False, seqid_1, seqid_2)
        self.view_area.inner_widget_layout.addWidget(stat_summary)
        

        self.view_area.setLayout(self.view_area.inner_widget_layout)


        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area)
        self.setLayout(self.layout)