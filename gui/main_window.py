import os
from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .welcome_view import WelcomeView
from .menu_bar import MenuBar
from .dark_style import dark_stylesheet

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

    def set_dark_mode(self):
        self.setStyleSheet(dark_stylesheet)

    def set_light_mode(self):
        qss_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'styles', 'styles.qss')
        
        with open(qss_path, 'r') as file:
            self.setStyleSheet(file.read())