import re
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QLineEdit

class add_controls(QVBoxLayout):
    
    def __init__(self):
        super().__init__()

        # Add dropdowns for adding expense
        self.name = QLineEdit()
        self.name.setPlaceholderText('Add the name of the expense here')
        self.addWidget(self.name)

        self.amount = QLineEdit()
        self.amount.setPlaceholderText('Add the amount here')
        validator = QRegularExpressionValidator(QRegularExpression('^[0-9.]+'))
        self.amount.setValidator(validator)
        self.addWidget(self.amount)

        self.type = QComboBox()
        self.type.setPlaceholderText('Type of expense')
        self.type.addItems(['Food', 'Clothing', 'Groceries', 'Income'])
        self.addWidget(self.type)

        self.button_submit = QPushButton()
        self.button_submit.setText('Submit')
        self.addWidget(self.button_submit)


    def reset(self):
        self.name.setText('')
        self.amount.setText('')
        self.type.setCurrentIndex(-1)

