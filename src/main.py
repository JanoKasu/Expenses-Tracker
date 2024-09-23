from PySide6.QtWidgets import QApplication
from window import window

if __name__ == '__main__':
	try:
		open('expenses.csv', 'r')
	except FileNotFoundError:
		f = open('expenses.csv', 'x')
		f.write('Name,Amount,Type,Date,Balance')
		f.close()
	app = QApplication([])
	window = window()
	window.show()
	app.exec()
