# functions when a button is clicked
# ex for sequence view

# on file load change state for each successful
# file load
# once both files loaded, check to see if
# seqid and sequence have been returned
# if both returned, call the sequenceview 
# constructor

# yay!
from PyQt6.QtWidgets import QMainWindow
from logic import (align_sequences, load_fasta_file)

from .sequence_view import SequenceView
from .alignment_view import AlignmentView


def init_sequence_view(main_window: QMainWindow):
    print(type(main_window))

    on_load = load_fasta_file(main_window)
    
    if on_load:
        global seqid, sequence
        seqid, sequence = on_load

        # call sequence view constructor
        sequence_view = SequenceView(seqid, sequence,
                                     seqid, sequence)
        
        # add to main_window layout
        main_window.main_widget.addWidget(sequence_view)

        # switch to sequence view
        main_window.main_widget.setCurrentWidget(sequence_view)



# fix returns to None on error
def init_alignment_view():
    on_align = align_sequences(sequence, sequence)

    if type(on_align) is list:
        sequence_1_aligned = on_align[0]
        sequence_2_aligned = on_align[1]

        # call alignment viewer
        alignment_view = AlignmentView(sequence_1_aligned, sequence_2_aligned)

