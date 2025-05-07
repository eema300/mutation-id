from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QWidget
from .graph_button import GraphButton
from .graph import Graph
from logic import export_png_graph

# use a stacked widget to swtch between graphs when
# arrow buttons are pushed
# this means you need to name the graph objects to 
# be able to select for stack change
PATH = '/Users/emmagomez/code/cpsc362/mutation-id/assets/'
PREV_BUTTON = 'left_arrow.png'
NEXT_BUTTON = 'right_arrow.png'
PREV_BUTTON_HOVER = 'left_arrow_hover.png'
NEXT_BUTTON_HOVER = 'right_arrow_hover.png'
SAVE_BUTTON = 'save_graph.png'
SAVE_BUTTON_HOVER = 'save_graph_hover.png'


class Graph_Area(QWidget):
    def __init__(self, main_window, sequence_wt, sequence_mt, mutation, seqid_wt, seqid_mt):
        super().__init__()

        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.inner_widget_layout.setSpacing(0)
        self.setFixedWidth(550)
        self.setFixedHeight(450)

        # list of graphs for exporting ease
        self.graphs = []

        # graph header with next and prev buttons to switch between graphs
        header = QWidget()
        header.setObjectName("graph_header")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(5, 4, 7, 3)

        next_graph_button = GraphButton(PATH, NEXT_BUTTON, NEXT_BUTTON_HOVER)
        next_graph_button.setToolTip("Go to next graph")
        next_graph_button.clicked.connect(lambda: self.next_graph())
        prev_graph_button = GraphButton(PATH, PREV_BUTTON, PREV_BUTTON_HOVER)
        prev_graph_button.setToolTip("Go to previous graph")
        prev_graph_button.clicked.connect(lambda: self.prev_graph())
        
        header_layout.addWidget(prev_graph_button)
        header_layout.addWidget(next_graph_button)


        header_layout.addStretch(1)

        save_graph_button = GraphButton(PATH, SAVE_BUTTON, SAVE_BUTTON_HOVER)
        save_graph_button.setToolTip("Save current graph")
        save_graph_button.clicked.connect(lambda: export_png_graph(main_window,
                                                                   self.graph_switcher.currentWidget()))
        
        header_layout.addWidget(save_graph_button)
        
        header.setLayout(header_layout)

        # graph viewer container
        self.graph_switcher = QStackedWidget()

        # graphs
        bar_graph_wt = self.plot_bar_chart(sequence_wt, seqid_wt)
        bar_graph_mt = self.plot_bar_chart(sequence_mt, seqid_mt)
        
        bar_graph_wt.setObjectName('reference_nucleotide_counts')
        bar_graph_mt.setObjectName('mutated_nucleotide_counts')

        self.graph_switcher.addWidget(bar_graph_wt)
        self.graph_switcher.addWidget(bar_graph_mt)

        if mutation:
            mut_lollipop = self.plot_mutations_chart(sequence_wt, sequence_mt)
            mut_lollipop.setObjectName('mutation_density')
            self.graph_switcher.addWidget(mut_lollipop)

        # add to and set layouts
        self.graph_switcher.setCurrentWidget(bar_graph_wt)
        self.inner_widget_layout.addWidget(header)
        self.inner_widget_layout.addWidget(self.graph_switcher)
        self.setLayout(self.inner_widget_layout)
    
    def plot_bar_chart(self, sequence, seqid):
        graph = Graph(graph_type='bar', title=seqid, sequence=sequence)

        if graph.fig not in self.graphs:
            self.graphs.append(graph.fig)

        return graph.plot_widget
    
    def plot_mutations_chart(self, sequence_wt, sequence_mt):
        graph = Graph(graph_type='stem', title='mutation density', 
                    sequence_wt=sequence_wt, sequence_mt=sequence_mt)

        if graph.fig not in self.graphs:
            self.graphs.append(graph.fig)

        return graph.plot_widget

    def next_graph(self):
        new_index = (self.graph_switcher.currentIndex() + 1) % self.graph_switcher.count()
        self.graph_switcher.setCurrentIndex(new_index)

    def prev_graph(self):
        new_index = (self.graph_switcher.currentIndex() - 1) % self.graph_switcher.count()
        self.graph_switcher.setCurrentIndex(new_index)