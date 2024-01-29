from model.Compra import CompraDB
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
        #self.fr_botones_menu.setFixedWidth(0)
        
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
        self.btn_inmueble_buscar.clicked.connect(self.buscar_inmueble)
        #TODO: Agregar funcionalidades
        self.llenar_tipoInb()
        self.consultar_ciudades()
        self.llenar_lista_elementos()
        self.llenar_lista_materiales()
        self.cbx_inmueble_ciudad.currentIndexChanged.connect(partial(self.ajustar_cbx_parroquias,self.cbx_inmueble_ciudad,self.cbx_parroquia_inmueble ))
        self.tbl_inmueble.setColumnCount(4)
        self.tbl_inmueble.setHorizontalHeaderLabels(["Codigo catastral","Ciudad","Parroquia","Precio"])
        
        #!Para Pagina Transaccion
        #TODO: Agregar funcionalidades
        self.btn_transaccion_crear.clicked.connect(self.crear_transaccion)
        self.btn_transaccion_limpiar.clicked.connect(self.limpiar_capos_transaccion)
        
        
        #!Para Pagina Pendiente
        #TODO: Agregar funcionalidades
        self.tbl_pendientes.setColumnCount(4)
        self.tbl_pendientes.setHorizontalHeaderLabels(['ID', "Clave Catastral", "FECHA INICiO", 'ESTADO'])
        self.btn_filtrar_pendientes.clicked.connect(self.filtrar_campos_pendientes)
        
        #!Para Pagina Historial
        #TODO: Agregar funcionalidades
        self.tbl_historial.setColumnCount(4)
        self.tbl_historial.setHorizontalHeaderLabels(['ID', "Clave Catastral", "FECHA INICiO", 'ESTADO'])
        self.btn_filtrar_pendientes.clicked.connect(self.filtrar_campos_historial)
        
        #!Para Pagina Compra
        #TODO: Agregar funcionalidades
        self.cbx_ciudad_compra.currentIndexChanged.connect(partial(self.ajustar_cbx_parroquias,self.cbx_ciudad_compra,self.cbx_parroquia_compra ))
        self.btn_filtrar_compra.clicked.connect(self.cambiar_parametros_filtro_compra)
        self.pushButton_17.hide()
        self.pushButton_16.hide()
        self.cbx_calificacion_compra.addItems(['Excelente','Muy Bueno','Bueno','Regular','Deficiente'])
        self.cbx_estado_compra.addItems(['TRUE','FALSE'])
        self.btn_finalizarTran_compra.clicked.connect(self.finalizar_transaccion)
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

        conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM parroquia WHERE nombre = '{self.cbx_parroquia_inmueble.currentText()}'" )
        parroquia = self.convertir_a_string(conectar.resultado)
        
        conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM tipo_inmueble WHERE nombre = '{self.cbx_inmueble_tipoInmueble.currentText()}'")
        tipo_inmueble = self.convertir_a_string(conectar.resultado)
        print(conectar.resultado)
        
        try:
            print(self.txt_inmueble_ccatastral.text(), 
                                int(self.txt_inmueble_numPisos.text()), 
                                self.txt_inmueble_anioCostru.text(),
                                'FALSE',
                                self.txt_inmueble_precio.text(),
                                self.txt_inmueble_m2Habitables.text(),
                                self.txt_inmueble_m2Terreno.text(),
                                parroquia,
                                self.cbx_inmueble_vendedor.currentText(),
                                tipo_inmueble)
        
        
            inmuebleDB.ingresar(self.txt_inmueble_ccatastral.text(), 
                            int(self.txt_inmueble_numPisos.text()), 
                            self.txt_inmueble_anioCostru.text(),
                            'FALSE',
                            self.txt_inmueble_precio.text(),
                            self.txt_inmueble_m2Habitables.text(),
                            self.txt_inmueble_m2Terreno.text(),
                            parroquia,
                            self.cbx_inmueble_vendedor.currentText(),
                            tipo_inmueble) 
        
        except Exception as e:
            print(e)
        
        
        print(inmuebleDB.consulta)
        inmuebleDB.enviar_consultar()
    
    def buscar_inmueble(self):
        inmuebleDB = InmuebleDB()
        inmuebleDB.conectar.conectar_()

        #*Obtener el id de la parroquia
        conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM parroquia WHERE nombre = '{self.cbx_parroquia_inmueble.currentText()}'" )
        parroquia = self.convertir_a_string(conectar.resultado)
        
        #*Obtener el id del tipo de inmueble
        conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM tipo_inmueble WHERE nombre = '{self.cbx_inmueble_tipoInmueble.currentText()}'")
        tipo_inmueble = self.convertir_a_string(conectar.resultado)

        #*Obtener el id de la ciudad
        conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM ciudad WHERE nombre = '{self.cbx_inmueble_tipoInmueble.currentText()}'")
        ciudad = self.convertir_a_string(conectar.resultado)

        #*Obtener lista de elementos
        """conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM elemento")
        elementos = self.convertir_a_string(conectar.resultado)"""

        #*Obtener lista de materiales
        """conectar = Conectar()
        conectar.conectar_()
        conectar.ingresar_sentencia(f"SELECT id FROM ciudad WHERE nombre = '{self.cbx_inmueble_tipoInmueble.currentText()}'")
        materiales = self.convertir_a_string(conectar.resultado)"""


        inmuebleDB.listar(self.txt_inmueble_ccatastral.text(),
                          self.txt_inmueble_precio.text(), 
                          self.txt_inmueble_precio.text(), 
                          self.cbx_inmueble_ciudad.currentText(),
                          self.cbx_parroquia_inmueble.currentText(),
                          self.txt_inmueble_numPisos.text(),
                          self.txt_inmueble_anioCostru.text(),
                          "",# array con elementos
                          "")# array con materiales
        
        print("Mi consulta:", inmuebleDB.consulta)
        inmuebleDB.enviar_consultar()
        #inmuebleDB.listar(self.txt_pre)
        #nombres_columnas = ["Columna 1", "Columna 2", "Columna 3"]
        #tabla.setHorizontalHeaderLabels(nombres_columnas)
        #
        for fila in inmuebleDB.conectar.resultado:
            print(fila)

        self.llenar_tabla(self.tbl_inmueble, inmuebleDB.conectar.resultado)

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
        r = map(lambda x: x[0], conexion.resultado)
        self.llenar_combobox(self.cbx_tipoInm_compra, r)
        
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
        r = map(lambda x: x[0], conexion.resultado)
        for item_text in r:
            item = QListWidgetItem(item_text)
            item.setCheckState(Qt.CheckState.Unchecked)  # Hacer el elemento chequeable
            self.list_elemento_compra.addItem(item)
        
        
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
        
        r = map(lambda x: x[0], conexion.resultado)
        for item_text in r:
            item = QListWidgetItem(item_text)
            item.setCheckState(Qt.CheckState.Unchecked)  # Hacer el elemento chequeable
            self.list_material_compra.addItem(item)
        
   
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
        
    def limpiar_capos_transaccion(self):
        self.txt_transaccion_comision.clear()
        self.txt_transaccion_comentario.clear()
        self.txt_transaccion_presioVenta.clear()
        self.cbx_transaccion_vendedor.setCurrentIndex(0)
        self.cbx_transaccion_agente.setCurrentIndex(0)
        self.cbx_transaccion_inmueble.setCurrentIndex(0)
    
    
    def crear_transaccion(self):
        #vendedor =  self.cbx_transaccion_vendedor.text()
        agente = self.cbx_transaccion_agente.currentText()
        inmueblle = self.cbx_transaccion_inmueble.currentText()
        comision = self.txt_transaccion_comision.text()
        precio_venta = self.txt_transaccion_presioVenta.text()
        comentario = self.txt_transaccion_comentario.text()
        try:
            conexion = Conectar()
            conexion.conectar_()
            
            agente_consulta = f''' 
            INSERT INTO transaccion (
                precio_deseado_vendedor, 
                fecha_inicio, 
                estado, 
                comision, 
                ce_agente, 
                id_inmueble,
                comentario_duegno_inmueble 
            ) VALUES (
                {float(precio_venta)}, 
                CURRENT_DATE, 
                false, 
                {float(comision)},
                '{agente}',
                '{inmueblle}',
                '{comentario}'
            );
            '''
            
            conexion.ingresar_sentencia(agente_consulta)
            conexion.resultado
        except Exception as e: print(e)
            
    #!Funcionalidades de Pendientes

    def llenar_tabla_pendientes(self):
        
        consulta_pendietes = ''' 
        Select id, id_inmueble, fecha_inicio, estado
        From transaccion 
        Where estado = 'FALSE'
        '''
        conexion = Conectar()
        conexion.conectar_()
        
        conexion.ingresar_sentencia(consulta_pendietes)
        r = conexion.resultado
        self.llenar_tabla(self.tbl_pendientes, r)
        
    def filtrar_campos_pendientes(self):
        
        agregar = ''
        ccatatral = self.txt_ccatastral_pendientes.text()
        if(len(ccatatral)!=0):
            agregar = f"AND id_inmueble = '{ccatatral}'"
        
        fecha_seleccionada = self.cld_fecha_pendientes.selectedDate().toString("yyyy-MM-dd")
        print('Fecha Seleccionada: ', fecha_seleccionada)
        
        conexion = Conectar()
        conexion.conectar_()
        
        consulta_pendietes = f''' 
        SELECT id, id_inmueble, fecha_inicio, estado
        FROM transaccion 
        WHERE estado = 'FALSE' AND fecha_inicio <= '{fecha_seleccionada}'
        ''' + agregar
        conexion.ingresar_sentencia(consulta_pendietes)
        
        print('Coincidencias: ', conexion.resultado)
        self.llenar_tabla(self.tbl_pendientes, conexion.resultado)
    
    #!Funcionalidades de Historial 
    
    def llenar_tabla_historial(self):
    
        consulta_historial = ''' 
        SELECT id, id_inmueble, fecha_inicio, estado
        FROM transaccion 
        WHERE estado = 'TRUE'
        '''
        conexion = Conectar()
        conexion.conectar_()
        
        conexion.ingresar_sentencia(consulta_historial)
        r = conexion.resultado
        self.llenar_tabla(self.tbl_historial, r)
    
    def filtrar_campos_historial(self):
        
        agregar = ''
        ccatatral = self.txt_ccatastral_pendientes.text()
        if(len(ccatatral)!=0):
            agregar = f" AND id_inmueble = '{ccatatral}'"
        
        fecha_seleccionada = self.cld_fecha_pendientes.selectedDate().toString("yyyy-MM-dd")
        print(fecha_seleccionada)
        
        conexion = Conectar()
        conexion.conectar_()
        
        consulta_historial = f''' 
        SELECT id, id_inmueble, fecha_inicio, estado
        FROM transaccion 
        WHERE estado = 'TRUE' AND fecha_inicio >= '{fecha_seleccionada}'
        '''+agregar
        conexion.ingresar_sentencia(consulta_historial)
        
        print(conexion.resultado)
        
    #!======================Funcionalidades de Compra=========================
    c = CompraDB()
     
    def llenar_combo_ccatastral(self, num_pisos='', tiempo_construccion='', metros_terreno='', ciudad='', parroquia='', precio_min='',precio_max='', tipo_imb=''):
        conexion = Conectar()
        conexion.conectar_()
        
        comprador_consulta = self.c.filtro_compra(num_pisos,tiempo_construccion,metros_terreno,ciudad,parroquia,precio_min,precio_max,tipo_imb)
        
        conexion.ingresar_sentencia(comprador_consulta)
        try:
            r = map(lambda x: x[0], conexion.resultado)
            self.llenar_combobox(self.cbx_inmueble_compra, r)
        except Exception as e: print(e)
    
    def llenar_combo_compradores(self):
        conexion = Conectar()
        conexion.conectar_()
        
        consulta_pendietes = f''' 
        SELECT cedula
        FROM comprador
        '''
        
        r = conexion.ingresar_sentencia(consulta_pendietes)
        try:
            r = map(lambda x: x[0], conexion.resultado)
            self.llenar_combobox(self.cbx_comprador_compra, r)   
        except Exception as e: print(e)
        
    def cambiar_parametros_filtro_compra(self):
        num_pisos = self.txt_numPisos_compra.text()
        tiempo_const = self.txt_anioC_compra.text()
        precio_max = self.txt_precioMax_compra.text()
        precio_min = self.txt_precioMin_compra.text()
        metros_terreno = self.txt_metroTerre_compra.text()
        ciudad = self.cbx_ciudad_compra.currentText()
        parroquia = self.cbx_parroquia_compra.currentText()
        tipo_inm = self.cbx_tipoInm_compra.currentText()
        
        self.llenar_combo_ccatastral(num_pisos,tiempo_const,metros_terreno,ciudad,parroquia,precio_min,precio_max,tipo_inm)
        elementos_chequeados = []
        for i in range(self.list_elemento_compra.count()):
            item = self.list_elemento_compra.item(i)
            if item.checkState():
                elementos_chequeados.append(item.text())
        elementos_chequeados
        print(elementos_chequeados)
        
        print(num_pisos, tiempo_const,precio_max, precio_min, metros_terreno, ciudad, parroquia,tipo_inm)
        
    def finalizar_transaccion(self):
        conexion = Conectar()
        conexion.conectar_()
    
        consulta = f'''
        UPDATE transaccion
        SET 
            ce_comprador = '{self.cbx_comprador_compra.currentText()}',
            precio_venta  = {self.txt_precioVenta_compra.text()},
            estado = {self.cbx_estado_compra.currentText()},
            comentario_comprador = '{self.txt_comentario_compra.text()}',
            id_calificacion = {self.cbx_calificacion_compra.currentIndex()+1},
            fecha_final = CURRENT_DATE
        WHERE id_inmueble = '{self.cbx_inmueble_compra.currentText()}'
        '''
        print('Id calificacion:',self.cbx_calificacion_compra.currentIndex()+1)
        try:
            r = conexion.ingresar_sentencia(consulta)
            print(r)
        except Exception as e: print(e)
    
    #!======================Funcionalidades de Reportes=========================
    #todo: para el primer reporte
    
    #todo: para el segundo reporte
    
    #todo: para el tercer reporte
    
    
    
    
    #?-------------Funcionalidades Extra----------------------------- 
    def convertir_a_string(self, lista_tuplas): # transforma tuplas a string, formato para sentencias SQL
        tuplas_convertidas = []
        for tupla in lista_tuplas:
            if len(tupla) == 1:
                # Si la tupla tiene solo un elemento, extraemos y limpiamos el elemento
                elemento_convertido = str(tupla[0]).strip("('')")
                tupla_convertida = elemento_convertido
            else:
                # Si la tupla tiene más de un elemento, creamos una tupla de elementos
                elementos_convertidos = []
                for elemento in tupla:
                    # Convertir cada elemento de la tupla a un string y quitar las comillas adicionales
                    elemento_convertido = str(elemento).strip("('')")
                    elementos_convertidos.append(elemento_convertido)
                # Crear una cadena con los elementos de la tupla entre paréntesis y separados por comas
                tupla_convertida = '(' + ', '.join(elementos_convertidos) + ')'
            tuplas_convertidas.append(tupla_convertida)
        # Unir todas las tuplas convertidas en una cadena
        cadena_resultante = ', '.join(tuplas_convertidas)
        return cadena_resultante    
    
    def llenar_combobox(self, cbx, data):
        cbx.clear()
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
                self.llenar_tabla_historial()
            case 'btn_compra':
                self.paginas__principales.setCurrentWidget(self.pg_Compra)
                self.llenar_combo_compradores()
                self.llenar_combo_ccatastral()
            case 'btn_pendientes':
                self.paginas__principales.setCurrentWidget(self.pg_Pendientes)
                self.llenar_tabla_pendientes()
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
                
        
        
        
        
        



