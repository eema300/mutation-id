from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt
from .side_panel import SidePanel
from .view_area import ViewArea
from .sequence_design import SequenceDesign
from .delete_button import DeleteButton
from .view_caller import init_alignment_view, delete_sequence, reset
from .stat_sum_area import StatSummary
from logic import export_png_all_graphs


class SequenceView(QWidget):
    def __init__(self, main_window, 
                 seqidWT, sequenceWT, WT_ON,
                 seqidMT, sequenceMT, MT_ON):
        super().__init__()

        # set name so you can access it later
        self.setObjectName('sequence_view')

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()

        # view area
        self.view_area = ViewArea()


        if WT_ON and MT_ON:
            # upper half of side panel
            # add xwt button to wt widget, push to left
            delete_wt_button = DeleteButton()
            delete_wt_button.setToolTip("Discard reference sequence")
            delete_wt_button.clicked.connect(lambda: delete_sequence(main_window, 0))
            self.side_panel.wt_widget_layout.addWidget(delete_wt_button)
            # add seqidwt to wt widget
            seqid_WT_label = QLabel(seqidWT)
            seqid_WT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            seqid_WT_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            self.side_panel.wt_widget_layout.addWidget(seqid_WT_label)
            self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
            # add xmt button to mt widget
            delete_mt_button = DeleteButton()
            delete_mt_button.setToolTip("Discard mutated sequence")
            delete_mt_button.clicked.connect(lambda: delete_sequence(main_window, 1))
            self.side_panel.mt_widget_layout.addWidget(delete_mt_button)
            # add seqidmt to mt widget
            seqid_MT_label = QLabel(seqidMT)
            seqid_MT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.side_panel.mt_widget_layout.addWidget(seqid_MT_label)
            seqid_MT_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)
            # add align seq button
            alignment_button = QPushButton("Align Sequences")
            alignment_button.setToolTip("Align sequences to identify differences")
            alignment_button.clicked.connect(lambda: init_alignment_view(main_window))
            self.side_panel.side_panel_layout.addWidget(alignment_button)

            # lower half of side panel
            self.side_panel.side_panel_layout.addStretch(1)
            # export all graphs button
            export_all_graphs_button = QPushButton('Export All Graphs')
            export_all_graphs_button.setToolTip("Export all graphs as PNGs")
            export_all_graphs_button.clicked.connect(lambda: export_png_all_graphs(main_window,
                                                                                   stat_summary.graph.graphs,
                                                                                   seqidWT, seqidMT))
            self.side_panel.side_panel_layout.addWidget(export_all_graphs_button)
            # add reset button
            reset_button = QPushButton('Reset')
            reset_button.setToolTip("Delete all sequences and clear summaries")
            reset_button.clicked.connect(lambda: reset(main_window))
            self.side_panel.side_panel_layout.addWidget(reset_button)
            # set layout
            self.side_panel.setLayout(self.side_panel.side_panel_layout)
            
            # view area
            # display sequences in a nice format
            self.sequence_design = SequenceDesign(sequence_1=sequenceWT,
                                             sequence_2=sequenceMT,
                                             mutation=False)
            self.view_area.inner_widget_layout.addWidget(self.sequence_design)

            # summary
            # stats summary table
            stat_summary = StatSummary(main_window, sequenceWT, sequenceMT, False, seqidWT, seqidMT)
            self.view_area.inner_widget_layout.addWidget(stat_summary)

            # set layout
            self.view_area.setLayout(self.view_area.inner_widget_layout)
            

        elif WT_ON or MT_ON:
            from .view_caller import init_sequence_view_WT, init_sequence_view_MT
            if WT_ON:
                # add xwt button to wt widget
                delete_wt_button = DeleteButton()
                delete_wt_button.setToolTip("Discard reference sequence")
                delete_wt_button.clicked.connect(lambda: delete_sequence(main_window, 0))
                self.side_panel.wt_widget_layout.addWidget(delete_wt_button)
                # add seqidwt to wt widget
                seqid_WT_label = QLabel(seqidWT)
                seqid_WT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
                seqid_WT_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                self.side_panel.wt_widget_layout.addWidget(seqid_WT_label)
                self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
                # add load mt button to mt widget
                load_mutation_button = QPushButton("Load Mutated FASTA")
                load_mutation_button.setToolTip("Open a FASTA file with the mutated sequence")
                load_mutation_button.clicked.connect(lambda: init_sequence_view_MT(main_window))
                self.side_panel.mt_widget_layout.addWidget(load_mutation_button)
                self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)
                # reset button
                self.side_panel.side_panel_layout.addStretch(1)
                reset_button = QPushButton('Reset')
                reset_button.setToolTip("Delete all sequences and clear summaries")
                reset_button.clicked.connect(lambda: reset(main_window))
                self.side_panel.side_panel_layout.addWidget(reset_button)
                # set layout
                self.side_panel.setLayout(self.side_panel.side_panel_layout)

                # view area
                # add sequences to view area
                self.sequence_design = SequenceDesign(sequence_1=sequenceWT,
                                                sequence_2=None,
                                                mutation=False)
                self.view_area.inner_widget_layout.addWidget(self.sequence_design)
                self.view_area.inner_widget_layout.addStretch(1)
                # summary
                # set layout
                self.view_area.setLayout(self.view_area.inner_widget_layout)

            else: # MT_ON
                # add load wt button to wt widget
                load_wt_button = QPushButton("Load Reference FASTA")
                load_wt_button.setToolTip("Open a FASTA file with the reference sequence")
                load_wt_button.clicked.connect(lambda: init_sequence_view_WT(main_window))
                self.side_panel.wt_widget_layout.addWidget(load_wt_button)
                self.side_panel.wt_widget.setLayout(self.side_panel.wt_widget_layout)
                # add xmt button to mt widget
                delete_mt_button = DeleteButton()
                delete_mt_button.setToolTip("Discard mutated sequence")
                delete_mt_button.clicked.connect(lambda: delete_sequence(main_window, 1))
                self.side_panel.mt_widget_layout.addWidget(delete_mt_button)
                # add seqidmt to mt widget
                seqid_MT_label = QLabel(seqidMT)
                seqid_MT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
                self.side_panel.mt_widget_layout.addWidget(seqid_MT_label)
                seqid_MT_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                self.side_panel.mt_widget.setLayout(self.side_panel.mt_widget_layout)
                # reset button
                self.side_panel.side_panel_layout.addStretch(1)
                reset_button = QPushButton('Reset')
                reset_button.setToolTip("Delete all sequences and clear summaries")
                reset_button.clicked.connect(lambda: reset(main_window))
                self.side_panel.side_panel_layout.addWidget(reset_button)
                # set layout
                self.side_panel.setLayout(self.side_panel.side_panel_layout)
                # view area
                # add sequences to view area
                self.sequence_design = SequenceDesign(sequence_1=None,
                                                sequence_2=sequenceMT,
                                                mutation=False)
                self.view_area.inner_widget_layout.addWidget(self.sequence_design)
                self.view_area.inner_widget_layout.addStretch(1)
                # summary
                # set layout
                self.view_area.setLayout(self.view_area.inner_widget_layout)

        else:
            reset(main_window)

        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area)
        self.setLayout(self.layout)