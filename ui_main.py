from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar, QLabel
from PySide6.QtCore import Qt

class Ui_Carrera:
    def setupUi(self, Form):
        Form.setObjectName("Carrera")
        Form.resize(600, 450)
        Form.setWindowTitle("Fórmula 1 PySide6 🏎️")
        
        self.layout_principal = QVBoxLayout(Form)
        self.barras = []
        self.labels_coches = []
        self.emojis = ["🏎️", "🚗", "🚓", "🚜", "🚀"] # Diferentes vehículos
        
        for i in range(5):
            contenedor_coche = QVBoxLayout()
            
            # Label para el emoji del coche que se moverá
            lbl_emoji = QLabel(self.emojis[i])
            lbl_emoji.setStyleSheet("font-size: 25px;")
            
            # Barra de progreso
            progreso = QProgressBar()
            progreso.setRange(0, 100)
            progreso.setTextVisible(False) # Quitamos el porcentaje para que se vea más limpio
            progreso.setFixedHeight(15)
            
            contenedor_coche.addWidget(lbl_emoji)
            contenedor_coche.addWidget(progreso)
            self.layout_principal.addLayout(contenedor_coche)
            
            self.barras.append(progreso)
            self.labels_coches.append(lbl_emoji)
        
        self.btn_inicio = QPushButton("🏁 ¡LARGADA! 🏁")
        self.btn_inicio.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c; color: white; 
                font-weight: bold; font-size: 18px; height: 50px; border-radius: 10px;
            }
            QPushButton:hover { background-color: #c0392b; }
        """)
        self.layout_principal.addWidget(self.btn_inicio)
        
        self.lbl_resultado = QLabel("¿Quién ganará? 🏆")
        self.lbl_resultado.setAlignment(Qt.AlignCenter)
        self.lbl_resultado.setStyleSheet("font-size: 20px; margin-top: 10px;")
        self.layout_principal.addWidget(self.lbl_resultado)