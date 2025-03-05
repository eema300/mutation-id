from PyQt6.QtGui import QAction
from PyQt6.Widgets import QFileDialog, QMessageBox


def load_fasta_file():
    pathname, _ = QFileDialog.getOpenFileName("Open File", "", "FASTA Files (*.fasta)")
    if not pathname:
        return
    
    try:
        with open(pathname, 'r') as file:
            sequence = file.read()

    except FileNotFoundError:
        QMessageBox.critical("File Error", "The selected file could not be found")
    except IOError as e:
        QMessageBox.critical("File Error", f"An error occured while reading the file {e}")
    except Exception as e:
        QMessageBox.critical("Error", f"An unexpected error occured {e}")


# extract header and sequence separately
def read_fasta():
    pass


# make sure the header follows the correct format, and that the sequence is
# only A, C, T, G, N
def validate_fasta(header, sequence):
    pass