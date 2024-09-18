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
		self.types = df['Type'].value_counts().index.tolist()
		self.counts = df['Type'].value_counts(normalize=True).tolist()
		self.series.setHoleSize(0.4)
		self.series.setLabelsVisible(True)

		for type, count in zip(self.types, self.counts):
			if type != 'Income':
				self.series.append(type, count)
		
		self.chart = QChart()
		self.chart.addSeries(self.series)
		self.chart.setTitle('Total Expenses')
		self.chart.legend().hide()
		
		
		self.chart_view = QChartView(self.chart)
		self.chart_view.setRenderHint(QPainter.Antialiasing)
		self.addWidget(self.chart_view)
		self.update()

	def update_chart(self, type):
		if type != 'Income':
			df = pd.read_csv('expenses.csv')
			self.series.clear()
			self.types = df['Type'].value_counts().index.tolist()
			self.counts = df['Type'].value_counts(normalize=True).tolist()

			for type, count in zip(self.types, self.counts):
				self.series.append(type, count)