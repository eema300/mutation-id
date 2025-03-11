from PyQt6.Widgets import QFileDialog, QMessageBox
import re


# globals
MAX_SEQID_LENGTH = 25
ALLOWED_SEQID_CHARS = ['-', '_', ',', ':', '*', '#']
ALLOWED_SEQ_CHARS = ['A', 'C', 'G', 'T', 'U', 'M', 'R', 'W',
                     'S', 'Y', 'K', 'V', 'H', 'D', 'B', 'N']
AMBIGUOUS_BASE_CODES = ['U', 'M', 'R', 'W', 'S', 'Y',
                        'K', 'V', 'H', 'D', 'B']


def load_fasta_file():
    pathname, _ = QFileDialog.getOpenFileName("Open File", "", "FASTA Files (*.fasta)")
    if not pathname:
        return -1
    
    try:
        with open(pathname, 'r') as file:
            fasta_file = file.read()
            return fasta_file

    except FileNotFoundError:
        QMessageBox.critical("File Error", "The selected file could not be found")
    except IOError as e:
        QMessageBox.critical("File Error", f"An error occured while reading the file {e}")
    except Exception as e:
        QMessageBox.critical("Error", f"An unexpected error occured {e}")
    
    return -1


# extract header and sequence separately
def read_fasta(fasta_file):
    try:
        # first line is header, subsequent lines are the sequence, pass to array
        fasta = fasta_file.split('\n')
        header = fasta[0]
        sequence = " ".join(fasta[1:])

        return header, sequence

    except IndexError:
        QMessageBox.critical("Error", "File was empty.")


'''
NCBI sequence ID should:
    - not contain any spaces
    - be 25 characters or less
    - only include letters, digits, hyphens (-), underscores (_), 
    periods (.), colons (:), asterisks (*), and/or number signs (#)
'''
# validate sequence id
def validate_seq_id(seqid):
    # empty
    if not seqid:
        return False

    # spaces?
    if ' ' in seqid:
        return False
    
    # 25 chars or less?
    if len(seqid) > 25:
        return False
    
    # allowed chars or alphanumeric?
    for letter in seqid:
        if not bool(re.match(r"\w", letter)) or letter not in ALLOWED_SEQID_CHARS:
            return False
    
    # if no problems, sequence id is valid
    return True


# validate fasta header
def validate_fasta_header(header):
    # empty
    if not header:
        return False
    
    # mandatory starting character
    if header[0] != '>':
        return False

    # extract sequence ID
    seqid = header[1:].split(' ')[0]

    validate_seq_id(seqid)
    
    # if no problems, header is valid
    return True


# validate fasta sequence
# only A, C, G, T, U, M, R, W, S, Y, K, V, H, D, B, N
def validate_fasta_sequence(sequence):
    # empty
    if not sequence:
        return False
    
    # check sequence for valid nucleotides
    for nucleotide in sequence:
        if nucleotide not in ALLOWED_SEQ_CHARS:
            return False
        
    # if no problems, sequence is valid
    return True


def validate_fasta(header, sequence):
    # validate header
    if not validate_fasta_header(header):
        QMessageBox.critical("Invalid Header", "The FASTA header is invalid.")

    # validate sequence
    if not validate_fasta_sequence(sequence):
        QMessageBox.critical("Invalid Sequence", "The FASTA sequence is invalid.")
    
    # if no problems, fasta is valid


# update ambiguous base codes to be N's
def update_ambiguous_codes(sequence):
    updated_sequence = ''.join(['N' if nucleotide in AMBIGUOUS_BASE_CODES 
                                else nucleotide for nucleotide in sequence])
    return updated_sequence