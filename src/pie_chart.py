import pandas as pd
from PySide6.QtCharts import QChart, QPieSeries, QChartView
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QPainter

class pie_chart(QVBoxLayout):
	def __init__(self):
		super().__init__()
		self.create_pie_chart()

	def create_pie_chart(self):
		df = pd.read_csv('expenses.csv')
		self.series = QPieSeries()
		self.series.setHoleSize(0.4)
		self.series.setLabelsVisible(True)
		dict = {}

		for type, value in zip(df['Type'], df['Amount']):
			dict[type] = dict[type] + value if type in dict else value

		for key, value in dict.items():
			if type != 'Income':
				self.series.append(key, value)
		
		self.chart = QChart()
		self.chart.addSeries(self.series)
		self.chart.setTitle('Total Expenses')
		self.chart.legend().hide()
		
		
		self.chart_view = QChartView(self.chart)
		self.chart_view.setRenderHint(QPainter.Antialiasing)
		self.addWidget(self.chart_view)
		self.update()

	def update_chart(self, type):
		df = pd.read_csv('expenses.csv')
		df = df[df.Type != 'Income']
		self.series.clear()
		dict = {}

		for type, value in zip(df['Type'], df['Amount']):
			dict[type] = dict[type] + value if type in dict else value

		for key, value in dict.items():
			if type != 'Income':
				self.series.append(key, value)