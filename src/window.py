from main_widget import main_widget
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow

class window(QMainWindow):
    def __init__(self):
        # Initialize the window
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setMinimumSize(QSize(400, 200))
        widget = main_widget()
        self.setCentralWidget(widget)