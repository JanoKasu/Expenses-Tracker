import pandas as pd
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class expenses_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv('expenses.csv')
        self.populate_table()


    def populate_table(self):
        self.df = pd.read_csv('expenses.csv')
        num_rows = len(self.df.index)
        num_cols = len(self.df.columns)
        self.setRowCount(num_rows)
        self.setColumnCount(num_cols)

        headers = self.df.columns.values
        self.setHorizontalHeaderLabels(headers)

        for i in range(num_rows):
            for j in range(num_cols):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iat[i, j])))

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def add_entry_to_table(self, name, amount, type, date):
        name = name.replace(',', '')
        amount = float(amount.replace(',', ''))
        if type != 'Income':
            amount *= -1
        df = pd.read_csv('expenses.csv')
        if df['Balance'].empty:
            balance = 0 if type != 'Income' else amount
        else:
            balance = df['Balance'].iloc[-1] + amount
        # Add entry to the csv
        with open('expenses.csv', 'a') as csv:
            if name and amount and type and date:
                csv.write(f'\n{name},{amount},{type},{date},{balance}')
        # Update the table
        self.populate_table()