import pandas as pd
import datetime
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Signal
from expenses_table import expenses_table
from add_controls import add_controls
from pie_chart import pie_chart

class main_widget(QWidget):
    add_table_entry = Signal(str, str, str, str)

    def __init__(self):
        super().__init__()
        # Add the layout
        main_layout = QHBoxLayout()

        # Add the Expenses Table
        df = pd.read_csv('expenses.csv')
        self.expenses = expenses_table()
        main_layout.addWidget(self.expenses, 67)

        # Add controls for adding expenses
        vertical_layout = QVBoxLayout()

        self.controls = add_controls()
        self.controls.button_submit.clicked.connect(self.signal_entry_to_table)
        vertical_layout.addLayout(self.controls, 50)

        chart = pie_chart(df)
        vertical_layout.addLayout(chart, 50)
        
        main_layout.addLayout(vertical_layout, 33)

        self.setLayout(main_layout)

    def signal_entry_to_table(self):
        self.expenses.add_entry_to_table(self.controls.name.toPlainText(),
                                         self.controls.amount.toPlainText(),
                                         self.controls.type.currentText(),
                                         str(datetime.date.today()))
        self.repaint()


        