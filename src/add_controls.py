import datetime
from expenses_table import expenses_table
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QComboBox, QPushButton
from PySide6.QtCore import Signal

class add_controls(QVBoxLayout):
    entry = Signal(str, str, str, str)
    
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

        self.button_submit = QPushButton()
        self.button_submit.setText('Submit')
        self.button_submit.clicked.connect(self.add_entry_to_table)
        self.entry.connect(expenses_table.add_entry_to_table)

        self.addWidget(self.button_submit)

    def add_entry_to_table(self):
        print("Adding Entry to Table")
        self.entry.emit(self.name.toPlainText(),
                        self.amount.toPlainText(),
                        self.type.currentText(),
                        str(datetime.date.today())
                        )


        