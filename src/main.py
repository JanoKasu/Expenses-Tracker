from PySide6.QtWidgets import QApplication
from window import window

app = QApplication([])
window = window()
window.show()

app.exec()