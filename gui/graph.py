from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from logic import get_base_proportions, find_all_mutations, create_bins, apply_bins

class Graph():
    def __init__(self, graph_type, title, sequence=None, sequence_wt=None, sequence_mt=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot()
        
        if graph_type == 'bar':
            counts = get_base_proportions(sequence)
            bases = list(counts.keys())
            num_bases = list(counts.values())
            colors = ['#ff44fc', '#fffd54', '#99ca3e', '#64b9fb', '#c0c0c0']

            self.ax.bar(bases, num_bases, color=colors, edgecolor='#000000')
            self.ax.set_yticks(range(0, max(num_bases) + 20, 20))
            self.ax.set_xlabel('nucleotide counts')

            self.name = ''.join([title, '_nucleotide_counts'])

        elif graph_type == 'stem':
            bin_counts = apply_bins(create_bins(sequence_mt), 
                                find_all_mutations(sequence_wt, 
                                                   sequence_mt))
            
            self.ax.stem(range(len(bin_counts)), bin_counts, linefmt='r-', markerfmt='rd')
            self.ax.set_yticks(range(max(bin_counts) + 1))
            self.ax.set_xlabel('bins')
            self.ax.set_ylabel('number of mutations')

            self.name = 'mutation_density'
        
        else:
            pass

        self.ax.set_title(title)
        self.fig.subplots_adjust(top=0.9, bottom=0.15)

        self.plot_widget = FigureCanvasQTAgg(self.fig)