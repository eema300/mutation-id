import sys
import os
from PyQt6.QtWidgets import QApplication
from gui import MainWindow

def load_stylesheet():
    path = os.path.join(os.path.dirname(__file__), 'styles', 'styles.qss')
    with open(path, 'r') as style:
        return style.read()

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()