import sys

from PyQt6.QtCore import QSize, Qt, QCoreApplication, QThread, pyqtSignal, QSettings
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                            QFileDialog, QHBoxLayout, QPushButton,
                            QWidget, QFrame, QVBoxLayout, QGroupBox, QTextEdit, QProgressBar, QLabel, QTabWidget, QSplitter, QStatusBar, QTableWidget, QTableWidgetItem, QCheckBox)
from PyQt6.QtGui import QAction, QIcon, QMovie
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

class AlignmentThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(object)

    def __init__(self, wt_sequence, mutant_sequence):
        super().__init__()
        self.wt_sequence = wt_sequence
        self.mutant_sequence = mutant_sequence

    def run(self):
        from Bio import pairwise2
        


    #Perform Sequence Alignment
        alignments = pairwise2.align.globalxx(self.wt_sequence, self.mutant_sequence)
        best_alignment = alignments[0] if alignments else None

    #Emit Progress Updates
        for i in range(101):
            self.progress.emit(i)
            self.msleep(50)

        self.finished.emit(best_alignment)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window and layout
        self.setWindowTitle("Mutation id")
        self.setMinimumSize(1150, 650)
        self.dark_mode = False
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)

        #Status Bar
        self.statusBar().showMessage("Ready")

        #Tab Widget for Sections
        self.tabs = QTabWidget()
        load_tab = QWidget()
        align_tab = QWidget()
        self.tabs.addTab(load_tab, "Load Sequences")
        self.tabs.addTab(align_tab, "Alignment")

        # side panel layout
        side_panel = QFrame()
        side_panel.setFrameShape(QFrame.Shape.StyledPanel)
        side_panel.setFixedWidth(250)
        side_panel_layout = QVBoxLayout()
        side_panel_layout.setContentsMargins(5, 5, 5, 5)
        side_panel_layout.setSpacing(10)

        #Group Box for Loading Sequences
        load_group = QGroupBox("Load Sequences")
        load_group_layout = QVBoxLayout()

        self.load_wt_button = QPushButton("Load Wild Type FASTA")
        self.load_mutation_button = QPushButton("Load Mutated Sequence FASTA")
        self.load_wt_button.setToolTip("Click to load a Wild Type FASTA file")
        self.load_mutation_button.setToolTip("Click to load a Mutated FASTA file")
        self.load_wt_button.clicked.connect(lambda: self.load_fasta_file("WT"))
        self.load_mutation_button.clicked.connect(lambda: self.load_fasta_file("Mutant"))

        load_group_layout.addWidget(self.load_wt_button)
        load_group_layout.addWidget(self.load_mutation_button)
        load_group.setLayout(load_group_layout)

        side_panel_layout.addWidget(load_group)
        side_panel_layout.addStretch(1)
        
        side_panel.setLayout(side_panel_layout)
        #Collapsible Side Panel
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(side_panel)
        splitter.addWidget(self.tabs)
        splitter.setStretchFactor(1, 5)
        main_layout.addWidget(splitter)

        # central area layout
        central_area = QFrame()
        central_area_layout = QVBoxLayout()

        central_area.setLayout(central_area_layout)
        main_layout.addWidget(central_area, stretch=1)

        # set main layout
        main_layout.addWidget(self.tabs, stretch=1)
        central_widget.setLayout(main_layout)

        #Load Tab Layout
        load_tab_layout = QVBoxLayout()
        self.wt_textbox = QTextEdit()
        self.wt_textbox.setReadOnly(True)
        self.mutant_textbox = QTextEdit()
        self.mutant_textbox.setReadOnly(True)

        load_tab_layout.addWidget(QLabel("Wild Type Sequence:"))
        load_tab_layout.addWidget(self.wt_textbox)
        load_tab_layout.addWidget(QLabel("Mutated Sequence:"))
        load_tab_layout.addWidget(self.mutant_textbox)
        load_tab.setLayout(load_tab_layout)

        #Alignment Tab Layout
        align_tab_layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.loading_label = QLabel()
        self.loading_label.hide()
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setFontFamily("Courier New")
        self.result_display.setFontPointSize(12)
        self.result_display.setMinimumHeight(300)
        #New Run Alignment Button
        self.run_alignment_button = QPushButton("Run Alignment")
        self.run_alignment_button.setToolTip("Click to run sequence alignment")
        self.run_alignment_button.clicked.connect(self.run_alignment)
        align_tab_layout.addWidget(QLabel("Alignment Progress:"))
        align_tab_layout.addWidget(self.progress_bar)
        align_tab_layout.addWidget(self.loading_label)
        align_tab_layout.addWidget(QLabel("Alignment Results:"))
        align_tab_layout.addWidget(self.result_display)
        align_tab_layout.addWidget(self.run_alignment_button)
        align_tab.setLayout(align_tab_layout)
        self.save_results_button = QPushButton("Save Results")
        self.save_results_button.clicked.connect(self.save_results)

        align_tab_layout.addWidget(self.save_results_button)

        
        # menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        run_menu = menu_bar.addMenu("Run")

        load_wt_action = QAction("Load WT FASTA", self)
        load_wt_action.triggered.connect(lambda: self.load_fasta_file("WT"))

        load_mutation_action = QAction("Load Mutated FASTA", self)
        load_mutation_action.triggered.connect(lambda: self.load_fasta_file("Mutant"))

        alignment_action = QAction("Run Alignment", self)
        alignment_action.triggered.connect(self.run_alignment)
        theme_action = QAction("Toggle Dark Mode", self)
        theme_action.triggered.connect(self.toggle_theme)

        file_menu.addAction(load_wt_action)
        file_menu.addAction(load_mutation_action)
        run_menu.addAction(alignment_action)
        menu_bar.addAction(theme_action)


        #Apply Styles
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                border-radius: 8px;
                padding: 8px;
                border: 2px solid transparent;
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 2px solid #1f618d;
            }
            QTextEdit {
                background-color: #ecf0f1;
                font-size: 14px;
                border-radius: 5px;
                padding: 5px;
            }
            QProgressBar {
                border: 2px solid #2980b9;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                width: 10px;
            }
        """)

    def toggle_theme(self):
        if self.dark_mode:
            self.setStyleSheet("")
            self.dark_mode = False
        else:
            self.setStyleSheet("""
                QWidget { background-color: #2c3e50; color: white;}
                QPushButton { background-color: #34495e; color: white; border-radius: 5px; padding: 5px;}
                QTextEdit { background-color: #95a5a6; color: black;}
            """)
            self.dark_mode = True

    def load_fasta_file(self, sequence_type):
        pathname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "FASTA Files (*.fasta)")
        if not pathname:
            return
        
        
        try:
            with open(pathname, 'r') as file:
                sequence = file.read()

            if not sequence.startswith(">"):
                QMessageBox.warning(self, "Invalid File", "The selected file is not a valid FASTA file.")
                return

            if sequence_type == "WT":
                self.wt_textbox.setText(sequence)
            else:
                self.mutant_textbox.setText(sequence)
            
            self.statusBar().showMessage(f"Loaded {sequence_type} sequence successfully")
                

        except FileNotFoundError:
            QMessageBox.critical(self, "File Error", "The selected file could not be found")
        except IOError as e:
            QMessageBox.critical(self, "File Error", f"An error occured while reading the file {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occured {e}")

    def save_results(self):
             options = QFileDialog.Options()
             file_path, _ = QFileDialog.getSaveFileName(self, "Save Alignment Results", "", "Text Files (*.txt);;All Files (*)", options=options)

             if file_path:
                try:
                    with open(file_path, "w") as file:
                            file.write(self.result_display.toPlainText())  # Assuming results are stored here
                            self.statusBar().showMessage("Results saved successfully!")
                except Exception as e:
                        QMessageBox.critical(self, "Error", f"Failed to save results: {e}")


    def run_alignment(self):
         wt_text = self.wt_textbox.toPlainText().split("\n", 1)[-1].replace("\n", "")
         mutant_text = self.mutant_textbox.toPlainText().split("\n", 1)[-1].replace("\n", "")

         if not wt_text or not mutant_text:
             QMessageBox.warning(self, "Error", "Both sequences must be loaded before running alignment.")
             return
         

         self.statusBar().showMessage("Alignment in progress...")
         self.loading_label.show()
         self.progress_bar.setValue(0)
         self.thread = AlignmentThread(wt_text, mutant_text)
         self.thread.progress.connect(self.progress_bar.setValue)
         self.thread.finished.connect(self.alignment_done)
         self.thread.start()

    def alignment_done(self, best_alignment):
        self.loading_label.hide()
        
        if best_alignment:
            from Bio.pairwise2 import format_alignment
            #Format the alignment using HTML
            aligned_seq1, aligned_seq2, score, begin, end = best_alignment
            #Initialize an empty result for the HTML formatted alignment
            html_result = "<pre>"

            #Compare each character and highlight mismatches
            for c1, c2 in zip(aligned_seq1, aligned_seq2):
                if c1 == c2:
                    html_result += f"<span style='color: green;'>{c1}</span>"
                else:
                    html_result += f"<span style='color: red;'>{c1}</span>"

            html_result += "</pre>"

            self.result_display.setHtml(html_result)
            QMessageBox.information(self, "Success", f"Alignment Completed!\n\n{format_alignment(*best_alignment)}")
        else:
            QMessageBox.warning(self, "Warning", "No alignment found.")

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()