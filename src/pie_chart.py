import pandas as pd
from PySide6.QtCharts import QChart, QPieSeries, QChartView
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QPainter

class pie_chart(QVBoxLayout):
	def __init__(self, df):
		super().__init__()
		self.create_pie_chart(df)

	def create_pie_chart(self, df: pd.DataFrame):
		series = QPieSeries()
		types = df['Type'].value_counts().index.tolist()
		counts = df['Type'].value_counts(normalize=True).tolist()

		for type, count in zip(types, counts):
			series.append(type, count)

		series.setHoleSize(0.4)
		series.setLabelsVisible(True)
		
		chart = QChart()
		chart.addSeries(series)
		chart.setTitle('Expenses')
		chart.legend().hide()
		
		
		chart_view = QChartView(chart)
		chart_view.setRenderHint(QPainter.Antialiasing)
		self.addWidget(chart_view)