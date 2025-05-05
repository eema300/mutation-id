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


def init_sequence_view_WT(main_window: QMainWindow):
    global WILD_TYPE_ON

    on_load = load_fasta_file(main_window)
    
    if on_load:
        WILD_TYPE_ON = True
        global seqid_WT, sequence_WT
        seqid_WT, sequence_WT = on_load

        from .sequence_view import SequenceView
        # call sequence view constructor
        sequence_view = SequenceView(main_window, 
                                    seqid_WT, sequence_WT, WILD_TYPE_ON,
                                    seqid_MT, sequence_MT, MUTATED_TYPE_ON)
        
        # add to main_window layout
        main_window.main_widget.addWidget(sequence_view)

        # switch to sequence view
        main_window.main_widget.setCurrentWidget(sequence_view)



def init_sequence_view_MT(main_window: QMainWindow):
    global MUTATED_TYPE_ON 
    
    on_load = load_fasta_file(main_window)
    
    if on_load:
        MUTATED_TYPE_ON = True
        global seqid_MT, sequence_MT
        seqid_MT, sequence_MT = on_load

        from .sequence_view import SequenceView
        # call sequence view constructor
        sequence_view = SequenceView(main_window, 
                                    seqid_WT, sequence_WT, WILD_TYPE_ON,
                                    seqid_MT, sequence_MT, MUTATED_TYPE_ON)
        
        # add to main_window layout
        main_window.main_widget.addWidget(sequence_view)

        # switch to sequence view
        main_window.main_widget.setCurrentWidget(sequence_view)



def init_alignment_view(main_window: QMainWindow):
    on_align = align_sequences(sequence_WT, sequence_MT)

    if on_align:
        global sequence_WT_aligned, sequence_MT_aligned
        sequence_WT_aligned, sequence_MT_aligned = on_align

        # check to see if already exists in stacked widget
        if view_exists(main_window, view='alignment_view'):
            go_back_to_view(main_window, view='alignment_view')
        else:
            from .alignment_view import AlignmentView
            # call alignment viewer
            alignment_view = AlignmentView(main_window, 
                                        seqid_WT, sequence_WT_aligned, 
                                        seqid_MT, sequence_MT_aligned)

            # add to main_window layout
            main_window.main_widget.addWidget(alignment_view)

            # switch to alignment view
            main_window.main_widget.setCurrentWidget(alignment_view)



def init_mutation_view(main_window: QMainWindow):
    # check to see if already exists in stacked widget
    if view_exists(main_window, view='mutation_view'):
        go_back_to_view(main_window, view='mutation_view')
    else:
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

    # delete mutated type        
    elif state == MT:
        seqid_MT = ""
        sequence_MT = ""
        MUTATED_TYPE_ON = False

    else:
        return

    if not (WILD_TYPE_ON or MUTATED_TYPE_ON):
        # switch to welcome view
        go_back_to_view(main_window, 'welcome_view')
        # delete sequence view
        delete_view(main_window, 'sequence_view')
    
    else:
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
    go_back_to_view(main_window, view='welcome_view')

    # delete all other views
    delete_all_views(main_window)



def go_back_to_view(main_window: QMainWindow, view):
    for i in range(main_window.main_widget.count()):
        widget = main_window.main_widget.widget(i)
        print(widget)
        
        if widget.objectName() == view:
            main_window.main_widget.setCurrentWidget(widget)
    print(main_window.main_widget.count())



def view_exists(main_window: QMainWindow, view):
    exist = False

    for i in range(main_window.main_widget.count()):
        widget = main_window.main_widget.widget(i)
        
        if widget.objectName() == view:
            exist = True
    
    return exist



def delete_view(main_window: QMainWindow, view):
    for i in range(main_window.main_widget.count()):
        widget = main_window.main_widget.widget(i)

        if widget.objectName() == view:
            main_window.main_widget.removeWidget(widget)



def delete_all_views(main_window:QMainWindow):
    for i in reversed(range(main_window.main_widget.count())):
        widget = main_window.main_widget.widget(i)
        
        if widget is None:
            continue
        if widget.objectName() != 'welcome_view':
            main_window.main_widget.removeWidget(widget)
    
    print('after deleting:', main_window.main_widget.count())