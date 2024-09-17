import pandas as pd
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from expenses_table import expenses_table
from add_controls import add_controls
from pie_chart import pie_chart

class main_widget(QWidget):
    def __init__(self):
        super().__init__()
        # Add the layout
        main_layout = QHBoxLayout()

        # Add the Expenses Table
        df = pd.read_csv('expenses.csv')
        expenses = expenses_table(df)
        main_layout.addWidget(expenses, 67)

        # Add controls for adding expenses
        vertical_layout = QVBoxLayout()
        controls = add_controls()
        vertical_layout.addLayout(controls, 50)
        chart = pie_chart(df)
        vertical_layout.addLayout(chart, 50)
        main_layout.addLayout(vertical_layout, 33)

        self.setLayout(main_layout)