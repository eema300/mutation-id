from PyQt6.QtWidgets import QMainWindow
from logic import (align_sequences, load_fasta_file)

# enum consts
WT = 0
MT = 1

# state variable if sequence is diplayed
WILD_TYPE_ON = False
MUTATED_TYPE_ON = False

# global variables to hold the seq ids and sequences
seqid_WT = ""
seqid_MT = ""
sequence_WT = ""
sequence_MT = ""
sequence_WT_aligned = ""
sequence_MT_aligned = ""


# def init_sequence_view(main_window: QMainWindow):
#     from .sequence_view import SequenceView

#     on_load = load_fasta_file(main_window)
    
#     if on_load:
#         global seqid, sequence
#         seqid, sequence = on_load
            

#         # call sequence view constructor
#         sequence_view = SequenceView(main_window, 
#                                      seqid, sequence, WILD_TYPE_ON,
#                                      seqid, sequence, MUTATED_TYPE_ON)
        
#         # add to main_window layout
#         main_window.main_widget.addWidget(sequence_view)

#         # switch to sequence view
#         main_window.main_widget.setCurrentWidget(sequence_view)



def init_sequence_view_WT(main_window: QMainWindow):
    from .sequence_view import SequenceView
    global WILD_TYPE_ON

    on_load = load_fasta_file(main_window)
    
    if on_load:
        WILD_TYPE_ON = True
        global seqid_WT, sequence_WT
        seqid_WT, sequence_WT = on_load

        # call sequence view constructor
        sequence_view = SequenceView(main_window, 
                                    seqid_WT, sequence_WT, WILD_TYPE_ON,
                                    seqid_MT, sequence_MT, MUTATED_TYPE_ON)
        
        # add to main_window layout
        main_window.main_widget.addWidget(sequence_view)

        # switch to sequence view
        main_window.main_widget.setCurrentWidget(sequence_view)



def init_sequence_view_MT(main_window: QMainWindow):
    from .sequence_view import SequenceView
    global MUTATED_TYPE_ON 
    
    on_load = load_fasta_file(main_window)
    
    if on_load:
        MUTATED_TYPE_ON = True
        global seqid_MT, sequence_MT
        seqid_MT, sequence_MT = on_load

        # call sequence view constructor
        sequence_view = SequenceView(main_window, 
                                    seqid_WT, sequence_WT, WILD_TYPE_ON,
                                    seqid_MT, sequence_MT, MUTATED_TYPE_ON)
        
        # add to main_window layout
        main_window.main_widget.addWidget(sequence_view)

        # switch to sequence view
        main_window.main_widget.setCurrentWidget(sequence_view)



def init_alignment_view(main_window: QMainWindow):
    from .alignment_view import AlignmentView

    on_align = align_sequences(sequence_WT, sequence_MT)

    if on_align:
        global sequence_WT_aligned, sequence_MT_aligned
        sequence_WT_aligned, sequence_MT_aligned = on_align

        # call alignment viewer
        alignment_view = AlignmentView(main_window, 
                                       seqid_WT, sequence_WT_aligned, 
                                       seqid_MT, sequence_MT_aligned)

        # add to main_window layout
        main_window.main_widget.addWidget(alignment_view)

        # switch to alignment view
        main_window.main_widget.setCurrentWidget(alignment_view)



def init_mutation_view(main_window: QMainWindow):
    from .mutation_view import MutationView

    # call mutation viewer
    mutation_view = MutationView(main_window,
                                 seqid_WT, sequence_WT_aligned, 
                                 seqid_MT, sequence_MT_aligned)
    
    # add to main_window layout
    main_window.main_widget.addWidget(mutation_view)

    # switch to mutation view
    main_window.main_widget.setCurrentWidget(mutation_view)



def delete_sequence(main_window: QMainWindow, state):
    from .sequence_view import SequenceView
    
    global seqid_WT, seqid_MT, sequence_WT, sequence_MT, WILD_TYPE_ON, MUTATED_TYPE_ON

    # delete wild type 
    if state == WT:
        seqid_WT = ""
        sequence_WT = ""
        WILD_TYPE_ON = False
        
    elif state == MT:
        seqid_MT = ""
        sequence_MT = ""
        MUTATED_TYPE_ON = False

    else:
        return
    
    # call sequence view constructor
    sequence_view = SequenceView(main_window, 
                                    seqid_WT, sequence_WT, WILD_TYPE_ON,
                                    seqid_MT, sequence_MT, MUTATED_TYPE_ON)
    
    # add to main_window layout
    main_window.main_widget.addWidget(sequence_view)

    # switch to sequence view
    main_window.main_widget.setCurrentWidget(sequence_view)



def reset(main_window: QMainWindow):
    # empty globals
    global WILD_TYPE_ON, MUTATED_TYPE_ON, seqid_WT, seqid_MT
    global sequence_WT, sequence_MT, sequence_WT_aligned, sequence_MT_aligned
    
    WILD_TYPE_ON = False
    MUTATED_TYPE_ON = False
    seqid_WT = ""
    seqid_MT = ""
    sequence_WT = ""
    sequence_MT = ""
    sequence_WT_aligned = ""
    sequence_MT_aligned = ""

    # go back to welcome view
    from .welcome_view import WelcomeView

    welcome_view = WelcomeView(main_window)

    # add to main_window layout
    main_window.main_widget.addWidget(welcome_view)

    # switch to sequence view
    main_window.main_widget.setCurrentWidget(welcome_view)