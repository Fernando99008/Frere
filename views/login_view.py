from PySide6.QtWidgets import ( QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QEvent
from services.auth_service import iniciar_sesion


# =========================================================
# CLASE PARA MOSTRAR IMAGEN RESPONSIVA
# =========================================================

class ImageLabel(QLabel):

    def __init__(self, image_path):
        super().__init__()

        self.pixmap_original = QPixmap(image_path)

        self.setAlignment(
            Qt.AlignCenter
        )

    def resizeEvent(self, event):

        if not self.pixmap_original.isNull():

            pixmap = self.pixmap_original.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(
                pixmap
            )

        super().resizeEvent(event)


# =========================================================
# LOGIN
# =========================================================

class LoginView(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Frère - Iniciar sesión"
        )

        self.setWindowIcon(
            QIcon( "assets/icon/frere.ico" )
        )

        # =================================================
        # PANTALLA COMPLETA
        # =================================================

        self.showMaximized()

        # =================================================
        # LAYOUT PRINCIPAL
        # =================================================

        layout_principal = QHBoxLayout()

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(
            0
        )

        # =================================================
        # PANEL IZQUIERDO
        # =================================================

        panel_izquierdo = QFrame()

        panel_izquierdo.setObjectName(
            "panelIzquierdo"
        )

        layout_izquierdo = QVBoxLayout()

        layout_izquierdo.setContentsMargins(
            0,
            0,
            0,
            0
        )

        # Imagen

        imagen = ImageLabel(
            "assets/frere.png"
        )

        layout_izquierdo.addWidget(
            imagen
        )

        panel_izquierdo.setLayout(
            layout_izquierdo
        )

        # =================================================
        # PANEL DERECHO
        # =================================================

        panel_derecho = QFrame()

        panel_derecho.setObjectName(
            "panelDerecho"
        )

        layout_derecho = QVBoxLayout()

        layout_derecho.setAlignment(
            Qt.AlignCenter
        )

        # =================================================
        # FORMULARIO
        # =================================================

        formulario = QFrame()

        formulario.setFixedWidth(
            450
        )

        layout_formulario = QVBoxLayout(
            formulario
        )

        layout_formulario.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_formulario.setSpacing(
            10
        )

        # =================================================
        # TÍTULO
        # =================================================

        titulo = QLabel(
            "Iniciar sesión"
        )

        titulo.setObjectName(
            "titulo"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        # =================================================
        # SUBTÍTULO
        # =================================================

        subtitulo = QLabel(
            "Ingresá tus datos para entrar a frère"
        )

        subtitulo.setObjectName(
            "subtitulo"
        )

        subtitulo.setAlignment(
            Qt.AlignCenter
        )

        # =================================================
        # USUARIO
        # =================================================

        self.input_usuario = QLineEdit()

        self.input_usuario.setPlaceholderText(
            "Nombre de usuario o email"
        )

        self.input_usuario.setFixedHeight(
            54
        )

        self.input_usuario.setFocusPolicy(
            Qt.StrongFocus
        )

        # Mensaje usuario

        self.mensaje_usuario = QLabel()

        self.mensaje_usuario.setObjectName(
            "mensajeUsuario"
        )

        self.mensaje_usuario.setText(
            ""
        )

        self.mensaje_usuario.setVisible(
            False
        )

        # Enter

        self.input_usuario.returnPressed.connect(
            self.enter_usuario
        )

        # Detectar escritura

        self.input_usuario.textChanged.connect(
            self.validar_usuario
        )

        # =================================================
        # CONTENEDOR PASSWORD
        # =================================================

        contenedor_password = QFrame()

        contenedor_password.setObjectName(
            "contenedorPassword"
        )

        contenedor_password.setFixedHeight(
            54
        )

        layout_password = QHBoxLayout(
            contenedor_password
        )

        layout_password.setContentsMargins(
            0,
            0,
            5,
            0
        )

        layout_password.setSpacing(
            0
        )

        # =================================================
        # PASSWORD
        # =================================================

        self.input_password = QLineEdit()

        self.input_password.setPlaceholderText(
            "Contraseña"
        )

        self.input_password.setEchoMode(
            QLineEdit.Password
        )

        self.input_password.setFixedHeight(
            54
        )

        self.input_password.setFocusPolicy(
            Qt.StrongFocus
        )

        # Enter

        self.input_password.returnPressed.connect(
            self.enter_password
        )

        # Detectar escritura

        self.input_password.textChanged.connect(
            self.validar_password
        )

        # =================================================
        # BOTÓN MOSTRAR CONTRASEÑA
        # =================================================

        self.password_visible = False

        self.boton_password = QPushButton()

        self.boton_password.setObjectName(
            "botonPassword"
        )

        self.boton_password.setIcon(
            QIcon(
                "assets/icon/ver_mas.svg"
            )
        )

        self.boton_password.setFixedSize(
            48,
            48
        )

        self.boton_password.setCursor(
            Qt.PointingHandCursor
        )

        self.boton_password.setToolTip(
            "Mostrar contraseña"
        )

        self.boton_password.setFocusPolicy(
            Qt.StrongFocus
        )

        self.boton_password.clicked.connect(
            self.toggle_password
        )

        # =================================================
        # AGREGAR PASSWORD + BOTÓN
        # =================================================

        layout_password.addWidget(
            self.input_password
        )

        layout_password.addWidget(
            self.boton_password
        )

        # =================================================
        # BOTÓN LOGIN
        # =================================================

        self.boton_login = QPushButton(
            "Iniciar sesión"
        )

        self.boton_login.setObjectName(
            "botonLogin"
        )

        self.boton_login.setCursor(
            Qt.PointingHandCursor
        )

        self.boton_login.setFixedHeight(
            54
        )

        self.boton_login.setFocusPolicy(
            Qt.StrongFocus
        )

        self.boton_login.clicked.connect(
            self.login
        )

        # =================================================
        # AGREGAR ELEMENTOS
        # =================================================

        layout_formulario.addWidget(
            titulo
        )

        layout_formulario.addWidget(
            subtitulo
        )

        layout_formulario.addSpacing(
            20
        )

        layout_formulario.addWidget(
            self.input_usuario
        )

        layout_formulario.addWidget(
            self.mensaje_usuario
        )

        layout_formulario.addWidget(
            contenedor_password
        )

        # =================================================
        # MENSAJE PASSWORD
        # =================================================

        self.mensaje_password = QLabel()

        self.mensaje_password.setObjectName(
            "mensajePassword"
        )

        self.mensaje_password.setText(
            ""
        )

        self.mensaje_password.setVisible(
            False
        )

        layout_formulario.addWidget(
            self.mensaje_password
        )

        layout_formulario.addSpacing(
            10
        )

        layout_formulario.addWidget(
            self.boton_login
        )

        # =================================================
        # FORMULARIO CENTRADO
        # =================================================

        layout_derecho.addWidget(
            formulario,
            alignment=Qt.AlignCenter
        )

        panel_derecho.setLayout(
            layout_derecho
        )

        # =================================================
        # PANELES
        # =================================================

        layout_principal.addWidget(
            panel_izquierdo,
            1
        )

        layout_principal.addWidget(
            panel_derecho,
            1
        )

        self.setLayout(
            layout_principal
        )

        # =================================================
        # ORDEN DE NAVEGACIÓN
        # =================================================

        self.elementos_navegacion = [
            self.input_usuario,
            self.input_password,
            self.boton_password,
            self.boton_login
        ]

        # =================================================
        # EVENT FILTER
        # =================================================

        for elemento in self.elementos_navegacion:

            elemento.installEventFilter(
                self
            )

        # =================================================
        # ESTILOS
        # =================================================

        self.setStyleSheet("""

            /* =================================================
               GENERAL
               ================================================= */

            QWidget {
                font-family: Arial;
            }


            /* =================================================
               PANEL IZQUIERDO
               ================================================= */

            #panelIzquierdo {
                background-color: #111827;
            }


            /* =================================================
               PANEL DERECHO
               ================================================= */

            #panelDerecho {
                background-color: #ffffff;
            }


            /* =================================================
               TÍTULO
               ================================================= */

            #titulo {
                font-size: 40px;
                font-weight: bold;
                color: #111827;
            }


            /* =================================================
               SUBTÍTULO
               ================================================= */

            #subtitulo {
                font-size: 18px;
                color: #6b7280;
            }


            /* =================================================
               INPUTS
               ================================================= */

            QLineEdit {

                height: 54px;

                border: 2px solid #d1d5db;

                border-radius: 8px;

                padding-left: 18px;

                padding-right: 10px;

                font-size: 18px;

                background-color: #ffffff;

                color: #111827;
            }


            /* =================================================
               INPUT - HOVER
               ================================================= */

            QLineEdit:hover {

                border: 2px solid #9ca3af;
            }


            /* =================================================
               INPUT - FOCUS
               ================================================= */

            QLineEdit:focus {

                border: 2px solid #2563eb;

                background-color: #ffffff;
            }


            /* =================================================
               INPUT CON ERROR
               ================================================= */

            QLineEdit[error="true"] {

                border: 2px solid #ef4444;

                background-color: #fff5f5;
            }


            /* =================================================
               CONTENEDOR PASSWORD
               ================================================= */

            #contenedorPassword {

                border: 2px solid #d1d5db;

                border-radius: 8px;

                background-color: #ffffff;
            }


            /* =================================================
               PASSWORD
               ================================================= */

            #contenedorPassword QLineEdit {

                border: none;

                border-radius: 0;

                padding-left: 18px;

                padding-right: 5px;

                background-color: transparent;
            }


            #contenedorPassword QLineEdit:focus {

                border: none;

                background-color: transparent;
            }


            /* =================================================
               BOTÓN PASSWORD
               ================================================= */

            #botonPassword {

                border: none;

                background-color: transparent;

                padding: 4px;
            }


            /* =================================================
               BOTÓN PASSWORD - HOVER
               ================================================= */

            #botonPassword:hover {

                background-color: #f3f4f6;

                border-radius: 6px;
            }


            /* =================================================
               BOTÓN PASSWORD - FOCUS TECLADO
               ================================================= */

            #botonPassword:focus {

                background-color: #e5e7eb;

                border: 2px solid #2563eb;

                border-radius: 6px;
            }


            /* =================================================
               BOTÓN PASSWORD - PRESSED
               ================================================= */

            #botonPassword:pressed {

                background-color: #e5e7eb;

                border-radius: 6px;
            }


            /* =================================================
               MENSAJES
               ================================================= */

            #mensajeUsuario,
            #mensajePassword {

                font-size: 14px;

                color: #ef4444;

                padding-left: 5px;
            }


            /* =================================================
               BOTÓN LOGIN
               ================================================= */

            #botonLogin {

                height: 54px;

                border-radius: 8px;

                background-color: #2563eb;

                color: white;

                font-size: 18px;

                font-weight: bold;
            }


            /* =================================================
               BOTÓN LOGIN - HOVER
               ================================================= */

            QPushButton:hover {

                background-color: #1d4ed8;
            }


            /* =================================================
               BOTÓN LOGIN - FOCUS TECLADO
               ================================================= */

            QPushButton:focus {

                border: 3px solid #111827;

                background-color: #1d4ed8;
            }


            /* =================================================
               BOTÓN LOGIN - PRESSED
               ================================================= */

            QPushButton:pressed {

                background-color: #1e40af;
            }

        """)


    # =========================================================
    # EVENT FILTER
    # =========================================================

    def eventFilter(self, objeto, evento):

        if evento.type() == QEvent.KeyPress:

            tecla = evento.key()

            # =================================================
            # ENTER
            # =================================================

            if tecla == Qt.Key_Return or tecla == Qt.Key_Enter:

                if objeto == self.input_usuario:

                    self.enter_usuario()

                    return True

                elif objeto == self.input_password:

                    self.enter_password()

                    return True

                elif objeto == self.boton_password:

                    self.toggle_password()

                    return True

                elif objeto == self.boton_login:

                    self.login()

                    return True

            # =================================================
            # FLECHA ARRIBA / ABAJO
            # =================================================

            if tecla in (
                Qt.Key_Up,
                Qt.Key_Down
            ):

                self.mover_vertical(
                    objeto,
                    tecla
                )

                return True

            # =================================================
            # FLECHA IZQUIERDA / DERECHA
            # =================================================
            #
            # En los campos de texto dejamos que Qt maneje
            # las flechas para mover el cursor.
            #
            # =================================================

            if tecla in (
                Qt.Key_Left,
                Qt.Key_Right
            ):

                if isinstance(
                    objeto,
                    QLineEdit
                ):

                    return super().eventFilter(
                        objeto,
                        evento
                    )

                self.mover_horizontal(
                    objeto,
                    tecla
                )

                return True

        return super().eventFilter(
            objeto,
            evento
        )


    # =========================================================
    # MOVER VERTICALMENTE
    # =========================================================

    def mover_vertical(self, objeto, tecla):

        if objeto not in self.elementos_navegacion:
            return

        posicion = self.elementos_navegacion.index(
            objeto
        )

        # -----------------------------------------------------
        # ABAJO
        # -----------------------------------------------------

        if tecla == Qt.Key_Down:

            siguiente = posicion + 1

            if siguiente >= len(
                self.elementos_navegacion
            ):

                siguiente = 0

        # -----------------------------------------------------
        # ARRIBA
        # -----------------------------------------------------

        else:

            siguiente = posicion - 1

            if siguiente < 0:

                siguiente = len(
                    self.elementos_navegacion
                ) - 1

        self.elementos_navegacion[
            siguiente
        ].setFocus()


    # =========================================================
    # MOVER HORIZONTALMENTE
    # =========================================================

    def mover_horizontal(self, objeto, tecla):

        if objeto not in self.elementos_navegacion:
            return

        posicion = self.elementos_navegacion.index(
            objeto
        )

        if tecla == Qt.Key_Right:

            siguiente = posicion + 1

            if siguiente >= len(
                self.elementos_navegacion
            ):

                siguiente = 0

        else:

            siguiente = posicion - 1

            if siguiente < 0:

                siguiente = len(
                    self.elementos_navegacion
                ) - 1

        self.elementos_navegacion[
            siguiente
        ].setFocus()


    # =========================================================
    # ENTER EN USUARIO
    # =========================================================

    def enter_usuario(self):

        username = self.input_usuario.text().strip()

        if not username:

            self.mostrar_error_usuario()

            return

        self.quitar_error_usuario()

        self.input_password.setFocus()


    # =========================================================
    # ENTER EN PASSWORD
    # =========================================================

    def enter_password(self):

        password = self.input_password.text()

        if not password:

            self.mostrar_error_password()

            return

        self.quitar_error_password()

        self.login()


    # =========================================================
    # VALIDAR USUARIO
    # =========================================================

    def validar_usuario(self):

        if self.input_usuario.text().strip():

            self.quitar_error_usuario()


    # =========================================================
    # VALIDAR PASSWORD
    # =========================================================

    def validar_password(self):

        if self.input_password.text():

            self.quitar_error_password()


    # =========================================================
    # MOSTRAR ERROR USUARIO
    # =========================================================

    def mostrar_error_usuario(self):

        self.input_usuario.setProperty(
            "error",
            "true"
        )

        self.input_usuario.style().unpolish(
            self.input_usuario
        )

        self.input_usuario.style().polish(
            self.input_usuario
        )

        self.mensaje_usuario.setText(
            "⚠ Completá el usuario para continuar."
        )

        self.mensaje_usuario.setVisible(
            True
        )

        self.input_usuario.setFocus()


    # =========================================================
    # QUITAR ERROR USUARIO
    # =========================================================

    def quitar_error_usuario(self):

        self.input_usuario.setProperty(
            "error",
            "false"
        )

        self.input_usuario.style().unpolish(
            self.input_usuario
        )

        self.input_usuario.style().polish(
            self.input_usuario
        )

        self.mensaje_usuario.setText(
            ""
        )

        self.mensaje_usuario.setVisible(
            False
        )


    # =========================================================
    # MOSTRAR ERROR PASSWORD
    # =========================================================

    def mostrar_error_password(self):

        self.input_password.setProperty(
            "error",
            "true"
        )

        self.input_password.style().unpolish(
            self.input_password
        )

        self.input_password.style().polish(
            self.input_password
        )

        self.mensaje_password.setText(
            "⚠ Completá la contraseña para continuar."
        )

        self.mensaje_password.setVisible(
            True
        )

        self.input_password.setFocus()


    # =========================================================
    # QUITAR ERROR PASSWORD
    # =========================================================

    def quitar_error_password(self):

        self.input_password.setProperty(
            "error",
            "false"
        )

        self.input_password.style().unpolish(
            self.input_password
        )

        self.input_password.style().polish(
            self.input_password
        )

        self.mensaje_password.setText(
            ""
        )

        self.mensaje_password.setVisible(
            False
        )


    # =========================================================
    # MOSTRAR / OCULTAR PASSWORD
    # =========================================================

    def toggle_password(self):

        if self.password_visible:

            self.input_password.setEchoMode(
                QLineEdit.Password
            )

            self.boton_password.setIcon(
                QIcon(
                    "assets/icon/ver_mas.svg"
                )
            )

            self.boton_password.setToolTip(
                "Mostrar contraseña"
            )

            self.password_visible = False

        else:

            self.input_password.setEchoMode(
                QLineEdit.Normal
            )

            self.boton_password.setIcon(
                QIcon(
                    "assets/icon/ver_menos.svg"
                )
            )

            self.boton_password.setToolTip(
                "Ocultar contraseña"
            )

            self.password_visible = True


    # =========================================================
    # LOGIN
    # =========================================================

    def login(self):

        username = self.input_usuario.text().strip()

        password = self.input_password.text()

        # =================================================
        # VALIDAR USUARIO
        # =================================================

        if not username:

            self.mostrar_error_usuario()

            return

        # =================================================
        # VALIDAR PASSWORD
        # =================================================

        if not password:

            self.mostrar_error_password()

            return

        # =================================================
        # QUITAR ERRORES
        # =================================================

        self.quitar_error_usuario()

        self.quitar_error_password()

        # =================================================
        # AUTENTICAR
        # =================================================

        usuario = iniciar_sesion(
            username,
            password
        )

        # =================================================
        # LOGIN CORRECTO
        # =================================================

        if usuario:

            QMessageBox.information(
                self,
                "Frère",
                f"Bienvenido {usuario.nombre}"
            )

            print(
                "Usuario:",
                usuario.username
            )

            print(
                "Rol ID:",
                usuario.rol_id
            )

        # =================================================
        # LOGIN INCORRECTO
        # =================================================

        else:

            QMessageBox.warning(
                self,
                "Frère",
                "Usuario o contraseña incorrectos."
            )

            self.input_password.setFocus()

            self.input_password.selectAll()