from model.Conectar import Conectar
from view.menu_principal import Ui_MenuPrincipal
from model.Persona import PersonaDB
from model.Inmueble import InmuebleDB
from functools import partial
from PyQt6 import QtWidgets, QtCore
from PyQt6 import uic
from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem, QTableWidgetSelectionRange, QListWidgetItem

 
class UI(QtWidgets.QMainWindow, Ui_MenuPrincipal):
    
    primera_colum = ""
    fila_tabla = None
    ciudad_parroquias = {
    'CUENCA': [
        'Cuenca', 'Bellavista', 'Cañaribamba', 'El Batán', 'El Sagrario', 'El Vecino',
        'Gil Ramírez Dávalos', 'Huayna Cápac', 'Machángara', 'Monay', 'San Blas', 'San Sebastián',
        'Sucre', 'Totoracocha', 'Yanuncay', 'Hermano Miguel', 'Baños', 'Chaucha', 'Checa (Jidcay)',
        'Chiquintad', 'Cumbe', 'El Valle', 'Llacao', 'Molleturo', 'Nulti', 'Octavio Cordero Palacios (Santa Rosa)',
        'Paccha', 'Quingeo', 'Ricaurte', 'San Joaquín', 'Santa Ana', 'Sayausí', 'Sidcay', 'Sinincay',
        'Tarqui', 'Turi', 'Portete (Irquis)'
    ],
    'GUALACEO': [
        'Gualaceo', 'Daniel Córdova Toral (Oriente)', 'Jadán', 'Luís Cordero Vega',
        'Mariano Moreno', 'Remigio Crespo Toral (Gúlag)', 'San Juan', 'Zhidmad', 'Simón Bolívar (Gañanzol)'
    ],
    'PAUTE': [
        'Paute Bulán (José Víctor Izquierdo)', 'Chicán (Guillermo Ortega)', 'Dugdug',
        'El Cabo', 'Guarainag', 'San Cristóbal (Carlos Ordóñez Lazo)', 'Tomebamba'
    ],
    'GIRÓN': [
        'Girón', 'Asunción', 'San Gerardo'
    ],
    'Sta. ISABEL': [
        'Santa Isabel', 'Adbón Calderón (La unión)', 'Zhaglli (Shaglli)'
    ],
    'SÍGSIG': [
        'Sígsig', 'Cuchil (Cutchil)', 'Jima (Gima)', '-güel', 'Ludo', 'San Bartolomé', 'San José de Raranga'
    ],
    'Sn. FERNANDO': [
        'San Fernando Chumblín'
    ],
    'NABÓN': [
        'Nabón', 'Cochapata', 'El Progreso', 'Las Nieves (Chaya)'
    ],
    'PUCARÁ': [
        'Pucará San Rafael de Sharug'
    ],
    'OÑA': [
        'San Felipe de Oña Susudel'
    ],
    'CHORDELEG': [
        'Chordeleg', 'La unión', 'Luis Gallarza Orellana (Delegsol)', 'Principal', 'San Martín de Puzhío'
    ],
    'EL PAN': [
        'El pan', 'San Vicente'
    ],
    'SEVILLA DE ORO': [
        'Sevilla de Oro Amaluza', 'Palmas'
    ],
    'GUACHAPALA': [
        'Guachapala'
    ],
    'CAMILO PONCE ENRÍQUEZ': [
        'Camilo Ponce Enríquez El Carmen de Pujilí'
    ]
}
    
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        #?uic.loadUi('../TF_BaseDeDatos/view/menu_principal.ui' , self)
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
        
        #!Para salir del sistema
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

        
        #!Para Pagina Usuario
        self.cbx_categoria_usuario.addItem('VENDENDOR')
        self.cbx_categoria_usuario.addItem('AGENTE')
        self.cbx_categoria_usuario.addItem('COMPRADOR')
        
        #*: Agregar funcionalidades para ventana
        self.btn_crear_usuario.clicked.connect(self.ingresar_usuario)
        self.btn_buscar_usuario.clicked.connect(self.buscar_usuario)
        self.btn_eliminar_usuario.clicked.connect(self.eliminar_usuario)
        self.btn_editar_usuario.clicked.connect(self.editar_usuario)
        self.ckb_editar_usuario.clicked.connect(self.activar_campos)
        self.btn_limpiar_usuario.clicked.connect(self.limpiar_campos)

        #!Para Pagina Inmueble
        self.btn_inmueble_ingresar.clicked.connect(self.ingresar_inmueble)
        #TODO: Agregar funcionalidades
        self.llenar_tipoInb()
        self.consultar_ciudades()
        self.llenar_lista_elementos()
        self.llenar_lista_materiales()
        self.cbx_inmueble_ciudad.currentIndexChanged.connect(partial(self.ajustar_cbx_parroquias,self.cbx_inmueble_ciudad,self.cbx_parroquia_inmueble ))
        
        
        #!Para Pagina Transaccion
        #TODO: Agregar funcionalidades
        self.btn_transaccion_crear.clicked.connect(self.crear_transaccion)
        
        
        #!Para Pagina Pendiente
        #TODO: Agregar funcionalidades
        
        #!Para Pagina Historial
        #TODO: Agregar funcionalidades
        
        #!Para Pagina Compra
        #TODO: Agregar funcionalidades
        self.cbx_ciudad_compra.currentIndexChanged.connect(partial(self.ajustar_cbx_parroquias,self.cbx_ciudad_compra,self.cbx_parroquia_compra ))
        #self.cbx_parroquia_compra.currentIndexChanged.connect(self.ajustar_cbx_parroquias)
        
        #!Para Pagina Reportes
        #TODO: Agregar funcionalidades
        
    #! Funcionalidades usuario
    #TODO: Ingresar un usuario 
    def ingresar_usuario(self):
        personaDB = PersonaDB()
        personaDB.conectar.conectar_()
        personaDB.ingresar(self.cbx_categoria_usuario.currentIndex(), 
                           self.txt_cedula_usuario.text(), 
                           self.txt_nombre_usuario.text(), 
                           self.txt_apellido_usuario.text(), 
                           self.txt_telefono_usuarios.text(), 
                           self.txt_correo_usuario.text())()
        
        print("Consulta: ", personaDB.consulta)
        personaDB.enviar_consultar()
        personaDB.cerrar_conexion()

    #TODO: Editar usuario 
    def editar_usuario(self):
        personaDB = PersonaDB()
        personaDB.conectar.conectar_()
        personaDB.editar(self.cbx_categoria_usuario.currentIndex(), 
                           self.txt_cedula_usuario.text(), 
                           self.txt_nombre_usuario.text(), 
                           self.txt_apellido_usuario.text(), 
                           self.txt_telefono_usuarios.text(), 
                           self.txt_correo_usuario.text())()
        print("Consulta: ", personaDB.consulta)
        personaDB.enviar_consultar()
        personaDB.cerrar_conexion()
        self.limpiar_campos()
        
    #TODO: Eliminar usuarios
    def eliminar_usuario(self):
        personaDB = PersonaDB()
        personaDB.conectar.conectar_()
        personaDB.eliminar(self.cbx_categoria_usuario.currentIndex(), self.txt_cedula_usuario.text())()
        print(personaDB.consulta)
        personaDB.enviar_consultar()
        personaDB.cerrar_conexion()
        self.limpiar_campos()

    #TODO: Editar usuarios
    def buscar_usuario(self):
        personaDB = PersonaDB()
        personaDB.conectar.conectar_()
        personaDB.listar(self.cbx_categoria_usuario.currentIndex(), 
                         self.txt_cedula_usuario.text(), 
                         self.txt_nombre_usuario.text())()
        
        print("Consulta: ", personaDB.consulta)
        personaDB.enviar_consultar()
        print(personaDB.conectar.resultado)
        self.llenar_tabla(self.tbl_usuario, personaDB.conectar.resultado)
        
    #TODO: actualiza la tabla de usuarios y deja en blanco los text
    def limpiar_campos(self):
        self.txt_cedula_usuario.clear()
        self.txt_apellido_usuario.clear()
        self.txt_correo_usuario.clear()
        self.txt_telefono_usuarios.clear()
        self.txt_nombre_usuario.clear()
        self.btn_buscar_usuario.click()
        
    #*Para activar o desacticar los campos de usuario
    def activar_campos(self):
        booleano = True
        #print("se ha clicleado,", self.ckb_editar_usuario.isChecked())
        if self.ckb_editar_usuario.isChecked():
            self.txt_cedula_usuario.setEnabled(not booleano)
            self.txt_apellido_usuario.setEnabled(booleano)
            self.txt_correo_usuario.setEnabled(booleano)
            self.txt_telefono_usuarios.setEnabled(booleano)
            self.txt_nombre_usuario.setEnabled(booleano)
            self.cbx_categoria_usuario.setEnabled(not booleano)
            self.btn_editar_usuario.setEnabled(booleano)
        else:
            self.txt_cedula_usuario.setEnabled(booleano)
            self.txt_apellido_usuario.setEnabled(booleano)
            self.txt_correo_usuario.setEnabled(booleano)
            self.txt_telefono_usuarios.setEnabled(booleano)
            self.txt_nombre_usuario.setEnabled(booleano)
            self.cbx_categoria_usuario.setEnabled(booleano)
            self.btn_editar_usuario.setEnabled(booleano)

        
    #!Funcionalidades Inmueble
    #TODO: ingresar inmueble, 
    #clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, fecha_registro, m2_habitables, m2_terreno, ce_vendedor0    
    def ingresar_inmueble(self):
        inmuebleDB = InmuebleDB()
        inmuebleDB.conectar.conectar_()
        print(self.txt_inmueble_ccatastral.text())
        parroquia = f"SELECT id FROM parrroquia WHERE nombre = {self.cbx_parroquia_inmueble.currentText()}"    
        inmuebleDB.ingresar(self.txt_inmueble_ccatastral.text(), 
                            int(self.txt_inmueble_numPisos.text()), 
                            self.txt_inmueble_anioCostru.text(),
                            "FALSE",
                            self.txt_precioMin_compra.text(),
                            self.txt_inmueble_m2Habitables.text(),
                            self.txt_inmueble_m2Terreno.text(),
                            parroquia)()
        print(inmuebleDB.consulta)
        inmuebleDB.enviar_consultar()
        
    def consultar_ciudades(self):
        conectar = Conectar()
        conectar.conectar_()
        
        consulta = ''' 
        SELECT nombre 
        FROM ciudad
        ''' 
        conectar.ingresar_sentencia(consulta)
        
        print(conectar.resultado)
        for c in conectar.resultado:
            self.cbx_inmueble_ciudad.addItem(c[0])
            self.cbx_ciudad_compra.addItem(c[0])
        
            
    def ajustar_cbx_parroquias(self, cbx_c, cbx_p):
        ciudad = cbx_c.currentText()
        print('Ciudad:', ciudad)
        
        conectar = Conectar()
        conectar.conectar_() 
        
        consulta = f''' 
        SELECT p.nombre 
        FROM parroquia AS p
        JOIN ciudad AS c ON p.id_ciudad = c.id
        WHERE c.nombre = '{ciudad}' 
        '''
        conectar.ingresar_sentencia(consulta)
        
        cbx_p.clear()
        for c in conectar.resultado:
            cbx_p.addItem(c[0])
    
    def llenar_vendedores_inmueble(self):
        conexion = Conectar()
        conexion.conectar_()
        
        vendedores_consulta = ''' 
        select cedula, nombre
        from vendedor 
        '''
        
        conexion.ingresar_sentencia(vendedores_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_inmueble_vendedor, r)
    
    
    def llenar_tipoInb(self):
        conexion = Conectar()
        conexion.conectar_()
        
        tipoInm_consulta = ''' 
        select nombre
        from tipo_inmueble 
        '''
        
        conexion.ingresar_sentencia(tipoInm_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_inmueble_tipoInmueble, r)
        
    def llenar_lista_elementos(self):
        conexion = Conectar()
        conexion.conectar_()
        
        tipoInm_consulta = ''' 
        select nombre
        from elemento 
        '''
        
        conexion.ingresar_sentencia(tipoInm_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        
        for item_text in r:
            item = QListWidgetItem(item_text)
            item.setCheckState(Qt.CheckState.Unchecked)  # Hacer el elemento chequeable
            self.list_inmueble_elementos.addItem(item)
        
        
    def llenar_lista_materiales(self):
        conexion = Conectar()
        conexion.conectar_()
        
        tipoInm_consulta = ''' 
        select nombre
        from material 
        '''
        
        conexion.ingresar_sentencia(tipoInm_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        
        for item_text in r:
            item = QListWidgetItem(item_text)
            item.setCheckState(Qt.CheckState.Unchecked)  # Hacer el elemento chequeable
            self.list_inmueble_materiales.addItem(item)
        
   
   #!Funcionalidad Transaccion
   
    def llenar_vendedores_transaccion(self):
        conexion = Conectar()
        conexion.conectar_()
        
        vendedores_consulta = ''' 
        select cedula, nombre
        from vendedor 
        '''
        
        conexion.ingresar_sentencia(vendedores_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_transaccion_vendedor, r)
        
    
    def llenar_inmueble_transaccion(self):
        conexion = Conectar()
        conexion.conectar_()
        
        inmueble_consulta = ''' 
        select clave_castral
        from inmueble
        '''
        conexion.ingresar_sentencia(inmueble_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_transaccion_inmueble, r)
        
    def llenar_agente_transaccion(self):
        conexion = Conectar()
        conexion.conectar_()
        
        agente_consulta = ''' 
        select cedula, nombre
        from agente
        '''
        conexion.ingresar_sentencia(agente_consulta)
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_transaccion_agente, r)
        
    def limpiar_campos():
        ...
    
    
    def crear_transaccion(self):
        #vendedor =  self.cbx_transaccion_vendedor.text()
        agente = self.cbx_transaccion_agente.text()
        inmueblle = self.cbx_transaccion_inmueble.text()
        comision = self.txt_transaccion_comision.text()
        precio_venta = self.txt_transaccion_presioVenta.text()
        comentario = self.txt_transaccion_comentario.text()
        
        conexion = Conectar()
        conexion.conectar_()
        
        agente_consulta = f''' 
        INSERT INTO transaccion (
            precio_deseado_vendedor, 
            precio_venta, 
            fecha_inicio, 
            fecha_final, 
            estado, 
            comision,
            ce_vendedor,
            ce_comprador,
            id_calificacion,
            comentario_comprador,
            id_inmueble,
            comentario_duegno_inmueble
        ) VALUES (
            {float(precio_venta)}, 
            '', 
            CURRENT_DATE, 
            CURRENT_DATE, 
            false, 
            {float(comision)},
            '{agente}',
            '',
            '',
            'Sin comentarios',
            '{inmueblle}',
            '{comentario}'
        );
        '''
        
        conexion.ingresar_sentencia(agente_consulta)
        conexion.resultado
        
        
    #?-----------------------Funcionalidades Extra----------------------------- 
    
    def llenar_combobox(self, cbx, data):
        for d in data:
            cbx.addItem(str(d))
       
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
                self.cbx_inmueble_vendedor.clear()
                self.llenar_vendedores_inmueble()
            case 'btn_historial':
                self.paginas__principales.setCurrentWidget(self.pg_HIstorial)
            case 'btn_compra':
                self.paginas__principales.setCurrentWidget(self.pg_Compra)
            case 'btn_pendientes':
                self.paginas__principales.setCurrentWidget(self.pg_Pendientes)
            case 'btn_transaccion':
                self.paginas__principales.setCurrentWidget(self.pg_Transaccion)
                self.cbx_transaccion_agente.clear()
                self.cbx_transaccion_inmueble.clear()
                self.cbx_transaccion_vendedor.clear()
                self.llenar_vendedores_transaccion()
                self.llenar_agente_transaccion()
                self.llenar_inmueble_transaccion()
    
    
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
            QTableWidgetSelectionRange(row, 0, row, tabla.columnCount() - 1),
            True  # True para seleccionar toda la fila
        )

        # Seleccionar el elemento de la primera columna
        selected_row = tabla.currentRow()
        item_primera_columna = tabla.item(selected_row, 0)
        ID = item_primera_columna.text()
        self.primera_colum = selected_row
        self.llenar_campos_pagina(tabla)
        
        
    def llenar_campos_pagina(self, tabla):
        match tabla:
            case self.tbl_usuario:
                #TODO: Llenar campos de pagina usuarios para editar
                print(self.primera_colum)
                self.txt_cedula_usuario.setText(self.tbl_usuario.item(self.primera_colum, 0).text())
                self.txt_nombre_usuario.setText(self.tbl_usuario.item(self.primera_colum, 1).text())
                self.txt_apellido_usuario.setText(self.tbl_usuario.item(self.primera_colum, 2).text())
                self.txt_telefono_usuarios.setText(self.tbl_usuario.item(self.primera_colum, 3).text())
                self.txt_correo_usuario.setText(self.tbl_usuario.item(self.primera_colum, 4).text())


            case self.tbl_inmueble:
                #TODO: Llenar campos de pagina inmueble para editar y eliminar
                print(self.primera_colum)
                self.txt_inmueble_ccatastral.setText(self.tbl_inmueble.item(self.primera_colum, 0).text())
                self.txt_inmueble_numPisos.setText(self.tbl_inmueble.item(self.primera_colum, 1).text())
                self.txt_inmueble_precio.setText(self.tbl_inmueble.item(self.primera_colum, 2).text())
                self.txt_inmueble_m2Habitables.setText(self.tbl_inmueble.item(self.primera_colum, 3).text())
                self.txt_inmueble_m2Terreno.setText(self.tbl_inmueble.item(self.primera_colum, 4).text())
                self.txt_inmueble_ciudad.setCurrentText(self.tbl_inmueble.item(self.primera_colum, 5).text())
                self.parroquia.setCurrentText(self.tbl_inmueble.item(self.primera_colum, 6).text())
                #self.txt_inmueble_m2Terreno.setText(self.tbl_inmueble.item(self.primera_colum, 4).text())
                ...
            case self.tbl_pendientes:
                print(self.primera_colum)

                ...
            case self.tbl_historial:
                ...
            case self.tbl_desempenio:
                ...
            case self.tbl_ventas:
                ...
            case self.tbl_porcentaje:
                ...
                
        
        
        
        
        



