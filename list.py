from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel

app = QApplication([])
model = QStringListModel([
    "An element", "Another element", "And another one."
])
view = QListView()
view.setModel(model)
view.show()
app.exec_() 