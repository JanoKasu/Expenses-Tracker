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

        self.button_submit = QPushButton()
        self.button_submit.setText('Submit')

        self.addWidget(self.button_submit)

