# need a state variable that changes every time
# you add a sequence using the file loader
# it needs to go from 0 to 1 to 2 and then decrease
# as such when user deletes a sequence

from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .welcome_view import WelcomeView
from .menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window and layout
        self.setWindowTitle("mutation id")
        self.setMinimumSize(1275, 650)
        # stacked widget for switching between views
        self.main_widget = QStackedWidget()
        self.setCentralWidget(self.main_widget)

        # view on entry of program
        welcome_view = WelcomeView(self)

        # add view to stacked widget
        self.main_widget.addWidget(welcome_view)

        # menu bar
        menu_bar = MenuBar(self)
        self.setMenuBar(menu_bar)