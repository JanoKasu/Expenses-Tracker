import re
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLineEdit

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

        horizontal_layout = QHBoxLayout()

        self.button_submit = QPushButton()
        self.button_submit.setText('Submit')
        horizontal_layout.addWidget(self.button_submit)

        self.button_delete = QPushButton()
        self.button_delete.setText('Delete Row')
        horizontal_layout.addWidget(self.button_delete)

        self.addLayout(horizontal_layout)


    def reset(self):
        self.name.setText('')
        self.amount.setText('')
        self.type.setCurrentIndex(-1)