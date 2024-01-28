from view.menu_principal import Ui_MenuPrincipal
from functools import partial
from PyQt6 import QtWidgets, QtCore
from PyQt6 import uic
from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem, QTableWidgetSelectionRange, QDialog

 
class UI(QtWidgets.QMainWindow, Ui_MenuPrincipal):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        #uic.loadUi('../TF_BaseDeDatos/view/menu_principal.ui' , self)
        self.setupUi(self)
        
        #*Boton para mostrar u ocultar el menu
        self.btn_menu.clicked.connect(self.ocultar_menu_lateral)
        
        #*Listar de botones del meu principal
        self.lista_btn_menu = [self.btn_usuario, self.btn_Inmueble, self.btn_transaccion, 
                               self.btn_pendientes, self.btn_historial, self.btn_reportes, self.btn_compra]
        
        #*Para mantener el estilo onHover en los botones del menu
        self.btn_transaccion.clicked.connect(partial(self.presionar_boton_menu, self.btn_transaccion.objectName()))
        self.btn_pendientes.clicked.connect(partial(self.presionar_boton_menu, self.btn_pendientes.objectName()))
        self.btn_historial.clicked.connect(partial(self.presionar_boton_menu, self.btn_historial.objectName()))
        self.btn_Inmueble.clicked.connect(partial(self.presionar_boton_menu, self.btn_Inmueble.objectName()))
        self.btn_reportes.clicked.connect(partial(self.presionar_boton_menu, self.btn_reportes.objectName()))
        self.btn_usuario.clicked.connect(partial(self.presionar_boton_menu, self.btn_usuario.objectName()))
        self.btn_compra.clicked.connect(partial(self.presionar_boton_menu, self.btn_compra.objectName()))
        
        #*Boton seleccionado de la primera pagina
        self.presionar_boton_menu('btn_usuario')
    
        
        #*Para que el menueste escondido
        self.fr_botones_menu.setFixedWidth(0)
        
        #Para salir del sistema
        self.btn_salir.clicked.connect(self.close)
        
        #*Para reescalar columnas de las tablas y centrarlas 
        #self.tbl_.horizontalHeader().setVisible(True)
        self.tbl_usuario.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_inmueble.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_pendientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_porcentaje.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_desempenio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_ventas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_historial.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        #*Pare seleccionar la fila completa de una tabla a la hora de dar click
        self.tbl_usuario.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_usuario))
        self.tbl_inmueble.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_inmueble))
        self.tbl_pendientes.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_pendientes))
        self.tbl_porcentaje.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_porcentaje))
        self.tbl_desempenio.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_desempenio))
        self.tbl_ventas.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_ventas))
        self.tbl_historial.itemClicked.connect(partial(self.seleccionar_fila_completa_tabla, self.tbl_historial))
        
        
  
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

 
    def llenar_tabla(self, tabla, datos):
        tabla.setRowCount(len(datos)) 
        for i, fila in enumerate(datos):
            for j, columna in enumerate(fila):
                elemento = QTableWidgetItem(str(columna))
                elemento.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                tabla.setItem(i, j, elemento)
    
    
    def seleccionar_fila_completa_tabla(self, tabla, item):
        # Coordenas de la fila
        row = item.row()
        print(f"{item.row()}, {item.column()}")

        # Seleccionar la fila completa
        tabla.setRangeSelected(
            QTableWidgetSelectionRange(row, 0, row, self.tabla.columnCount() - 1),
            True  # True para seleccionar toda la fila
        )

        # Seleccionar el elemento de la primera columna
        selected_row = self.tabla.currentRow()
        item_primera_columna = self.tabla.item(selected_row, 0)
        ID = item_primera_columna.text()



