import pandas as pd
from PySide6.QtWidgets import QTableWidget
from PySide6.QtCore import Slot

class expenses_table(QTableWidget):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__()
        self.df = dataframe
        self.populate_table()

    def populate_table(self):
        self.setRowCount(len(self.df.index))
        self.setColumnCount(len(self.df.columns))

        headers = self.df.columns.values
        self.setHorizontalHeaderLabels(headers)

    @Slot(str)
    @Slot(str)
    @Slot(str)
    @Slot(str)
    def add_entry_to_table(name, amount, type, date):
        with open('expenses.csv', 'a') as csv:
            name = name.replace(',', '')
            amount = float(amount.replace(',', ''))
            if name and amount and type and date:
                csv.write(f'\n{name},{amount},{type},{date}')