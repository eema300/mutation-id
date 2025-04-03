from PyQt6.QtWidgets import (QGraphicsView, QGraphicsScene, 
                             QGraphicsRectItem, QGraphicsTextItem)
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtCore import Qt

class SequenceDesign(QGraphicsView):
    nucleotide_colors = {
        'A': QColor('#ff44fc'),
        'C': QColor('#fffd54'),
        'G': QColor('#99ca3e'),
        'T': QColor('#64b9fb'),
        'N': QColor('#c0c0c0'),
        '-': QColor('#ff7878'),
    }

    def __init__(self, sequence_1, sequence_2):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # turn vertical scroll bar off
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # only display loaded sequences
        if sequence_1:
            self.build_seq_graphic(sequence_1, 0)
            
        if sequence_2:
            self.build_seq_graphic(sequence_2, 1)


    def update_size(self):
        self.scene.setSceneRect(0, 0, self.scene.sceneRect().width(), self.scene.sceneRect().height() + 50)

    def build_seq_graphic(self, sequence, row):
        # square cell shape, 20x20 pixels
        cell_size = 40

        # for calculating next cell placement
        col = 0

        for nucleotide in sequence:
            # calculate current position
            col_pos = col * cell_size
            row_pos = row * cell_size

            # get color
            color = self.nucleotide_colors.get(nucleotide, QColor('white'))
            # create shape at position
            cell = QGraphicsRectItem(col_pos, row_pos, cell_size, cell_size)
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

            # increment column
            col += 1

        self.update_size()