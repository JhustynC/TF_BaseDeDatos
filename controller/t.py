from PyQt6 import QtWidgets
from PyQt6.uic import load_ui
from view import menu_principal



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        load_ui('menu_principal',self)
        self.setWindowTitle("My App")
    


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()