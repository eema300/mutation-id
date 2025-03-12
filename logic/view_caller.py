# functions when a button is clicked
# ex for sequence view

# on file load change state for each successful
# file load
# once both files loaded, check to see if
# seqid and sequence have been returned
# if both returned, call the sequenceview 
# constructor

# yay!
from logic import (align_sequences, load_fasta_file)

from gui import SequenceView, AlignmentView


def init_sequence_view():
    on_load = load_fasta_file()
    
    if type(on_load) is list:
        global seqid, sequence
        seqid = on_load[0]
        sequence = on_load[1]

        # call sequence viewer
        sequence_view = SequenceView(seqid, sequence,
                                     seqid, sequence)


    # if not a list, that means it returned -1 on error


def init_alignment_view():
    on_align = align_sequences(sequence, sequence)

    if type(on_align) is list:
        sequence_1_aligned = on_align[0]
        sequence_2_aligned = on_align[1]

        # call alignment viewer
        alignment_view = AlignmentView(sequence_1_aligned, sequence_2_aligned)

    # if not a list, that means it returned -1 on error