from PyQt6.QtWidgets import QGraphicsScene, QFileDialog, QMessageBox, QMainWindow
from PyQt6.QtGui import QImage, QPainter

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
    print(filename)
    pathname, _ = QFileDialog.getSaveFileName(None, 'Save FASTA', filename, "FASTA Files (*.fasta)")

    if not pathname:
        return
    
    try:
        with open(pathname, 'w') as file:
            file.write(fasta)

    except Exception as e:
        QMessageBox(main_window, "Error", f"An unexpected error occured {e}")