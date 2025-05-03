from PyQt6.QtWidgets import QGraphicsScene, QFileDialog, QMessageBox, QMainWindow
from PyQt6.QtGui import QImage, QPainter
import matplotlib.pyplot as plt
from .loc_mutation import find_sub_mutation

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
    positions = find_sub_mutation(aligned_sequence_WT, aligned_sequence_MT)
    for i in range(len(aligned_sequence_MT)):
        if aligned_sequence_MT[i] == '-':
            positions.append(i)


    if positions:
        # sort the list in ascending order to make for a neater csv
        positions.sort()

        # write csv
        csv = 'base, position\n'
        for position in positions:
            csv += ','.join([aligned_sequence_MT[position], str(position)+'\n'])
        
        
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