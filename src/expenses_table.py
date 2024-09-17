import pandas as pd
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QTableWidget

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