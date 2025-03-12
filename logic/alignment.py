from PyQt6.QtWidgets import QMessageBox
from Bio import pairwise2 as pw

# globals
MATCH_SCORE = 2
MISMATCH_PENALTY = -1
GAP_PENALTY = -2

# get start and end positions for aligned portions of sequences
def align_sequences(sequence_1, sequence_2):
    # Smith-Waterman local alignment
    alignments = pw.align.localms(sequence_1, sequence_2, 
                                  MATCH_SCORE, 
                                  MISMATCH_PENALTY, 
                                  GAP_PENALTY)
    
    # alignments is a list of tuples of best alignments, best score is elem 0
    # each tuple has sequence_1, sequence_2 (both with dashes on gaps),
    # alignment score (how many nucleotides matched)
    # start position, stop position

    try:
        # take the best scoring alignment
        best_alignment = alignments[0]

        # extract aligned sequences from best scoring alignment
        sequence_1_aligned = best_alignment[0]
        sequence_2_aligned = best_alignment[1]

        return [sequence_1_aligned, sequence_2_aligned]
    
    except IndexError:
        # if no alignment possible, list empty, and cannot identify mutations
        QMessageBox.critical("No Alignment Possible", "Sequences are too"
                             "different to align and find mutations. Try"
                             "a different sequence more similar to the"
                             "wild type.")
        
        return -1
        