from PyQt6.QtWidgets import QGraphicsScene, QFileDialog, QMessageBox, QMainWindow
from PyQt6.QtGui import QImage, QPainter
import matplotlib.pyplot as plt
from .loc_mutation import loc_mutation_types

def export_png(main_window: QMainWindow, scene: QGraphicsScene, 
               seqid_WT, seqid_MT):
    width = scene.sceneRect().width()
    height = scene.sceneRect().height()

    image = QImage(int(width), int(height), QImage.Format.Format_ARGB32)

    painter = QPainter(image)
    scene.render(painter)
    painter.end()

    filename = '-'.join([seqid_WT, seqid_MT, 'alignment']) + '.png'
    pathname, _ = QFileDialog.getSaveFileName(None, 'Save Image', filename, "PNG Files (*.png)")

    if not pathname:
        return
    
    try:
        image.save(pathname)

    except Exception as e:
        QMessageBox(main_window, "Error", f"An unexpected error occured {e}")



def export_fasta(main_window: QMainWindow,
                 seqid_WT, seqid_MT, 
                 aligned_sequence_WT, aligned_sequence_MT):

    # create string
    fasta = '\n'.join(['>' + seqid_WT, aligned_sequence_WT, 
                       '>' + seqid_MT, aligned_sequence_MT])


    # save file
    filename = '-'.join([seqid_WT, seqid_MT, 'alignment']) + '.fasta'
    pathname, _ = QFileDialog.getSaveFileName(None, 'Save FASTA', filename, "FASTA Files (*.fasta)")

    if not pathname:
        return
    
    try:
        with open(pathname, 'w') as file:
            file.write(fasta)

    except Exception as e:
        QMessageBox(main_window, "Error", f"An unexpected error occured {e}")

    
def export_csv(main_window: QMainWindow,
               seqid_WT, seqid_MT,
               aligned_sequence_WT, aligned_sequence_MT):
    
    # get positions
    positions = loc_mutation_types(aligned_sequence_WT, aligned_sequence_MT)
    
    if positions:
        # write csv
        csv = 'base, position, type\n'
        for position in positions:
            csv += ','.join([aligned_sequence_MT[int(position)], str(position), positions[position]+'\n'])
        
        # save file
        filename = '-'.join([seqid_WT, seqid_MT, 'mutations']) + '.csv'
        pathname, _ = QFileDialog.getSaveFileName(None, 'Save CSV', filename, "CSV Files (*.csv)")

        if not pathname:
            return
        
        try:
            with open(pathname, 'w') as file:
                file.write(csv)
        
        except Exception as e:
            QMessageBox(main_window, "Error", f"An unexpected error occured {e}")


def export_png_graph(main_window: QMainWindow, graph):
    # set filename
    graph_name = graph.objectName()
    filename = ''.join([graph_name, '.png'])
    
    # allow user to change filename and location to save
    pathname, _ = QFileDialog.getSaveFileName(None, 
                                                f"Save {graph_name}", 
                                                filename, 
                                                "PNG Files (*.png)")
    if not pathname:
        return
    
    try:
        graph.savefig(pathname)
    
    except Exception as e:
        QMessageBox(main_window, "Error", f"An unexpected error occured {e}")


def export_png_all_graphs(main_window: QMainWindow, graphs,
                          seqid_WT, seqid_MT):
    # graph names
    graph_names = [''.join([seqid_WT, '_nucleotide_counts']),
                   ''.join([seqid_MT, '_nucleotide_counts']),
                   'mutation_density']

    # set filenames
    filenames = [''.join([graph_name, '.png']) for graph_name in graph_names]
    
    # iterate through each graph and save
    for fig, graph_name, filename in zip(graphs, graph_names, filenames):
        # allow user to change filename and location to save
        pathname, _ = QFileDialog.getSaveFileName(None, 
                                                  f"Save {graph_name}", 
                                                  filename, 
                                                  "PNG Files (*.png)")
        if not pathname:
            return
        
        try:
            fig.savefig(pathname)
        
        except Exception as e:
            QMessageBox(main_window, "Error", f"An unexpected error occured {e}")