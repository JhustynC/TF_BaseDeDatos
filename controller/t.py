from PyQt6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QtWidgets.QPushButton("Press Me!")
        self.setCentralWidget(button)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()