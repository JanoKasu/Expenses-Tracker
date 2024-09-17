from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QComboBox, QPushButton

class add_controls(QVBoxLayout):
    def __init__(self):
        super().__init__()
        
        # Add dropdowns for adding expense
        name = QTextEdit()
        name.setPlaceholderText('Add the name of the expense here')
        self.addWidget(name)

        amount = QTextEdit()
        amount.setPlaceholderText('Add the amount here')
        self.addWidget(amount)

        type = QComboBox()
        type.addItems(['Food', 'Clothing', 'Groceries'])
        self.addWidget(type)

        submit = QPushButton()
        submit.setText('Submit')
        self.addWidget(submit)
