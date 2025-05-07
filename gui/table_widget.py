from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont, QBrush
from PyQt6.QtCore import pyqtSignal
from logic import get_gc_content, get_base_proportion, find_repeats, get_mutation_types, find_insertion_mutations, find_deletion_mutations, find_sub_mutation

class Table(QTableWidget):
    def __init__(self, main_window, mutation, sequence_wt, sequence_mt):
        super().__init__()

        # save these to access in function later
        self.main_window = main_window
        self.mutation = mutation
        self.sequence_1 = sequence_wt
        self.sequence_2 = sequence_mt

        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()
        clicked = pyqtSignal(int, int)
        self.setFixedWidth(340)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.setRowCount(14)
        self.setColumnCount(3)

        self.horizontalHeader().setFixedHeight(30)

        self.cell_height = self.verticalHeader().defaultSectionSize()
        self.header_height = self.horizontalHeader().height()

        self.setFixedHeight(2 + self.header_height + self.cell_height * 14)

        # length
        self.setItem(0, 0, QTableWidgetItem("GC Content"))
        self.setItem(0, 1, QTableWidgetItem(get_gc_content(sequence_wt)))
        self.setItem(0, 2, QTableWidgetItem(get_gc_content(sequence_mt)))

        # gc content
        self.setItem(1, 0, QTableWidgetItem("Length"))
        self.setItem(1, 1, QTableWidgetItem(str(len(sequence_wt.replace('-', '')))))
        self.setItem(1, 2, QTableWidgetItem(str(len(sequence_mt.replace('-', '')))))

        # base proportions
        self.setItem(2, 0, QTableWidgetItem("A"))
        self.setItem(2, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'A')))
        self.setItem(2, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'A')))
        self.setItem(3, 0, QTableWidgetItem("T"))
        self.setItem(3, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'T')))
        self.setItem(3, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'T')))
        self.setItem(4, 0, QTableWidgetItem("G"))
        self.setItem(4, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'G')))
        self.setItem(4, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'G')))
        self.setItem(5, 0, QTableWidgetItem("C"))
        self.setItem(5, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'C')))
        self.setItem(5, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'C')))

        # repeat content
        self.setItem(6, 0, QTableWidgetItem("Repeat Content"))
        self.setItem(6, 1, QTableWidgetItem(find_repeats(sequence_wt)))
        self.setItem(6, 2, QTableWidgetItem(find_repeats(sequence_mt)))

        # mutation types
        if mutation:
            mutation_types = get_mutation_types(sequence_wt, sequence_mt)
            self.setItem(7, 0, QTableWidgetItem("Deletions"))
            self.item(7, 0).setToolTip("Click to highlight deletion mutations")
            self.setItem(7, 2, QTableWidgetItem(str(mutation_types['deletion'])))
            self.setItem(8, 0, QTableWidgetItem("Substitutions"))
            self.item(8, 0).setToolTip("Click to highlight substitution mutations")
            self.setItem(8, 2, QTableWidgetItem(str(mutation_types['substitution'])))
            self.setItem(9, 0, QTableWidgetItem("Insertions"))
            self.item(9, 0).setToolTip("Click to highlight insertion mutations")
            self.setItem(9, 2, QTableWidgetItem(str(mutation_types['insertion'])))
            self.cellClicked.connect(self.handle_cell_click)

        # colnames
        self.setHorizontalHeaderLabels(['Summary', 'Reference', 'Mutated'])
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)

        for col in range(self.columnCount()):
            item = self.horizontalHeaderItem(col)
            item.setFont(font)
            item.setBackground(QBrush(QColor("#383b42")))
            item.setForeground(QBrush(QColor("white")))

        self.verticalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.setAlternatingRowColors(True)

        def mousePressEvent(self, event):
            index = self.indexAt(event.pos())
            if index.isValid():
                self.clicked.emit(index.row(), index.column())
            super().mousePressEvent(event)


    def handle_cell_click(self, row, column):
        item = self.item(row, column)
        
        # deletions
        if item and row == 7 and column == 0:
            positions = find_deletion_mutations(self.sequence_1, self.sequence_2)
            if item.background().color() == QColor("black"):
                # change cell color back to normal
                item.setBackground(QColor('#f1f1f1'))
                item.setForeground(QBrush(QColor("black")))
                # clear filter
                self.main_window.main_widget.currentWidget().sequence_design.clear_highlight(self.sequence_2, positions)
            else:
                # change cell color to indicate filter on
                item.setBackground(QColor("black"))
                item.setForeground(QBrush(QColor("white")))
                # apply filter
                self.main_window.main_widget.currentWidget().sequence_design.highlight_mutations(self.sequence_2, positions)

        # substitutions
        elif item and row == 8 and column == 0:
            positions = find_sub_mutation(self.sequence_1, self.sequence_2)
            if item.background().color() == QColor("black"):
                # change cell color back to normal
                item.setBackground(QColor('white'))
                item.setForeground(QBrush(QColor("black")))
                # clear filter
                self.main_window.main_widget.currentWidget().sequence_design.clear_highlight(self.sequence_2, positions)
            else:
                # change cell color to indicate filter on
                item.setBackground(QColor("black"))
                item.setForeground(QBrush(QColor("white")))
                # apply filter
                self.main_window.main_widget.currentWidget().sequence_design.highlight_mutations(self.sequence_2, positions)
        
        # insertions
        elif item and row == 9 and column == 0:
            positions = find_insertion_mutations(self.sequence_1, self.sequence_2)
            if item.background().color() == QColor("black"):
                # change cell color back to normal
                item.setBackground(QColor('#f1f1f1'))
                item.setForeground(QBrush(QColor("black")))
                # clear filter
                self.main_window.main_widget.currentWidget().sequence_design.clear_highlight(self.sequence_2, positions)
            else:
                # change cell color to indicate filter on
                item.setBackground(QColor("black"))
                item.setForeground(QBrush(QColor("white")))
                # apply filter
                self.main_window.main_widget.currentWidget().sequence_design.highlight_mutations(self.sequence_2, positions)
        
        # no mutation type clicked, don't do anything
        else:
            return