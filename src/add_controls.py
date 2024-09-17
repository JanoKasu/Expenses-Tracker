import datetime
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QComboBox, QPushButton

class add_controls(QVBoxLayout):
    def __init__(self):
        super().__init__()
        
        # Add dropdowns for adding expense
        self.name = QTextEdit()
        self.name.setPlaceholderText('Add the name of the expense here')
        self.addWidget(self.name)

        self.amount = QTextEdit()
        self.amount.setPlaceholderText('Add the amount here')
        self.addWidget(self.amount)

        self.type = QComboBox()
        self.type.setPlaceholderText('Type of expense')
        self.type.addItems(['Food', 'Clothing', 'Groceries', 'Income'])
        self.addWidget(self.type)

        self.submit = QPushButton()
        self.submit.setText('Submit')
        # self.submit.clicked.connect(expenses_table.add_entry_to_table)
        # pass these to that slot
        # (self.name.toPlainText(), self.amount.toPlainText(), self.type.currentIndex(), datetime.date.today())
        self.addWidget(self.submit)