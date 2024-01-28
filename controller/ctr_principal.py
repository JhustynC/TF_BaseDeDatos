from functools import partial
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6 import uic
from PyQt6.QtCore import QPropertyAnimation
 
class UI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        uic.loadUi('../TF_BaseDeDatos/view/menu_principal.ui' , self)
        
        
        # Boton para mostrar u ocultar el menu
        self.btn_menu.clicked.connect(self.ocultar_menu_lateral)
        
        # Lisata de botones del meu principal
        self.lista_btn_menu = [self.btn_usuario, self.btn_Inmueble, self.btn_transaccion, 
                               self.btn_pendientes, self.btn_historial, self.btn_reportes, self.btn_compra]
        
        # Para mantener el estilo onHover en los botones del menu
        self.btn_transaccion.clicked.connect(partial(self.presionar_boton_menu, self.btn_transaccion.objectName()))
        self.btn_pendientes.clicked.connect(partial(self.presionar_boton_menu, self.btn_pendientes.objectName()))
        self.btn_historial.clicked.connect(partial(self.presionar_boton_menu, self.btn_historial.objectName()))
        self.btn_Inmueble.clicked.connect(partial(self.presionar_boton_menu, self.btn_Inmueble.objectName()))
        self.btn_reportes.clicked.connect(partial(self.presionar_boton_menu, self.btn_reportes.objectName()))
        self.btn_usuario.clicked.connect(partial(self.presionar_boton_menu, self.btn_usuario.objectName()))
        self.btn_compra.clicked.connect(partial(self.presionar_boton_menu, self.btn_compra.objectName()))

        
    def presionar_boton_menu(self, name):  # Para mantener el estilo onHover en los botones del menu

        # Obtenemos le boton del menu que fue presionado
        btn = list(filter(lambda btn: btn.objectName() == name, self.lista_btn_menu))[0]

        # Cambiamos el estilo del boton
        btn.setStyleSheet('background-color:rgb(232, 232, 232);'
                          'color:rgb(0, 0, 0);')

        # Dejamos a los otros botones normales
        for b in self.lista_btn_menu:
            if b is not btn:
                b.setStyleSheet('')

        # Coneccion de botones con paginas
        match name:
            case 'btn_usuario':
                self.paginas__principales.setCurrentWidget(self.pg_Usuarios)
            case 'btn_reportes':
                self.paginas__principales.setCurrentWidget(self.pg_Reportes)
            case 'btn_Inmueble':
                self.paginas__principales.setCurrentWidget(self.pg_Inmueble)
            case 'btn_historial':
                self.paginas__principales.setCurrentWidget(self.pg_HIstorial)
            case 'btn_compra':
                self.paginas__principales.setCurrentWidget(self.pg_Compra)
            case 'btn_pendientes':
                self.paginas__principales.setCurrentWidget(self.pg_Pendientes)
            case 'btn_transaccion':
                self.paginas__principales.setCurrentWidget(self.pg_Transaccion)
    
    def ocultar_menu_lateral(self):
        width = self.fr_botones_menu.width()
        if width == 0:
            extender = 200
        else:
            extender = 0
        self.animacion = QPropertyAnimation(self.fr_botones_menu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animacion.start()

 
app = QtWidgets.QApplication([])
window = UI()
window.show()
app.exec()




