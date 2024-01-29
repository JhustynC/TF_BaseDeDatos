from controller.ctr_principal import UI
from PyQt6 import QtWidgets

from model.Compra import CompraDB

app = QtWidgets.QApplication([])
window = UI()
window.show()
app.exec()

