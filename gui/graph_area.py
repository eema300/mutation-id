from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from .graph_button import GraphButton
from logic import get_base_proportions, find_all_mutations, create_bins, apply_bins

# use a stacked widget to swtch between graphs when
# arrow buttons are pushed
# this means you need to name the graph objects to 
# be able to select for stack change
PATH = '/Users/emmagomez/code/cpsc362/mutation-id/assets/'
PREV_BUTTON = 'left_arrow.png'
NEXT_BUTTON = 'right_arrow.png'
PREV_BUTTON_HOVER = 'left_arrow_hover.png'
NEXT_BUTTON_HOVER = 'right_arrow_hover.png'

class Graph(QFrame):
    def __init__(self, sequence_wt, sequence_mt, mutation, seqid_wt, seqid_mt):
        super().__init__()

        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.inner_widget_layout.setSpacing(0)
        self.setFixedWidth(550)
        self.setFixedHeight(450)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        # graph header with next and prev buttons to switch between graphs
        header = QWidget()
        header.setObjectName("graph_header")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        next_graph_button = GraphButton(PATH, NEXT_BUTTON, NEXT_BUTTON_HOVER)
        next_graph_button.clicked.connect(lambda: self.next_graph())
        prev_graph_button = GraphButton(PATH, PREV_BUTTON, PREV_BUTTON_HOVER)
        prev_graph_button.clicked.connect(lambda: self.prev_graph())
        
        header_layout.addWidget(prev_graph_button)
        header_layout.addWidget(next_graph_button)

        header_layout.addStretch(1)
        header.setLayout(header_layout)

        # graph viewer container
        self.graph_switcher = QStackedWidget()

        # graphs
        bar_graph_wt = FigureCanvasQTAgg(self.plot_bar_chart(sequence_wt, 0, seqid_wt))
        bar_graph_mt = FigureCanvasQTAgg(self.plot_bar_chart(sequence_mt, 1, seqid_mt))
        
        self.graph_switcher.addWidget(bar_graph_wt)
        self.graph_switcher.addWidget(bar_graph_mt)

        if mutation:
            mut_lollipop = FigureCanvasQTAgg(self.plot_mutations_chart(sequence_wt,
                                                                       sequence_mt))
            self.graph_switcher.addWidget(mut_lollipop)

        # add to and set layouts
        self.graph_switcher.setCurrentWidget(bar_graph_wt)
        self.inner_widget_layout.addWidget(header)
        self.inner_widget_layout.addWidget(self.graph_switcher)
        self.setLayout(self.inner_widget_layout)
    
    def plot_bar_chart(self, sequence, mutated, seqid):
        fig = Figure()

        counts = get_base_proportions(sequence)
        bases = list(counts.keys())
        num_bases = list(counts.values())
        colors = ['#ff44fc', '#fffd54', '#99ca3e', '#64b9fb']

        ax = fig.add_subplot()
        ax.bar(bases, num_bases, color=colors, edgecolor='#000000')
        ax.set_yticks(range(0, max(num_bases) + 20, 20))
        ax.set_title(seqid)
        ax.set_xlabel('nucleotide counts')

        fig.subplots_adjust(top=0.9, bottom=0.15)

        return fig
    
    def plot_mutations_chart(self, sequence_wt, sequence_mt):
        fig = Figure()

        bin_counts = apply_bins(create_bins(sequence_mt), 
                                find_all_mutations(sequence_wt, 
                                                   sequence_mt))

        ax = fig.add_subplot()
        ax.stem(range(len(bin_counts)), bin_counts, linefmt='r-', markerfmt='rd')
        ax.set_yticks(range(max(bin_counts) + 1))

        ax.set_title('mutation density')
        ax.set_xlabel('bins')
        ax.set_ylabel('number of mutations')

        fig.subplots_adjust(top=0.9, bottom=0.15)

        return fig

    def next_graph(self):
        new_index = (self.graph_switcher.currentIndex() + 1) % self.graph_switcher.count()
        self.graph_switcher.setCurrentIndex(new_index)

    def prev_graph(self):
        new_index = (self.graph_switcher.currentIndex() - 1) % self.graph_switcher.count()
        self.graph_switcher.setCurrentIndex(new_index)