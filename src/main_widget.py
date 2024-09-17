import pandas as pd
from PySide6.QtWidgets import QWidget, QHBoxLayout
from expenses_table import expenses_table
from add_controls import add_controls

class main_widget(QWidget):
    def __init__(self):
        super().__init__()
        # Add the layout
        main_layout = QHBoxLayout()

        # Add the Expenses Table
        df = pd.read_csv('expenses.csv')
        expenses = expenses_table(df)
        main_layout.addWidget(expenses)

        # Add controls for adding expenses
        controls = add_controls()
        main_layout.addLayout(controls)

        self.setLayout(main_layout)