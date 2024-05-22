from controller.ctr_principal import UI
from PyQt6 import QtWidgets

from model.Compra import CompraDB


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = UI()
    window.show()
    app.exec()

 