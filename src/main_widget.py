import datetime
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
        self.expenses = expenses_table()
        main_layout.addWidget(self.expenses, 67)

        # Add controls for adding expenses
        vertical_layout = QVBoxLayout()

        self.controls = add_controls()
        self.controls.button_submit.clicked.connect(self.signal_entry_to_table)
        self.controls.button_delete.clicked.connect(self.expenses.delete_table_row)
        vertical_layout.addLayout(self.controls, 50)

        self.chart = pie_chart()
        vertical_layout.addLayout(self.chart, 50)
        
        main_layout.addLayout(vertical_layout, 33)

        self.setLayout(main_layout)

    def signal_entry_to_table(self):
        self.expenses.add_entry_to_table(self.controls.name.text(),
                                         self.controls.amount.text(),
                                         self.controls.type.currentText(),
                                         str(datetime.date.today()))
        self.expenses.repaint()
        self.chart.update_chart(self.controls.type.currentText())
        self.controls.reset()