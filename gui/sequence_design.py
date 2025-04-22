from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene, 
                             QGraphicsRectItem, QGraphicsTextItem)
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtCore import Qt
from logic import find_sub_mutation

class SequenceDesign(QGraphicsView):

    cell_size = 40

    def __init__(self, sequence_1, sequence_2, mutation):
        super().__init__()
        self.nucleotide_colors = {
            'A': QColor('#ff44fc'),
            'C': QColor('#fffd54'),
            'G': QColor('#99ca3e'),
            'T': QColor('#64b9fb'),
            'N': QColor('#c0c0c0'),
            '-': QColor('#ffffff'),
        }

        if mutation:
            self.nucleotide_colors['-'] = QColor('#ff7878')
            self.sub_mutation_positions = find_sub_mutation(sequence_1, sequence_2)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # turn vertical scroll bar off
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFixedHeight(125)

        # only display loaded sequences
        if sequence_1:
            self.build_seq_graphic(sequence_1, 0.1, mutation=False)
            
        if sequence_2:
            self.build_seq_graphic(sequence_2, 1.25, mutation)

        self.scene.setSceneRect(0, 0, self.scene.sceneRect().width() + 20, 105)


    def build_seq_graphic(self, sequence, row, mutation):
        # for calculating next cell placement
        col = 0.25
        # helper index for using the find_sub_mutation function
        i = 0

        for nucleotide in sequence:
            # calculate current position
            col_pos = col * self.cell_size
            row_pos = row * self.cell_size

            # get color
            if mutation and i in self.sub_mutation_positions:
                color = QColor('#ff7878')
            else:
                color = self.nucleotide_colors.get(nucleotide, QColor('white'))
            
            # create shape at position
            cell = QGraphicsRectItem(col_pos, row_pos, self.cell_size, self.cell_size)
            # set color
            cell.setBrush(QBrush(color))
            # add shape
            self.scene.addItem(cell)

            # get text
            if nucleotide == '-':
                text = QGraphicsTextItem('')
            else:
                text = QGraphicsTextItem(nucleotide)
            # set text
            text.setPos(col_pos + 10, row_pos + 10)
            # add text
            self.scene.addItem(text)

            # increment column and helper index
            col += 1
            i += 1


    # NEED TO USE find_sub_mutation TO UPDATE COLOR OF THOSE MUTATIONS IN MUTATION VIEW