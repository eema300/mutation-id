from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt
from .side_panel import SidePanel
from .view_area import ViewArea
from .sequence_design import SequenceDesign
from .view_caller import reset, go_back_to_view
from logic import export_png, export_csv, export_png_all_graphs, export_png_mutation
from .stat_sum_area import StatSummary

class MutationView(QWidget):
    def __init__(self, main_window,
                 seqid_1, sequence_1_aligned, 
                 seqid_2, sequence_2_aligned):
        super().__init__()

        # set name so you can access it later
        self.setObjectName('mutation_view')

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()

        # view area
        # mutations need to be highlighted
        self.view_area = ViewArea()
        
        
        # label the sequences with their seq ids
        seqid_1_label = QLabel(seqid_1)
        seqid_1_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.side_panel.wt_widget_layout.addWidget(seqid_1_label)
        self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
        seqid_2_label = QLabel(seqid_2)
        seqid_2_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.side_panel.mt_widget_layout.addWidget(seqid_2_label)
        self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)

        # back to alignment view button
        back_button = QPushButton('Back')
        back_button.setToolTip("Go back to alignment view")
        back_button.clicked.connect(lambda: go_back_to_view(main_window, view='alignment_view'))
        self.side_panel.side_panel_layout.addWidget(back_button)

        self.side_panel.side_panel_layout.addStretch(1)

        # exporting buttons
        export_png_button = QPushButton('Export Mutations As PNG')
        export_png_button.setToolTip("Export mutation-highlighted sequences as a PNG")
        export_png_button.clicked.connect(lambda: export_png_mutation(main_window, self.sequence_design.scene,
                                                             seqid_1, seqid_2))
        self.side_panel.side_panel_layout.addWidget(export_png_button)
        export_csv_button = QPushButton('Export Mutations As CSV')
        export_csv_button.setToolTip("Export mutation base-positions as a CSV")
        export_csv_button.clicked.connect(lambda: export_csv(main_window, 
                                                                 seqid_1, seqid_2,
                                                                 sequence_1_aligned, sequence_2_aligned))
        self.side_panel.side_panel_layout.addWidget(export_csv_button)
        
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

        # display the sequences in a nice format
        self.sequence_design = SequenceDesign(sequence_1=sequence_1_aligned,
                                         sequence_2=sequence_2_aligned,
                                         mutation=True)
        self.view_area.inner_widget_layout.addWidget(self.sequence_design)
        

        # stats summary table
        stat_summary = StatSummary(main_window, sequence_1_aligned, sequence_2_aligned, True, seqid_1, seqid_2)
        self.view_area.inner_widget_layout.addWidget(stat_summary)


        self.view_area.setLayout(self.view_area.inner_widget_layout)

        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area)
        self.setLayout(self.layout)